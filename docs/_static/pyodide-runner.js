/**
 * Pyodide-powered "▶ Run" button for code cells.
 *
 * Adds a Run button next to the Copy button on every code-cell block.
 * Clicking Run loads Pyodide (WebAssembly CPython) on first use, then
 * executes the cell and shows output inline.
 */
(function () {
  "use strict";

  const PYODIDE_CDN =
    "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js";

  let pyodidePromise = null;

  /** Lazy-load Pyodide the first time someone clicks Run. */
  function loadPyodide() {
    if (pyodidePromise) return pyodidePromise;

    pyodidePromise = new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = PYODIDE_CDN;
      script.onload = async () => {
        try {
          /* global loadPyodide – provided by the CDN script */
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

  /** Run a code string and return { stdout, stderr }. */
  async function runCode(pyodide, code) {
    // Redirect stdout / stderr so we can capture them.
    pyodide.runPython(`
import sys, io
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()
`);
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
      pyodide.runPython(`
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
`);
    }
  }

  /** Create or update the output area below a code block. */
  function showOutput(container, text, isError) {
    let outputEl = container.querySelector(".pyodide-output");
    if (!outputEl) {
      outputEl = document.createElement("pre");
      outputEl.className = "pyodide-output";
      container.appendChild(outputEl);
    }
    outputEl.textContent = text || "(no output)";
    outputEl.classList.toggle("pyodide-error", isError);
    outputEl.style.display = "block";
  }

  /** Inject a Run button into a code-cell container. */
  function addRunButton(container) {
    const btn = document.createElement("button");
    btn.className = "pyodide-run-btn";
    btn.title = "Run this code (Pyodide)";
    btn.textContent = "▶ Run";

    btn.addEventListener("click", async () => {
      const codeEl = container.querySelector("pre code, pre");
      if (!codeEl) return;
      const code = codeEl.textContent;

      btn.disabled = true;
      btn.textContent = "⏳ Loading…";

      try {
        const pyodide = await loadPyodide();
        btn.textContent = "⏳ Running…";
        const { output, error } = await runCode(pyodide, code);
        showOutput(container, output, error);
      } catch (err) {
        showOutput(container, "Failed to load Pyodide:\n" + err.message, true);
      } finally {
        btn.disabled = false;
        btn.textContent = "▶ Run";
      }
    });

    // Insert at top of the container, next to the copy button area
    const highlight = container.querySelector(".highlight");
    if (highlight) {
      highlight.style.position = "relative";
      highlight.appendChild(btn);
    } else {
      container.prepend(btn);
    }
  }

  /** Find all code-cell blocks and attach Run buttons. */
  function init() {
    // myst-nb renders {code-cell} as <div class="cell ..."><div class="cell_input">...
    const cells = document.querySelectorAll(".cell .cell_input");
    cells.forEach(addRunButton);

    // Also target plain highlighted python blocks produced by myst-nb
    if (cells.length === 0) {
      document
        .querySelectorAll('div.highlight-python, div.highlight-default')
        .forEach(function (block) {
          // Skip if already handled
          if (block.closest(".cell_input")) return;
          addRunButton(block);
        });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
