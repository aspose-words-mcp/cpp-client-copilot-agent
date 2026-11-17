> Build-harness sample only: hand-authored starter, replayed locally. No live Copilot generation or runtime execution.

# C++ answer showcase

Runtime execution: **Not checked**. Replayed answers are not live Copilot generations.

## create-document

Create a document with a paragraph. Use Aspose.Words for C++ and provide a complete compilable C++ program with required headers and evidence citations.

Origin: saved-answer. Compilation: passed.

This is a hand-authored build-harness demonstration, not a Copilot response or MCP-verified answer. It creates a simple Word document. Compilation is checked separately; execution and output are not checked.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>

int main()
{
    auto document = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(document);
    builder->Writeln(u"Hello from Aspose.Words for C++.");
    document->Save(u"hello.docx");
    return 0;
}
```

