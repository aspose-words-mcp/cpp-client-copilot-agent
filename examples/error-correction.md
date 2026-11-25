# C++ error correction

Adapted from the Java examples workflow, with C++-specific causes observed in copilot-full-02. These illustrations were reviewed against local SDK paths; they were not compiled or run during this edit.

## C0/C1: Complete programs

A supported how-to answer needs its actual code, not just type names. Statements at global scope are not a standalone program.

Wrong fragment:
```text
#include <Aspose.Words.Cpp/Document.h>
auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
doc->Save(u"output.pdf");
```
Complete shape:
```cpp
#include <Aspose.Words.Cpp/Document.h>
int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    doc->Save(u"output.pdf");
    return 0;
}
```
The input file is required only for execution. Compilation does not load it.

## C2: C1083 — nonexistent include

Observed wrong paths include Aspose.Words.Cpp/Api/Document.h, Aspose.Words.Cpp/Aspose.Words.Cpp.h and system/make_object.h. A C++ namespace does not determine a header path. The installed package supplies Aspose.Words.Cpp/Document.h; use the SDK-relative header evidence supplied by the runner. Do not automatically rewrite every Model path: some internal paths exist, but guessed paths often do not.

## C3: C2027/C2039 — incomplete returned type

Before treating a missing member as an incorrect API, inspect whether its class is only forward-declared. Examples:

| Usage | Explicit header |
| --- | --- |
| SaveFormat enum values | Aspose.Words.Cpp/SaveFormat.h |
| ImportFormatMode | Aspose.Words.Cpp/ImportFormatMode.h |
| doc->get_Range()->Replace(...) | Aspose.Words.Cpp/Range.h |
| builder->get_Font()->set_Name(...) | Aspose.Words.Cpp/Font.h |
| doc->get_MailMerge()->Execute(...) | Aspose.Words.Cpp/MailMerging/MailMerge.h |
| Revisions collection members | Aspose.Words.Cpp/RevisionCollection.h |
| Sections collection members | Aspose.Words.Cpp/SectionCollection.h |
| FindReplaceOptions | Aspose.Words.Cpp/Replacing/FindReplaceOptions.h |

Adding the header resolves type visibility, not necessarily the overload. Verify the method signature too.

## C4/C5: Wrong overloads and undefined helpers

Check exact C++ signatures, parameter types and ownership. Declare inputs in the same program. Replace test-suite path helpers with plain example paths. Do not add unrelated libraries to conceal an SDK mismatch.

## C6/C7: Build versus runtime

Missing SDK/toolchain, build timeout and dependency problems are unavailable verification. Compiler/linker diagnostics require code or build review. A linked program is not proof that its conversion output is correct. Never run generated programs as part of this compile-only workflow.

## C8: Repairs and evidence

Return the full program, preserve requested behavior and supporting URLs, and record the initial and repaired results. Prose-only or unsupported answers are not compilation passes. Review answer coverage independently of whether it compiles.

## C9: Missing or unusable endpoint response

A successful CLI exit is not enough: confirm there is a final answer and a successful `words-cpp` tool call before treating generation as complete. If the CLI fails, the answer is empty, the required MCP evidence is missing, or the answer still omits `main()` after its format retry, the showcase runner retries in a fresh CLI session (two retries by default). These attempts do not resume the earlier session. If retries are exhausted, preserve the failure and report it; do not fill gaps with guessed APIs, citations, or claims that a feature is unsupported. In interactive use, retry the failed lookup/request and state clearly when verified endpoint evidence remains unavailable.

## Approved repair data flow

On --verify-code runs, the controller may send prior generated code, compiler errors with local paths removed, and SDK-relative header names back to Copilot. Raw local diagnostics remain in results.json for local inspection. The repair prompt does not include SDK header contents or license files. Compiler-feedback repairs are separate from generation retries: --repair-attempts defaults to two, while --generation-retries defaults to two fresh sessions for unusable responses. Both limits are configurable. Repair metadata and sanitized feedback are logged in repair-log.md. Review local artifacts before publishing them.
