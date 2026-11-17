# C++ Copilot showcase

Run questions in fresh Copilot CLI sessions, or replay a saved Markdown answer. Optional compilation extracts each `cpp`, `c++`, `cxx` or `cc` fenced block verbatim into its own temporary Windows build project. Programs are never executed by the runner. Incomplete snippets are not silently repaired or supplied with missing headers.

From the repository root:

```powershell
python showcase/scripts/run_copilot.py --run preview --all --dry-run
# Replay an existing answer without calling a model:
python showcase/scripts/run_copilot.py --run replay-01 --query-id create-document --answer-file path/to/answer.md --verify-code --packages examples/packages
# Generate one answer using an authenticated Copilot CLI and configured MCP URL:
python showcase/scripts/run_copilot.py --run sample-01
# Generate all selected questions and compile:
python showcase/scripts/run_copilot.py --run full-01 --all --verify-code --packages examples/packages
```

Install/authenticate Copilot CLI separately for live generation. The invocation follows the .NET client's CLI pattern but has not been live-tested here. MCP tools are allowed; shell and write tools are denied during generation. This means saved-response shell inspection cannot run in this mode; review warnings and narrow questions if evidence is truncated. The existing instruction and agent files are copied unchanged into temporary workspaces.

Compilation requires Windows C++ Build Tools, the v142 toolset and restored SDK packages 26.9.0; see [examples](../examples/README.md). No automatic SDK download occurs in the runner. Reports record compile success separately from generation. Missing tools/SDKs are unavailable verification, not passes; no-code answers are not compile passes. Use a new run name for every attempt; existing runs are not overwritten. Automatic repair and resume are not implemented.

Outputs under `runs/<name>/`: `showcase.md`, `metrics.md`, and `results.json`. Review/redact reports before publishing; diagnostics can contain local paths or source details. Generated runs are Git-ignored. The runner does not publish reports or include .NET showcase results as C++ evidence.

```powershell
python -B -m unittest discover -s showcase/scripts -p 'test_*.py'
```

## Checked sample

[Starter showcase](sample/showcase.md) · [Build metrics](sample/metrics.md). This is a hand-authored saved-answer replay that compiled with SDK 26.9.0; it is not a Copilot evaluation result. Generated code was not executed.
