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
