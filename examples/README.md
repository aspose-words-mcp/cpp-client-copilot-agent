# Build generated C++ examples

Windows x64 build project using C++17, the v142 toolset, and pinned Aspose.Words.Cpp / CodePorting framework packages **26.9.0**. This matches the existing local test setup; it is not a claim that 26.9.0 is the latest SDK. Install Visual Studio C++ Build Tools and Windows 10 SDK, plus NuGet CLI for restoration.

```powershell
Set-Location examples/build-project
nuget restore packages.config -PackagesDirectory packages
.\build.ps1
# Optional execution of the reviewed starter:
.\build.ps1 -Run
```

The starter in `src/main.cpp` creates `build-project/outputs/hello.docx` when run with `-Run`. Building does not run it. A build pass is not runtime/output verification. Evaluation restrictions apply without an appropriate SDK license; do not commit license files.

To reuse restored packages, pass `-PackagesDirectory 'C:\path\to\packages'`. To compile another complete program, pass `-SourceFile 'C:\path\to\answer.cpp'`. Each example must contain its own includes and entry point. Multi-file projects require explicit project changes; fragments may fail compilation. `-PlatformToolset` can select another installed compatible toolset.

The showcase runner builds extracted C++ fences in temporary copies of this project and never executes generated programs. Inspect documents separately after any manually authorized run. SDK packages are not bundled and are ignored by Git.

## C++ build and repair guidance

Read [C++ build rules](cpp-build-rules.instructions.md) and [error-correction examples](error-correction.md). These adapt the Java workflow to the existing MSVC project and pinned C++ SDK; Maven/JDK settings do not apply. The source in `src/main.cpp` and the vcxproj and build.ps1 in `build-project/` already provide the C++ equivalent of the Java fixture and pom.xml.

The showcase runner explicitly includes both guidance files in generation prompts. It compiles and links locally and requests up to two compiler-driven repairs per answer by default; `--repair-attempts` configures this limit (0–5). For live generation, it also retries up to two times in fresh CLI sessions by default when the CLI fails, the final answer or successful `words-cpp` evidence is missing, or the answer still lacks `main()` after its format retry. Use `--generation-retries` to configure that limit (0–5). These are new attempts, not resumptions of the earlier session. Copilot shell/write access stays disabled. Only the controller builds programs; neither controller nor Copilot executes them. Existing .github instruction files are unchanged.

Repair requests send previous generated examples, compiler error text with local paths removed, and selected SDK-relative header names to Copilot. They do not send SDK source/header contents or licenses. Each run records repair-log.md plus original/repaired answers and actual build results in results.json. A timeout or failed question is recorded and remaining questions continue after configured generation retries are exhausted. No-code answers never count as compilation passes; review them for task coverage.

## Folder layout

```text
examples/
  cpp-build-rules.instructions.md
  error-correction.md
  README.md
  src/
    main.cpp
  build-project/
    build.ps1
    WordsCppExamples.vcxproj
    packages.config
```

`src` is a source-code convention, not a C++ compiler requirement. It separates the starter program from build configuration and guidance, matching the Java project's organization. The build script and project both default to `../src/main.cpp`. Restored packages, build output and optional runtime outputs live under `build-project/` and are ignored by Git. Existing external SDK package directories still work with `-PackagesDirectory`.
