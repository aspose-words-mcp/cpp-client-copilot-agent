# C++ build rules

Read examples/error-correction.md before writing code. These rules govern how to answer; do not omit requested code merely to avoid a compiler failure.

| Setting | Contract |
| --- | --- |
| Platform | Windows x64, MSVC v142, Windows SDK |
| Language | C++17 |
| Packages | Aspose.Words.Cpp and CodePorting.Translator.Cs2Cpp.Framework 26.9.0 |
| Source | Each cpp fence is an independent main.cpp |
| Check | Compile and link only; no execution |
| Warnings | Existing project /W3; not warnings-as-errors |

- C0: Answer supported how-to questions with code. Conceptual answers may be prose. If an operation is unsupported, explain with MCP evidence; do not invent an API or claim a compile pass.
- C1: Supply one complete program with int main(), all includes and all declarations. Keep helper functions/classes outside main. No ellipses, omitted setup or disconnected continuation blocks.
- C2: Use existing SDK headers, with their exact spelling and case. Do not invent umbrella headers, Api/Document.h, system/make_object.h or system/make_array.h. Prefer public forwarding headers rather than guessing Model paths.
- C3: Include concrete returned types and enums explicitly. Document.h alone does not define Font, Range, MailMerge, RevisionCollection, SectionCollection or SaveFormat. Include each type you dereference or use.
- C4: Verify overloads and ownership types through Words C++ MCP. Use System::SharedPtr and System::MakeObject where required, and UTF-16 literals. Do not translate Java/.NET signatures mechanically.
- C5: Declare every variable and helper in this program. No GetMyDir, Assert, BoxVector or sample-test helpers unless implemented here. Keep the requested behavior when repairing.
- C6: Use only the pinned SDK, its CodePorting dependency and the C++ standard library. Describe required files, licenses and external services. Compilation does not validate their availability.
- C7: On a compiler error, repair the actual cause using verified headers and signatures. The showcase requests at most two compiler-driven repairs by default; its --repair-attempts option can change this limit. Never delete functionality or substitute an empty main just to pass. Infrastructure failures are not evidence of bad API code.
- C8: Return the entire corrected answer and retain its supporting documentation citations. Add citations only from retrieved evidence. Flag a mistaken original citation rather than treating it as supporting evidence. Do not claim runtime execution or document correctness.
- C9: Base API and behavior claims on successful Aspose.Words C++ MCP evidence. If a lookup or tool call fails, returns no useful result, or the final answer is missing, retry the request rather than inventing a signature, citation, or unsupported-feature claim. The showcase retries unusable generation attempts in fresh CLI sessions (two retries by default); if those are exhausted, report the failure for review.

The showcase runner injects these rules into its generation prompt. Its retry limits are configurable with --generation-retries and --repair-attempts. Existing .github instructions are unchanged. In interactive Copilot use, explicitly ask the agent to read both examples guidance files before generating an answer.
