/**
 * Pyodide-powered "▶ Run" button for code cells.
 *
 * Replaces static <pre> blocks with editable <textarea> elements.
 * Users can modify code, click Run to execute via Pyodide (in-browser
 * WebAssembly Python), and click Reset to restore the original code.
 */
(function () {
  "use strict";

  const PYODIDE_CDN =
    "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js";

  // Hint the browser to start fetching the Pyodide script immediately.
  var prelink = document.createElement("link");
  prelink.rel = "preload";
  prelink.href = PYODIDE_CDN;
  prelink.as = "script";
  document.head.appendChild(prelink);

  let pyodidePromise = null;

  /** Lazy-load Pyodide the first time someone clicks Run. */
  function loadPyodide() {
    if (pyodidePromise) return pyodidePromise;

    pyodidePromise = new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = PYODIDE_CDN;
      script.onload = async () => {
        try {
          const py = await globalThis.loadPyodide();
          resolve(py);
        } catch (err) {
          reject(err);
        }
      };
      script.onerror = reject;
      document.head.appendChild(script);
    });
    return pyodidePromise;
  }

  /** Run a code string and return { output, error }. */
  async function runCode(pyodide, code) {
    pyodide.runPython(
      "import sys, io\nsys.stdout = io.StringIO()\nsys.stderr = io.StringIO()"
    );
    try {
      const result = pyodide.runPython(code);
      const stdout = pyodide.runPython("sys.stdout.getvalue()");
      const stderr = pyodide.runPython("sys.stderr.getvalue()");
      let output = stdout;
      if (stderr) output += stderr;
      if (result !== undefined && result !== null && String(result) !== "None") {
        output += String(result);
      }
      return { output: output, error: false };
    } catch (err) {
      const stderr = pyodide.runPython("sys.stderr.getvalue()");
      return { output: stderr + "\n" + err.message, error: true };
    } finally {
      pyodide.runPython("sys.stdout = sys.__stdout__\nsys.stderr = sys.__stderr__");
    }
  }

  /** Show or update the output area below the editor. */
  function showOutput(wrapper, text, isError) {
    var el = wrapper.querySelector(".pyodide-output");
    if (!el) {
      el = document.createElement("pre");
      el.className = "pyodide-output";
      wrapper.appendChild(el);
    }
    el.textContent = text || "(no output)";
    el.classList.toggle("pyodide-error", isError);
    el.style.display = "block";
  }

  /** Auto-resize textarea to fit content. */
  function autoResize(textarea) {
    textarea.style.height = "auto";
    textarea.style.height = textarea.scrollHeight + "px";
  }

  /** Convert a code block into an editable cell with Run/Reset/Copy buttons. */
  function makeEditable(container) {
    var preEl = container.querySelector("pre");
    if (!preEl) return;

    var codeEl = preEl.querySelector("code") || preEl;
    var originalCode = codeEl.textContent;

    // Create wrapper
    var wrapper = document.createElement("div");
    wrapper.className = "pyodide-cell";

    // Toolbar with buttons
    var toolbar = document.createElement("div");
    toolbar.className = "pyodide-toolbar";

    var runBtn = document.createElement("button");
    runBtn.className = "pyodide-run-btn";
    runBtn.textContent = "▶ Run";
    runBtn.title = "Run this code (Shift+Enter)";

    var resetBtn = document.createElement("button");
    resetBtn.className = "pyodide-reset-btn";
    resetBtn.textContent = "↺ Reset";
    resetBtn.title = "Restore original code";

    var copyBtn = document.createElement("button");
    copyBtn.className = "pyodide-copy-btn";
    copyBtn.textContent = "📋 Copy";
    copyBtn.title = "Copy code to clipboard";

    toolbar.appendChild(runBtn);
    toolbar.appendChild(resetBtn);
    toolbar.appendChild(copyBtn);

    // Editable textarea
    var textarea = document.createElement("textarea");
    textarea.className = "pyodide-editor";
    textarea.value = originalCode;
    textarea.spellcheck = false;
    textarea.autocomplete = "off";
    textarea.autocorrect = "off";
    textarea.autocapitalize = "off";

    // Replace the original pre block
    wrapper.appendChild(toolbar);
    wrapper.appendChild(textarea);
    container.innerHTML = "";
    container.appendChild(wrapper);

    // Auto-size on load and input
    autoResize(textarea);
    textarea.addEventListener("input", function () { autoResize(textarea); });

    // Shift+Enter to run
    textarea.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && e.shiftKey) {
        e.preventDefault();
        runBtn.click();
      }
      // Tab inserts spaces instead of moving focus
      if (e.key === "Tab") {
        e.preventDefault();
        var start = textarea.selectionStart;
        var end = textarea.selectionEnd;
        textarea.value = textarea.value.substring(0, start) + "    " + textarea.value.substring(end);
        textarea.selectionStart = textarea.selectionEnd = start + 4;
      }
    });

    // Run button
    runBtn.addEventListener("click", async function () {
      var code = textarea.value;
      runBtn.disabled = true;
      runBtn.textContent = "⏳ Loading…";
      try {
        var pyodide = await loadPyodide();
        runBtn.textContent = "⏳ Running…";
        var result = await runCode(pyodide, code);
        showOutput(wrapper, result.output, result.error);
      } catch (err) {
        showOutput(wrapper, "Failed to load Pyodide:\n" + err.message, true);
      } finally {
        runBtn.disabled = false;
        runBtn.textContent = "▶ Run";
      }
    });

    // Reset button
    resetBtn.addEventListener("click", function () {
      textarea.value = originalCode;
      autoResize(textarea);
      var outputEl = wrapper.querySelector(".pyodide-output");
      if (outputEl) outputEl.style.display = "none";
    });

    // Copy button
    copyBtn.addEventListener("click", function () {
      navigator.clipboard.writeText(textarea.value).then(function () {
        copyBtn.textContent = "✓ Copied!";
        setTimeout(function () { copyBtn.textContent = "📋 Copy"; }, 1500);
      });
    });
  }

  /** Find all code-cell blocks and make them editable. */
  function init() {
    // myst-nb renders {code-cell} as <div class="cell ..."><div class="cell_input">...
    var cells = document.querySelectorAll(".cell .cell_input");
    cells.forEach(makeEditable);

    // Fallback: target plain highlighted python blocks
    if (cells.length === 0) {
      document
        .querySelectorAll("div.highlight-python, div.highlight-default")
        .forEach(function (block) {
          if (block.closest(".cell_input")) return;
          makeEditable(block);
        });
    }

    // Preload Pyodide in the background
    if (document.querySelectorAll(".cell .cell_input, div.highlight-python").length > 0) {
      (typeof requestIdleCallback === "function" ? requestIdleCallback : function (cb) { setTimeout(cb, 2000); })(
        function () { loadPyodide(); }
      );
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
