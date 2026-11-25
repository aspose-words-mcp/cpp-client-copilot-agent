# C++ Copilot showcase

Run questions in fresh Copilot CLI sessions, or replay a saved Markdown answer. Optional compilation first tests each C++ fence unchanged. If it has no entry point, the checker tries an empty `main()` for declarations, then wraps executable statements in `main()` with unconditional includes kept outside. A continuation fence can reuse the preceding successfully wrapped snippet from the same answer. Every attempted strategy and compiler diagnostic is retained in `results.json`; successful harness code replaces the partial fence in `showcase.md` with an explicit harness label. The original response remains in `results.json`. Original answers, headers and API calls remain unchanged.

Programs are never executed by the runner. A compilation pass confirms compilation and linking only, not document conversion or output correctness. An unsuccessful fragment may require missing context; review its diagnostics before concluding that the API example is wrong. Conditional preprocessor blocks are not automatically moved into a statement harness.

From the repository root:

```powershell
python showcase/scripts/run_copilot.py --run preview --all --dry-run
# Replay an existing answer without calling a model:
python showcase/scripts/run_copilot.py --run replay-01 --query-id word-to-pdf-01 --answer-file path/to/answer.md --verify-code --packages examples/build-project/packages
# Generate one answer using an authenticated Copilot CLI and configured MCP URL:
python showcase/scripts/run_copilot.py --run sample-01
# Generate all selected questions and compile:
python showcase/scripts/run_copilot.py --run full-01 --all --verify-code --packages examples/build-project/packages
```

Install/authenticate Copilot CLI separately for live generation. The invocation follows the .NET client's CLI pattern but has not been live-tested here. MCP tools are allowed; shell and write tools are denied during generation. This means saved-response shell inspection cannot run in this mode; review warnings and narrow questions if evidence is truncated. The existing instruction and agent files are copied unchanged into temporary workspaces.

Compilation requires Windows C++ Build Tools, the v142 toolset and restored SDK packages 26.9.0; see [examples](../examples/README.md). No automatic SDK download occurs in the runner. Reports record compile success separately from generation. Missing tools/SDKs are unavailable verification, not passes; no-code answers are not compile passes. Use a new run name for every attempt; existing runs are not overwritten. Compiler-feedback repairs are bounded by --repair-attempts (default 2); generation resume is not implemented.

Outputs under `runs/<name>/`: `showcase.md`, `metrics.md`, and `results.json`. Review/redact reports before publishing; diagnostics can contain local paths or source details. Generated runs are Git-ignored. The runner does not publish reports or include .NET showcase results as C++ evidence.

```powershell
python -B -m unittest discover -s showcase/scripts -p 'test_*.py'
```

## Checked sample

[Starter showcase](sample/showcase.md) · [Build metrics](sample/metrics.md). This is a hand-authored saved-answer replay that compiled with SDK 26.9.0; it is not a Copilot evaluation result. Generated code was not executed.

## Published C++ showcase

[published-01](runs/published-01/showcase.md) matches all 99 questions and 15 categories of the .NET reference report, with C++ MCP evidence, compiled C++ examples, and preserved failures. Read the [metrics](runs/published-01/metrics.md) for shared-source counts and execution limitations. This is a Codex-authored MCP-assisted run, not GitHub Copilot CLI output.

## Recheck an existing run

No Copilot or MCP calls are made. Previous reports are backed up inside the run folder before compilation results are updated. Use the directory containing the restored SDK packages:

```powershell
python showcase/scripts/recheck_run.py --run copilot-full-01 --packages "D:\Faisalabad\AsposeMCP\November\gitlab\words-cpp-code-tests\packages" --workers 2
```

To test a successful harness yourself, copy its full code into `examples/src/main.cpp`, then use `examples/build-project/build.ps1` with the same `-PackagesDirectory`. Runtime testing additionally needs the input files, license and output checks required by that example.

## Complete programs in generated reports

The runner adds a per-question requirement for one standalone C++17 program with verified headers and `int main()`. It retries generation once if a C++ fence omits an entry point. Generation attempts and format warnings are saved in `results.json`. Instruction and agent files are unchanged.

The report displays the complete compiled source when the checker supplied a harness. An incomplete fragment without a successful harness is flagged rather than displayed as a runnable program; its original text remains in the JSON results. `--verify-code` compiles and links through the local checker. Copilot shell access remains disabled and programs are not executed. A pass is not a runtime or output validation result.

## Compiler-feedback repairs

New runs load examples/cpp-build-rules.instructions.md and examples/error-correction.md explicitly. Existing SDK header paths are supplied as generation evidence. With --verify-code, compiler errors are returned to Copilot for at most two repair attempts (set --repair-attempts 0 to disable). The previous answer and compiler errors have local paths removed; selected SDK header names are relative to the include directory. Runtime execution remains disabled. Failed generation no longer stops the remaining questions.

```powershell
python showcase/scripts/run_copilot.py --run copilot-full-03 --all --verify-code --packages "D:\Faisalabad\AsposeMCP\November\gitlab\words-cpp-code-tests\packages" --repair-attempts 2 --timeout 600
```

repair-log.md records sanitized feedback and final statuses; results.json retains every returned generation attempt and its compiler result. Earlier run folders are not changed. recheck_run.py only recompiles saved answers; it does not request model repairs. A repair pass must still be reviewed for requested behavior and evidence. Compilation alone cannot prove that the answer is correct or that a document operation works.
