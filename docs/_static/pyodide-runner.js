/**
 * Pyodide-powered "▶ Run" button for code cells.
 *
 * Replaces static <pre> blocks with editable <textarea> elements.
 * Users can modify code, click Run to execute via Pyodide (in-browser
 * WebAssembly Python), and click Reset to restore the original code.
 *
 * Compatible with Chrome, Edge, Firefox, Safari.
 */
(function () {
  "use strict";

  var PYODIDE_CDN =
    "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js";

  // Hint the browser to start fetching the Pyodide script immediately.
  try {
    var prelink = document.createElement("link");
    prelink.rel = "preload";
    prelink.href = PYODIDE_CDN;
    prelink.as = "script";
    prelink.crossOrigin = "anonymous";
    document.head.appendChild(prelink);
  } catch (e) { /* preload is optional */ }

  var pyodideReady = null;

  /** Lazy-load Pyodide the first time someone clicks Run. */
  function ensurePyodide() {
    if (pyodideReady) return pyodideReady;

    pyodideReady = new Promise(function (resolve, reject) {
      var script = document.createElement("script");
      script.src = PYODIDE_CDN;
      script.crossOrigin = "anonymous";
      script.onload = function () {
        // Pyodide script sets window.loadPyodide
        var loader = (typeof globalThis !== "undefined" && globalThis.loadPyodide) || window.loadPyodide;
        if (!loader) { reject(new Error("Pyodide loader not found")); return; }
        loader().then(resolve).catch(reject);
      };
      script.onerror = function () { reject(new Error("Failed to load Pyodide CDN")); };
      document.head.appendChild(script);
    });
    return pyodideReady;
  }

  /** Run Python code and capture stdout/stderr. */
  function runCode(pyodide, code) {
    pyodide.runPython(
      "import sys, io\nsys.stdout = io.StringIO()\nsys.stderr = io.StringIO()"
    );
    try {
      var result = pyodide.runPython(code);
      var stdout = pyodide.runPython("sys.stdout.getvalue()");
      var stderr = pyodide.runPython("sys.stderr.getvalue()");
      var output = stdout;
      if (stderr) output += stderr;
      if (result !== undefined && result !== null && String(result) !== "None") {
        output += String(result);
      }
      return { output: output, error: false };
    } catch (err) {
      var errStderr = "";
      try { errStderr = pyodide.runPython("sys.stderr.getvalue()"); } catch (e) { /* ignore */ }
      return { output: errStderr + "\n" + err.message, error: true };
    } finally {
      try { pyodide.runPython("sys.stdout = sys.__stdout__\nsys.stderr = sys.__stderr__"); } catch (e) { /* ignore */ }
    }
  }

  /** Show or update the output area. */
  function showOutput(wrapper, text, isError) {
    var el = wrapper.querySelector(".pyodide-output");
    if (!el) {
      el = document.createElement("pre");
      el.className = "pyodide-output";
      wrapper.appendChild(el);
    }
    el.textContent = text || "(no output)";
    if (isError) { el.classList.add("pyodide-error"); } else { el.classList.remove("pyodide-error"); }
    el.style.display = "block";
  }

  /** Auto-resize textarea to fit its content. */
  function autoResize(ta) {
    ta.style.height = "auto";
    ta.style.height = ta.scrollHeight + "px";
  }

  /** Cross-browser copy to clipboard. */
  function copyToClipboard(text, btn) {
    function onSuccess() {
      btn.textContent = "✓ Copied!";
      setTimeout(function () { btn.textContent = "\uD83D\uDCCB Copy"; }, 1500);
    }
    function onFail() {
      // Fallback: select a hidden textarea
      var tmp = document.createElement("textarea");
      tmp.value = text;
      tmp.style.position = "fixed";
      tmp.style.opacity = "0";
      document.body.appendChild(tmp);
      tmp.select();
      try { document.execCommand("copy"); onSuccess(); } catch (e) { /* silent */ }
      document.body.removeChild(tmp);
    }
    if (navigator.clipboard && typeof navigator.clipboard.writeText === "function") {
      navigator.clipboard.writeText(text).then(onSuccess).catch(onFail);
    } else {
      onFail();
    }
  }

  /** Convert a code block into an editable cell with Run / Reset / Copy. */
  function makeEditable(container) {
    var preEl = container.querySelector("pre");
    if (!preEl) return;
    // Avoid double-init
    if (container.querySelector(".pyodide-cell")) return;

    var codeEl = preEl.querySelector("code") || preEl;
    var originalCode = codeEl.textContent;

    // Build wrapper
    var wrapper = document.createElement("div");
    wrapper.className = "pyodide-cell";

    // Toolbar
    var toolbar = document.createElement("div");
    toolbar.className = "pyodide-toolbar";

    var runBtn = document.createElement("button");
    runBtn.className = "pyodide-run-btn";
    runBtn.type = "button";
    runBtn.textContent = "\u25B6 Run";
    runBtn.title = "Run this code (Shift+Enter)";

    var resetBtn = document.createElement("button");
    resetBtn.className = "pyodide-reset-btn";
    resetBtn.type = "button";
    resetBtn.textContent = "\u21BA Reset";
    resetBtn.title = "Restore original code";

    var copyBtn = document.createElement("button");
    copyBtn.className = "pyodide-copy-btn";
    copyBtn.type = "button";
    copyBtn.textContent = "\uD83D\uDCCB Copy";
    copyBtn.title = "Copy code to clipboard";

    toolbar.appendChild(runBtn);
    toolbar.appendChild(resetBtn);
    toolbar.appendChild(copyBtn);

    // Editable textarea
    var textarea = document.createElement("textarea");
    textarea.className = "pyodide-editor";
    textarea.value = originalCode;
    textarea.spellcheck = false;
    textarea.setAttribute("autocomplete", "off");
    textarea.setAttribute("autocorrect", "off");
    textarea.setAttribute("autocapitalize", "off");

    // Replace original content
    wrapper.appendChild(toolbar);
    wrapper.appendChild(textarea);
    container.innerHTML = "";
    container.appendChild(wrapper);

    // Size & events
    autoResize(textarea);
    textarea.addEventListener("input", function () { autoResize(textarea); });

    textarea.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && e.shiftKey) {
        e.preventDefault();
        runBtn.click();
      }
      if (e.key === "Tab") {
        e.preventDefault();
        var s = textarea.selectionStart;
        var end = textarea.selectionEnd;
        textarea.value = textarea.value.substring(0, s) + "    " + textarea.value.substring(end);
        textarea.selectionStart = textarea.selectionEnd = s + 4;
      }
    });

    runBtn.addEventListener("click", function () {
      var code = textarea.value;
      runBtn.disabled = true;
      runBtn.textContent = "\u23F3 Loading\u2026";
      ensurePyodide().then(function (pyodide) {
        runBtn.textContent = "\u23F3 Running\u2026";
        var result = runCode(pyodide, code);
        showOutput(wrapper, result.output, result.error);
      }).catch(function (err) {
        showOutput(wrapper, "Failed to load Pyodide:\n" + err.message, true);
      }).finally(function () {
        runBtn.disabled = false;
        runBtn.textContent = "\u25B6 Run";
      });
    });

    resetBtn.addEventListener("click", function () {
      textarea.value = originalCode;
      autoResize(textarea);
      var out = wrapper.querySelector(".pyodide-output");
      if (out) out.style.display = "none";
    });

    copyBtn.addEventListener("click", function () {
      copyToClipboard(textarea.value, copyBtn);
    });
  }

  /** Find code-cell blocks and make them editable. */
  function init() {
    var cells = document.querySelectorAll(".cell .cell_input");
    console.log("[pyodide-runner] Found " + cells.length + " code cells");

    for (var i = 0; i < cells.length; i++) {
      try { makeEditable(cells[i]); } catch (e) { console.error("[pyodide-runner]", e); }
    }

    // Fallback for pages without {code-cell} blocks
    if (cells.length === 0) {
      var blocks = document.querySelectorAll("div.highlight-python, div.highlight-default");
      for (var j = 0; j < blocks.length; j++) {
        if (blocks[j].parentElement && blocks[j].parentElement.classList.contains("cell_input")) continue;
        try { makeEditable(blocks[j]); } catch (e) { console.error("[pyodide-runner]", e); }
      }
    }

    // Preload Pyodide in the background
    setTimeout(function () { ensurePyodide(); }, 2000);
  }

  // Run after DOM is ready and copybutton.js has finished (it uses setTimeout 250ms)
  function scheduleInit() { setTimeout(init, 500); }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", scheduleInit);
  } else {
    scheduleInit();
  }
})();
