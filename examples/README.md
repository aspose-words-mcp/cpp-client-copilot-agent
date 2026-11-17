# Build generated C++ examples

Windows x64 build project using C++17, the v142 toolset, and pinned Aspose.Words.Cpp / CodePorting framework packages **26.9.0**. This matches the existing local test setup; it is not a claim that 26.9.0 is the latest SDK. Install Visual Studio C++ Build Tools and Windows 10 SDK, plus NuGet CLI for restoration.

```powershell
Set-Location examples
nuget restore packages.config -PackagesDirectory packages
.\build.ps1
# Optional execution of the reviewed starter:
.\build.ps1 -Run
```

The starter creates `outputs/hello.docx`. Building does not run it. A build pass is not runtime/output verification. Evaluation restrictions apply without an appropriate SDK license; do not commit license files.

To reuse restored packages, pass `-PackagesDirectory 'C:\path\to\packages'`. To compile another complete program, pass `-SourceFile 'C:\path\to\answer.cpp'`. Each example must contain its own includes and entry point. Multi-file projects require explicit project changes; fragments may fail compilation. `-PlatformToolset` can select another installed compatible toolset.

The showcase runner builds extracted C++ fences in temporary copies of this project and never executes generated programs. Inspect documents separately after any manually authorized run. SDK packages are not bundled and are ignored by Git.
