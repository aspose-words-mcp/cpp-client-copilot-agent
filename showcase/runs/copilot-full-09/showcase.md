# C++ answer showcase

Runtime execution: **Not checked**. Replayed answers are not live Copilot generations.

## word-to-pdf-01

How to convert DOC/DOCX to PDF?

Origin: copilot-cli. Compilation: passed.

Load the existing DOC/DOCX into `Document`, then save with a `.pdf` filename. Aspose.Words detects the input format and selects PDF output from the output extension. [Conversion guide](https://docs.aspose.com/words/cpp/convert-a-document-to-pdf/) · [Document constructor](https://reference.aspose.com/words/cpp/aspose.words/document/document/) · [Save API](https://reference.aspose.com/words/cpp/aspose.words/document/save/)

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    doc->Save(u"output.pdf");
    return 0;
}
```

Put `input.docx` beside the program, or change the input path to your `.doc` file. No Microsoft Office or external service is needed. For unrestricted, unwatermarked output, apply a valid Aspose.Words license; the unlicensed trial adds a watermark and limits document size ([licensing](https://docs.aspose.com/words/cpp/licensing/)). The MCP lookup resolved to latest stable rather than 26.9.0, so I can’t confirm the signatures specifically against that pinned version. The requested `examples/error-correction.md` was not present in the workspace; I followed the C++ rules included in your prompt.

## word-to-pdf-02

How to convert a document to PDF?

Origin: copilot-cli. Compilation: passed.

Load a document and save it with a `.pdf` extension; Aspose.Words infers the output format. See the [conversion guide](https://docs.aspose.com/words/cpp/convert-a-document-to-pdf/) and [`Document::Save`](https://reference.aspose.com/words/cpp/aspose.words/document/save/).

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <system/smart_ptr.h>

int main()
{
    auto sample = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(sample);
    builder->Writeln(u"Hello from Aspose.Words!");
    sample->Save(u"sample.docx");

    auto document = System::MakeObject<Aspose::Words::Document>(u"sample.docx");
    document->Save(u"output.pdf");
    return 0;
}
```

The example creates `sample.docx` and converts it to `output.pdf`, overwriting files with those names. To convert your own document, remove the sample-creation statements and replace `sample.docx` with its path. No external service is required. Without a license, [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/) apply.

The requested `examples\error-correction.md` file was not present; the guidance included in your prompt was used instead.

## word-to-pdf-03

How to convert DOC/DOCX to PDF in C++?

Origin: copilot-cli. Compilation: passed.

Load the file as an `Aspose::Words::Document`, then save with a `.pdf` filename. Aspose.Words detects the input format from the document and the output format from the extension; this works for DOC and DOCX without Microsoft Office. ([Conversion guide](https://docs.aspose.com/words/cpp/convert-a-document-to-pdf/), [Document constructor](https://reference.aspose.com/words/cpp/aspose.words/document/document/), [Save method](https://reference.aspose.com/words/cpp/aspose.words/document/save/))

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    // Change to "input.doc" to convert a legacy DOC file instead.
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    doc->Save(u"output.pdf");
    return 0;
}
```

Place `input.docx` (or `input.doc`) beside the program; an existing `output.pdf` will be overwritten. Build against Aspose.Words.Cpp and its CodePorting framework dependency. No credentials or external services are needed; use the SDK in accordance with its licensing terms. The MCP documentation index exposed only `latest-stable`, not a 26.9.0-specific API set, so exact-version compatibility could not be independently confirmed.

## word-to-pdf-04

How do I convert a DOC/DOCX document to PDF in C++?

Origin: copilot-cli. Compilation: passed.

Use `Document` to load the input (the file format is detected automatically), then save with a `.pdf` filename. Change `input.docx` to `input.doc` for a DOC source.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    auto document = System::MakeObject<Aspose::Words::Document>(
        System::String(u"input.docx"));
    document->Save(System::String(u"output.pdf"));
    return 0;
}
```

Place the input file where the program can find it; an existing `output.pdf` will be overwritten. Build against Aspose.Words.Cpp and CodePorting.Translator.Cs2Cpp.Framework 26.9.0. Production use requires a valid Aspose.Words license to remove evaluation limitations; no credentials or external services are needed. [Document loading](https://reference.aspose.com/words/cpp/aspose.words/document/document/) · [Saving and format detection](https://reference.aspose.com/words/cpp/aspose.words/document/save/) · [Installation and licensing](https://docs.aspose.com/words/cpp/installation/)

## word-to-html-01

How to convert DOC/DOCX to HTML?

Origin: copilot-cli. Compilation: passed.

Load the `.doc` or `.docx` file, then save with an `.html` extension. Aspose.Words detects the input format from the file and chooses the output format from the extension. ([Document constructor](https://reference.aspose.com/words/cpp/aspose.words/document/document/), [Save](https://reference.aspose.com/words/cpp/aspose.words/document/save/))

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    doc->Save(u"output.html");
    return 0;
}
```

Use `input.doc` instead if that’s your source file. The input must exist; the output file is overwritten if it already exists. No credentials or external service are needed. Configure an Aspose.Words license for your intended use. The MCP reference resolved to `latest-stable`, not a 26.9.0-specific snapshot; see the [HTML conversion guide](https://docs.aspose.com/words/cpp/convert-a-document-to-html-mhtml-or-epub/).

## word-to-html-02

How to convert a document to HTML?

Origin: copilot-cli. Compilation: passed.

Load the document and save it as HTML using [`Document::Save`](https://reference.aspose.com/words/cpp/aspose.words/document/save/):

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/SaveFormat.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(
        System::String(u"input.docx"));
    doc->Save(u"output.html", Aspose::Words::SaveFormat::Html);
    return 0;
}
```

Place `input.docx` in the working directory. Existing `output.html` is overwritten. Without a license, evaluation limitations apply; see [licensing](https://reference.aspose.com/words/cpp/aspose.words/license/). No external service is needed.

## word-to-html-03

How to convert DOC/DOCX to HTML in C++?

Origin: copilot-cli. Compilation: passed.

Load the `.doc` or `.docx` into `Document`, then save it with `SaveFormat::Html`. The constructor detects the input format, and the explicit save format selects HTML. ([Document](https://reference.aspose.com/words/cpp/aspose.words/document/document/), [Save](https://reference.aspose.com/words/cpp/aspose.words/document/save/), [SaveFormat](https://reference.aspose.com/words/cpp/aspose.words/saveformat/))

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/SaveFormat.h>
#include <system/smart_ptr.h>

int main()
{
    System::SharedPtr<Aspose::Words::Document> doc =
        System::MakeObject<Aspose::Words::Document>(u"input.docx");

    doc->Save(u"output.html", Aspose::Words::SaveFormat::Html);
    return 0;
}
```

Set the input path to your existing DOC or DOCX file (for a legacy DOC, for example, use `input.doc`). The output file is overwritten if it already exists. This requires Aspose.Words for C++ and its CodePorting framework at the specified version, plus an appropriate license for your use; no external service or credentials are needed. Depending on save options, HTML may reference separate resource files such as fonts. ([HTML conversion and resources](https://docs.aspose.com/words/cpp/convert-a-document-to-html-mhtml-or-epub/))

## word-to-html-04

How do I convert a DOC/DOCX document to HTML in C++?

Origin: copilot-cli. Compilation: passed.

Place the source document beside the program as `input.docx` (or change the name to `input.doc`). Aspose.Words detects the input format from the file; `SaveFormat::Html` explicitly selects HTML output.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/SaveFormat.h>
#include <system/smart_ptr.h>

int main()
{
    auto document = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    document->Save(u"output.html", Aspose::Words::SaveFormat::Html);
    return 0;
}
```

The program needs the Aspose.Words for C++ and CodePorting framework packages you specified, plus the input file and an Aspose license. It needs no credentials or external services. If `output.html` already exists, it will be overwritten.

Sources: [Document loading](https://reference.aspose.com/words/cpp/aspose.words/document/document/), [`Document::Save`](https://reference.aspose.com/words/cpp/aspose.words/document/save/), and [`SaveFormat`](https://reference.aspose.com/words/cpp/aspose.words/saveformat/). The MCP reference endpoint exposed its latest-stable documentation rather than a version-specific 26.9.0 snapshot.

## word-to-excel-01

How to convert DOC/DOCX to Excel?

Origin: copilot-cli. Compilation: passed.

Aspose.Words for C++ can load a DOC or DOCX and save it as XLSX. Set `input.doc` or `input.docx` to your source file; the output path’s `.xlsx` extension selects the Excel format.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    doc->Save(u"output.xlsx");
    return 0;
}
```

The `Document` constructor detects the input format, and `Save` writes the XLSX file. The output file is overwritten if it already exists. [Conversion guide](https://docs.aspose.com/words/cpp/convert-a-document-to-excel/) · [Document API](https://reference.aspose.com/words/cpp/aspose.words/document/) · [Save API](https://reference.aspose.com/words/cpp/aspose.words/document/save/)

Build against Aspose.Words.Cpp and CodePorting.Translator.Cs2Cpp.Framework 26.9.0. A valid Aspose.Words license is needed for production use; no credentials or external services are required. The MCP reference index resolved the 26.9.0 request to `latest-stable`, so it did not provide a distinct 26.9.0 reference set. I did not compile or run this example. The requested `examples\error-correction.md` file was not present in the workspace.

## word-to-excel-02

How to convert a Word document to Excel?

Origin: copilot-cli. Compilation: passed.

Load the Word document and save it with an `.xlsx` extension; Aspose.Words [selects the output format from the extension](https://reference.aspose.com/words/cpp/aspose.words/document/save/). See the [Word-to-Excel guide](https://docs.aspose.com/words/cpp/convert-a-document-to-excel/).

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    doc->Save(u"output.xlsx");
    return 0;
}
```

Place `input.docx` in the working directory. An existing `output.xlsx` may be overwritten. No external service is required; without a license, evaluation restrictions apply.

The documentation endpoint returned latest-stable API evidence, not version-specific 26.9.0 evidence. The requested `examples\error-correction.md` file was not present in the workspace; the supplied error-correction guidance was used.

## word-to-excel-03

How to convert DOC/DOCX to XLSX in C++?

Origin: copilot-cli. Compilation: passed.

Aspose.Words can load a DOC or DOCX and save it as XLSX. Replace the input filename below with your existing document’s path.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/SaveFormat.h>
#include <system/smart_ptr.h>

int main()
{
    System::String inputFile(u"input.docx");
    System::String outputFile(u"output.xlsx");

    auto doc = System::MakeObject<Aspose::Words::Document>(inputFile);
    doc->Save(outputFile, Aspose::Words::SaveFormat::Xlsx);

    return 0;
}
```

The `Document` constructor detects the input format, and `Save` writes the specified format. An existing `output.xlsx` is overwritten. For unrestricted use, apply your Aspose.Words license; no external service is required. `XlsxSaveOptions` is available for additional export settings.

Sources: [Convert a document to Excel](https://docs.aspose.com/words/cpp/convert-a-document-to-excel/), [Document constructor](https://reference.aspose.com/words/cpp/aspose.words/document/document/), [Document.Save](https://reference.aspose.com/words/cpp/aspose.words/document/save/), [XlsxSaveOptions](https://reference.aspose.com/words/cpp/aspose.words.saving/xlsxsaveoptions/).

## word-to-excel-04

How do I convert a DOC/DOCX document to Excel in C++?

Origin: copilot-cli. Compilation: passed.

Aspose.Words for C++ can load a DOC or DOCX and save it as XLSX. Set `inputPath` to your source file and `outputPath` to the desired workbook path:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    const System::String inputPath(u"input.docx"); // Or "input.doc"
    const System::String outputPath(u"output.xlsx");

    auto document = System::MakeObject<Aspose::Words::Document>(inputPath);
    document->Save(outputPath);
    return 0;
}
```

The `.xlsx` extension selects the output format. You’ll need the input document and, for production use, a valid Aspose.Words license; no external service or credentials are required. See the [Word-to-Excel guide](https://docs.aspose.com/words/cpp/convert-a-document-to-excel/), the [`Document` constructor](https://reference.aspose.com/words/cpp/aspose.words/document/document/), and [`Document.Save`](https://reference.aspose.com/words/cpp/aspose.words/document/save/).

The configured API lookup did not have a 26.9.0-specific reference set, so the signatures above were checked against its latest-stable reference. I could not locate `examples/error-correction.md` in the workspace; I followed the coding rules included in your prompt.

## word-to-excel-05

How to convert Word to XLSX in C++?

Origin: copilot-cli. Compilation: passed.

Load the Word document and save it with an `.xlsx` extension; Aspose.Words determines the output format from the filename. See the [conversion guide](https://docs.aspose.com/words/cpp/convert-a-document-to-excel/) and [`Document::Save`](https://reference.aspose.com/words/cpp/aspose.words/document/save/).

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    doc->Save(u"output.xlsx");
    return 0;
}
```

Place `input.docx` in the working directory. An existing `output.xlsx` is overwritten. No external service or credentials are required; without a license, [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/) apply.

The documentation endpoint returned current API evidence, but could not independently verify version 26.9.0.

## word-to-excel-06

Can Aspose.Words convert DOCX to Excel?

Origin: copilot-cli. Compilation: no_code.

Yes. Aspose.Words for C++ can convert DOCX to Excel’s XLSX format by loading the Word file as a `Document` and saving it with an `.xlsx` extension. You can use `XlsxSaveOptions` to control XLSX-specific save settings. [Convert a document to Excel](https://docs.aspose.com/words/cpp/convert-a-document-to-excel/) · [Document.Save API](https://reference.aspose.com/words/cpp/aspose.words/document/save/)

## word-to-markdown-01

How to convert DOC/DOCX to Markdown?

Origin: copilot-cli. Compilation: passed.

Load the DOC or DOCX, then [save it](https://reference.aspose.com/words/cpp/aspose.words/document/save/) with an `.md` extension:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <system/smart_ptr.h>

int main()
{
    const System::String input = u"input.docx"; // Also accepts input.doc
    const bool createSample = false;

    if (createSample)
    {
        auto sample = System::MakeObject<Aspose::Words::Document>();
        auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(sample);
        builder->Writeln(u"Hello from a sample Word document.");
        sample->Save(input);
    }

    auto doc = System::MakeObject<Aspose::Words::Document>(input);
    doc->Save(u"output.md");
    return 0;
}
```

Place the input in the working directory, or set `createSample` to `true` to create one. **That option overwrites the input path**; saving also overwrites `output.md`. Embedded images are saved as separate files in the output folder by default ([image options](https://reference.aspose.com/words/cpp/aspose.words.saving/markdownsaveoptions/get_imagesfolder/)).

An Aspose.Words license removes evaluation limitations; no external service or Microsoft Word is required ([licensing](https://docs.aspose.com/words/cpp/insert-checkboxes-text-input-or-images-mail-merge/), [API overview](https://docs.aspose.com/words/cpp/api-reference/)).

## word-to-markdown-02

How to convert a Word document to Markdown?

Origin: copilot-cli. Compilation: passed.

Load the Word document and save it with a `.md` extension; Aspose.Words determines the output format from the extension ([Save reference](https://reference.aspose.com/words/cpp/aspose.words/document/save/)).

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    doc->Save(u"output.md");
    return 0;
}
```

Place `input.docx` in the working directory. An existing `output.md` is overwritten. No external service or credentials are required. Without a license, evaluation limitations apply ([licensing](https://docs.aspose.com/words/cpp/licensing/)).

The requested `examples/error-correction.md` file was not present; I used the guidance included in your prompt.

## word-to-markdown-03

How to convert DOC/DOCX to Markdown in C++?

Origin: copilot-cli. Compilation: passed.

Use `Document` to load the existing Word file, then save it with a `.md` extension; `Save(fileName)` selects the output format from that extension.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    System::String inputPath = u"input.docx"; // Use u"input.doc" for a DOC file.
    System::String outputPath = u"output.md";

    auto document = System::MakeObject<Aspose::Words::Document>(inputPath);
    document->Save(outputPath);

    return 0;
}
```

Place `input.docx` (or `input.doc`) in the program’s working directory, or change `inputPath` to its location. The program uses the Aspose.Words C++ SDK and its CodePorting dependency; no credentials or external services are needed. For licensed use, see Aspose’s [licensing documentation](https://docs.aspose.com/words/cpp/licensing/).

Sources: [Document constructor](https://reference.aspose.com/words/cpp/aspose.words/document/document/), [Document.Save](https://reference.aspose.com/words/cpp/aspose.words/document/save/) (format inferred from the file extension), and [MarkdownSaveOptions](https://reference.aspose.com/words/cpp/aspose.words.saving/markdownsaveoptions/) (Markdown save format).

## word-to-markdown-04

How do I convert a DOC/DOCX document to Markdown in C++?

Origin: copilot-cli. Compilation: passed.

Load the `.doc` or `.docx` into `Document`, then save with a `.md` filename. Aspose.Words detects the output format from the extension; its Markdown guide shows this conversion pattern. [Markdown conversion guide](https://docs.aspose.com/words/cpp/convert-a-document-to-markdown/) · [Document.Save API](https://reference.aspose.com/words/cpp/aspose.words/document/save/) · [Supported formats](https://docs.aspose.com/words/cpp/supported-document-formats/)

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    doc->Save(u"output.md");
    return 0;
}
```

Place `input.docx` in the program’s working directory, or change the path; use `input.doc` for a DOC file. Conversion needs no external service or credentials. Aspose’s evaluation mode is available; for licensed use, provide your local license file before processing. [License API](https://reference.aspose.com/words/cpp/aspose.words/license/)

The MCP verified the API against its `latest-stable` reference, but did not resolve the requested 26.9.0 version specifically.

## word-to-markdown-05

How to save a Word document as a Markdown file?

Origin: copilot-cli. Compilation: passed.

Load the Word document and call [`Save`](https://reference.aspose.com/words/cpp/aspose.words/document/save/) with an `.md` extension; Aspose.Words determines the output format from the extension.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <system/smart_ptr.h>

int main()
{
    auto sample = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(sample);
    builder->Writeln(u"Hello from a Word document.");
    sample->Save(u"sample.docx");

    auto doc = System::MakeObject<Aspose::Words::Document>(u"sample.docx");
    doc->Save(u"output.md");
    return 0;
}
```

The program creates `sample.docx` and converts it to `output.md`, overwriting either file if it already exists. To use your own document, remove the sample-creation statements and replace `sample.docx` in the constructor with its path.

A license is optional; the [trial](https://docs.aspose.com/words/cpp/licensing/) adds an evaluation watermark and limits document size. No external service is required. The requested `examples/error-correction.md` file was not present; I used the guidance included in your prompt.

## word-to-markdown-06

Can Aspose.Words convert DOCX to Markdown?

Origin: copilot-cli. Compilation: no_code.

Yes. Aspose.Words for C++ can load a DOCX and save it as Markdown; saving with a `.md` filename lets it determine the output format from the extension. Exported images are saved alongside the Markdown file by default, and you can configure their folder. [Convert a Document to Markdown](https://docs.aspose.com/words/cpp/convert-a-document-to-markdown/) · [`Document::Save`](https://reference.aspose.com/words/cpp/aspose.words/document/save/)

## word-to-image-01

How to convert DOC/DOCX to an image?

Origin: copilot-cli. Compilation: passed.

Load the document and save each page as a PNG using [`ImageSaveOptions`](https://docs.aspose.com/words/cpp/convert-a-document-to-an-image/). Page indices are [zero-based](https://reference.aspose.com/words/cpp/aspose.words.saving/pageset/pageset/).

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/SaveFormat.h>
#include <Aspose.Words.Cpp/Saving/ImageSaveOptions.h>
#include <Aspose.Words.Cpp/Saving/PageSet.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    auto options = System::MakeObject<Aspose::Words::Saving::ImageSaveOptions>(
        Aspose::Words::SaveFormat::Png);
    options->set_Resolution(150.0f);

    const int32_t pageCount = doc->get_PageCount();
    for (int32_t i = 0; i < pageCount; ++i)
    {
        options->set_PageSet(
            System::MakeObject<Aspose::Words::Saving::PageSet>(i));
        System::String output = System::String::Format(u"page_{0}.png", i + 1);
        doc->Save(output, options);
    }
    return 0;
}
```

Place `input.docx` in the working directory; change the path to use a DOC file instead. Existing `page_*.png` files with matching names are overwritten. No external service is needed. Without a license, [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/) apply.

The referenced `examples/error-correction.md` file was unavailable; I used the guidance included in your request.

## word-to-image-02

How to convert a Word document to an image?

Origin: copilot-cli. Compilation: passed.

Save the document to a filename with the image extension; Aspose.Words uses that extension to choose the output format. This example converts `input.docx` to PNG:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    doc->Save(u"output.png");
    return 0;
}
```

Place `input.docx` where the program can access it. The program needs Aspose.Words for C++ and its matching CodePorting dependency; use a valid Aspose license for licensed use. No credentials or external services are needed. For rendering controls, use `ImageSaveOptions`; for a single multi-page image file, Aspose documents multi-page TIFF.

Sources: [Convert a document to an image](https://docs.aspose.com/words/cpp/convert-a-document-to-an-image/), [Document.Save API](https://reference.aspose.com/words/cpp/aspose.words/document/save/), [ImageSaveOptions API](https://reference.aspose.com/words/cpp/aspose.words.saving/imagesaveoptions/), [multi-page TIFF](https://docs.aspose.com/words/cpp/saving-a-document-as-a-multipage-tiff/). The configured MCP exposed latest-stable documentation, not version-specific 26.9.0 evidence; I have not claimed a compile or runtime check.

## word-to-image-03

How to convert DOC/DOCX to PNG in C++?

Origin: copilot-cli. Compilation: passed.

Use `Document` to load either DOC or DOCX, then render each page as a separate PNG with `ImageSaveOptions` and `PageSet`. The page index is zero-based. [Image conversion guide](https://docs.aspose.com/words/cpp/convert-a-document-to-an-image/) · [PageSet API](https://reference.aspose.com/words/cpp/aspose.words.saving/pageset/pageset/) · [Save API](https://reference.aspose.com/words/cpp/aspose.words/document/save/)

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/SaveFormat.h>
#include <Aspose.Words.Cpp/Saving/ImageSaveOptions.h>
#include <Aspose.Words.Cpp/Saving/PageSet.h>
#include <system/object.h>
#include <system/smart_ptr.h>

int main()
{
    // Change the path to your existing .doc or .docx file.
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    auto options = System::MakeObject<Aspose::Words::Saving::ImageSaveOptions>(
        Aspose::Words::SaveFormat::Png);

    for (int page = 0; page < doc->get_PageCount(); ++page)
    {
        options->set_PageSet(
            System::MakeObject<Aspose::Words::Saving::PageSet>(page));

        System::String outputFile =
            System::String::Format(u"page_{0}.png", page + 1);

        doc->Save(outputFile, options);
    }

    return 0;
}
```

This writes `page_1.png`, `page_2.png`, and so on in the current directory; existing files with those names are overwritten. Provide a valid Aspose.Words license for licensed use. No external service or credentials are required.

## word-to-image-04

How do I convert a DOC/DOCX document to an image in C++?

Origin: copilot-cli. Compilation: passed.

Use `Document` to load the DOC/DOCX, then render each page with `ImageSaveOptions`. This writes one PNG per page; `PageSet` uses zero-based page indices. The MCP reference index resolved 26.9.0 requests to `latest-stable`, so these references are not specific to the pinned patch version.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/SaveFormat.h>
#include <Aspose.Words.Cpp/Saving/ImageSaveOptions.h>
#include <Aspose.Words.Cpp/Saving/PageSet.h>
#include <system/smart_ptr.h>
#include <system/string.h>
#include <cstdint>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    auto options =
        System::MakeObject<Aspose::Words::Saving::ImageSaveOptions>(
            Aspose::Words::SaveFormat::Png);

    for (int32_t pageIndex = 0; pageIndex < doc->get_PageCount(); ++pageIndex)
    {
        options->set_PageSet(
            System::MakeObject<Aspose::Words::Saving::PageSet>(pageIndex));

        doc->Save(
            System::String::Format(u"page-{0}.png", pageIndex + 1),
            options);
    }

    return 0;
}
```

Place `input.docx` in the program’s working directory, or change the path; the `Document` constructor detects the file format. Existing `page-N.png` files are overwritten. The example uses a local file and needs no credentials or external service; build it with the Aspose.Words for C++ SDK and its required license/dependency setup.

Sources: [Document loading and format detection](https://reference.aspose.com/words/cpp/aspose.words/document/), [`Document::Save`](https://reference.aspose.com/words/cpp/aspose.words/document/save/), [`ImageSaveOptions`](https://reference.aspose.com/words/cpp/aspose.words.saving/imagesaveoptions/), [`PageSet`](https://reference.aspose.com/words/cpp/aspose.words.saving/pageset/), [`get_PageCount`](https://reference.aspose.com/words/cpp/aspose.words/document/get_pagecount/).

## word-to-image-05

How to save a Word document as an image?

Origin: copilot-cli. Compilation: passed.

Use [`ImageSaveOptions`](https://reference.aspose.com/words/cpp/aspose.words.saving/imagesaveoptions/) and a zero-based [`PageSet`](https://reference.aspose.com/words/cpp/aspose.words.saving/pageset/pageset/) to save each page as a PNG:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/SaveFormat.h>
#include <Aspose.Words.Cpp/Saving/ImageSaveOptions.h>
#include <Aspose.Words.Cpp/Saving/PageSet.h>
#include <system/smart_ptr.h>

#include <cstdint>

int main()
{
    // Create a sample input document.
    auto sample = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(sample);
    builder->Writeln(u"Hello from Aspose.Words!");
    sample->Save(u"sample-input.docx");

    auto doc = System::MakeObject<Aspose::Words::Document>(u"sample-input.docx");
    auto options = System::MakeObject<Aspose::Words::Saving::ImageSaveOptions>(
        Aspose::Words::SaveFormat::Png);
    options->set_Resolution(150.0f);

    const int32_t pageCount = doc->get_PageCount();
    for (int32_t i = 0; i < pageCount; ++i)
    {
        options->set_PageSet(
            System::MakeObject<Aspose::Words::Saving::PageSet>(i));
        System::String output = System::String::Format(u"page_{0}.png", i + 1);
        doc->Save(output, options);
    }

    return 0;
}
```

The program creates `sample-input.docx` and `page_1.png` in the working directory, overwriting files with those names. To convert your own document, remove the sample-creation statements and replace the input path.

No external service is needed. Without a license, [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/) apply. The documentation service exposes latest-stable references, not a separately verifiable 26.9.0 reference.

## word-to-image-06

Can Aspose.Words convert DOCX to JPG or PNG?

Origin: copilot-cli. Compilation: passed.

Yes. Aspose.Words can render a DOCX as JPEG or PNG; this example saves **each page** to separate files in both formats. [Conversion guide](https://docs.aspose.com/words/cpp/convert-a-document-to-an-image/) · [ImageSaveOptions reference](https://reference.aspose.com/words/cpp/aspose.words.saving/imagesaveoptions/)

```cpp
#include <cstdint>

#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/SaveFormat.h>
#include <Aspose.Words.Cpp/Saving/ImageSaveOptions.h>
#include <Aspose.Words.Cpp/Saving/PageSet.h>
#include <system/smart_ptr.h>

int main()
{
    auto document = System::MakeObject<Aspose::Words::Document>(u"input.docx");

    auto pngOptions = System::MakeObject<Aspose::Words::Saving::ImageSaveOptions>(
        Aspose::Words::SaveFormat::Png);
    auto jpegOptions = System::MakeObject<Aspose::Words::Saving::ImageSaveOptions>(
        Aspose::Words::SaveFormat::Jpeg);

    for (int32_t pageIndex = 0; pageIndex < document->get_PageCount(); ++pageIndex)
    {
        auto pageSet = System::MakeObject<Aspose::Words::Saving::PageSet>(pageIndex);
        pngOptions->set_PageSet(pageSet);
        jpegOptions->set_PageSet(pageSet);

        const int32_t pageNumber = pageIndex + 1;
        document->Save(System::String(u"page_") + pageNumber + u".png", pngOptions);
        document->Save(System::String(u"page_") + pageNumber + u".jpg", jpegOptions);
    }

    return 0;
}
```

Place `input.docx` in the program’s working directory; existing output files with those names may be overwritten. Use the Aspose.Words.Cpp and CodePorting framework packages. A valid Aspose.Words license is needed for licensed use; no credentials or external services are required. The MCP documentation resolved to latest stable, so I can’t confirm the signatures specifically against 26.9.0.

## pdf-to-other-01

How to convert PDF to other document formats?

Origin: copilot-cli. Compilation: passed.

Load the PDF into a [`Document`](https://reference.aspose.com/words/cpp/aspose.words/document/document/), then [save](https://reference.aspose.com/words/cpp/aspose.words/document/save/) it with the desired output extension:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.pdf");

    doc->Save(u"output.docx");
    doc->Save(u"output.html");
    doc->Save(u"output.rtf");
    return 0;
}
```

Place an unencrypted `input.pdf` in the working directory. Existing output files are overwritten. Conversion may change layout; inspect the results. No external service is required. Without a license, evaluation limitations apply; see [licensing](https://docs.aspose.com/words/cpp/licensing/).

## pdf-to-other-02

How to convert PDF to DOCX in C++?

Origin: copilot-cli. Compilation: passed.

Load the PDF into an Aspose `Document`, then save with a `.docx` filename; `Save` infers the output format from the extension. The conversion API follows this load-then-save pattern. ([conversion guide](https://docs.aspose.com/words/cpp/convert-a-document/), [Document constructor](https://reference.aspose.com/words/cpp/aspose.words/document/), [Save](https://reference.aspose.com/words/cpp/aspose.words/document/save/))

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    auto document = System::MakeObject<Aspose::Words::Document>(u"input.pdf");
    document->Save(u"output.docx");
    return 0;
}
```

Place `input.pdf` in the program’s working directory; `output.docx` is written there. The code needs no credentials or external service. For production, apply a valid Aspose.Words license before using the library; the trial version adds an evaluation watermark and imposes document-size limits ([licensing](https://docs.aspose.com/words/cpp/licensing/)). The configured MCP exposed `latest-stable`, not a separate 26.9.0 documentation snapshot.

## pdf-to-other-03

How to convert a PDF document to Word in C++?

Origin: copilot-cli. Compilation: passed.

Load the PDF into an Aspose.Words `Document`, then save it with a `.docx` filename:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    auto document = System::MakeObject<Aspose::Words::Document>(u"input.pdf");
    document->Save(u"output.docx");
    return 0;
}
```

Place `input.pdf` in the program’s working directory; the program writes `output.docx` there. Aspose.Words documents conversion as loading a supported format and saving to the desired format; its `Document` constructor detects the input format, and `Save` infers the output format from the filename. [Supported formats](https://docs.aspose.com/words/cpp/supported-document-formats/) · [Document constructor](https://reference.aspose.com/words/cpp/aspose.words/document/document/) · [Document.Save](https://reference.aspose.com/words/cpp/aspose.words/document/save/)

The program needs the Aspose.Words for C++ and CodePorting framework packages. No credentials or external service are required. A purchased license file is needed for licensed use; the trial works with an evaluation watermark and document-size limits. [Licensing](https://docs.aspose.com/words/cpp/licensing/)

**Version note:** The MCP API evidence resolved to `latest-stable`, not a version-specific 26.9.0 snapshot.

## pdf-to-other-04

How do I convert PDF to DOC or DOCX using Aspose.Words?

Origin: copilot-cli. Compilation: passed.

Load the PDF into a `Document`, then save it with the desired filename extension; `Save(filename)` selects the output format from that extension.[1][2]

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    System::SharedPtr<Aspose::Words::Document> document =
        System::MakeObject<Aspose::Words::Document>(u"input.pdf");

    document->Save(u"output.docx");
    document->Save(u"output.doc");

    return 0;
}
```

Place `input.pdf` in the program’s working directory; the outputs are written there too. Use an applicable Aspose license for licensed use; no credentials or external service are needed for this local conversion.[3] The MCP reference available to me resolved to `latest-stable`, not a 26.9.0-specific snapshot.

[1] [Document conversion](https://docs.aspose.com/words/cpp/convert-a-document/) · [2] [Document constructor](https://reference.aspose.com/words/cpp/aspose.words/document/document/) and [Save](https://reference.aspose.com/words/cpp/aspose.words/document/save/) · [3] [Licensing](https://docs.aspose.com/words/cpp/licensing/)

## pdf-to-other-05

How to convert PDF to HTML or an image in C++?

Origin: copilot-cli. Compilation: passed.

Load the PDF with `Document`, then save it as HTML or render each page as PNG. See [PDF loading](https://reference.aspose.com/words/cpp/aspose.words.loading/pdfloadoptions/) and [image conversion](https://docs.aspose.com/words/cpp/convert-a-document-to-an-image/).

```cpp
#include <cstdint>
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/SaveFormat.h>
#include <Aspose.Words.Cpp/Saving/ImageSaveOptions.h>
#include <Aspose.Words.Cpp/Saving/PageSet.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.pdf");

    doc->Save(u"output.html");

    auto options = System::MakeObject<Aspose::Words::Saving::ImageSaveOptions>(
        Aspose::Words::SaveFormat::Png);
    options->set_Resolution(150.0f);

    const int32_t pageCount = doc->get_PageCount();
    for (int32_t i = 0; i < pageCount; ++i)
    {
        options->set_PageSet(
            System::MakeObject<Aspose::Words::Saving::PageSet>(i));
        doc->Save(System::String::Format(u"page_{0}.png", i + 1), options);
    }

    return 0;
}
```

Place `input.pdf` in the working directory. Outputs overwrite matching files; HTML may also produce supporting files. No external service is required. The unlicensed [evaluation version](https://docs.aspose.com/words/cpp/licensing/) adds a watermark and limits document size. Conversion may alter layout or substitute missing fonts.

The documentation endpoint provides latest-stable API evidence, not a separately verified 26.9.0 reference.

## pdf-to-other-06

Can Aspose.Words convert PDF to other formats?

Origin: copilot-cli. Compilation: no_code.

Yes. Aspose.Words for C++ can load a PDF into a `Document` and save it in another supported format. For example, you can convert it to DOCX, HTML, or an image format. The exact options depend on the supported input and output formats. [PDF load options](https://reference.aspose.com/words/cpp/aspose.words.loading/pdfloadoptions/) · [Conversion workflow](https://docs.aspose.com/words/cpp/convert-a-document/) · [Supported formats](https://docs.aspose.com/words/cpp/supported-document-formats/)

## pdf-to-other-07

How to load a PDF document with PdfLoadOptions?

Origin: copilot-cli. Compilation: no_code.

Create a [`PdfLoadOptions`](https://reference.aspose.com/words/cpp/aspose.words.loading/pdfloadoptions/), set `PageIndex` and `PageCount` if needed, then pass it to the [`Document` constructor](https://reference.aspose.com/words/cpp/aspose.words/document/document/). Page indexes are zero-based; by default, all pages are read.

A standalone program remains **unverified**: the documentation lookup did not identify the `PdfLoadOptions` header, and access to the installed SDK headers was denied. The supplied `examples\error-correction.md` was also unavailable in the workspace.

## mail-merge-01

What is Mail Merge in Aspose.Words?

Origin: copilot-cli. Compilation: no_code.

**Mail Merge** combines a document template with data to generate personalized documents, such as letters, invoices or labels. Merge fields in the template are replaced with values from a data source—for example, a recipient’s name. [Aspose.Words overview](https://docs.aspose.com/words/cpp/mail-merge-and-reporting/)

A **simple merge** repeats the whole document for each record; a **merge with regions** repeats only designated sections, such as an invoice’s line items. [Types of mail merge](https://docs.aspose.com/words/cpp/types-of-mail-merge-operations/)

## mail-merge-02

How to perform mail merge in C++?

Origin: copilot-cli. Compilation: passed.

This example creates a template with two merge fields, supplies one record, and saves the merged document. `Execute(fieldNames, values)` performs a single-record merge; the names must match the template’s `MERGEFIELD` names. [Simple Mail Merge guide](https://docs.aspose.com/words/cpp/simple-mail-merge-operation/) · [Execute API](https://reference.aspose.com/words/cpp/aspose.words.mailmerging/mailmerge/execute/)

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/MailMerging/MailMerge.h>
#include <system/array.h>
#include <system/object.h>
#include <system/smart_ptr.h>

int main()
{
    System::SharedPtr<Aspose::Words::Document> doc =
        System::MakeObject<Aspose::Words::Document>();
    System::SharedPtr<Aspose::Words::DocumentBuilder> builder =
        System::MakeObject<Aspose::Words::DocumentBuilder>(doc);

    builder->Write(u"Dear ");
    builder->InsertField(u" MERGEFIELD FirstName ");
    builder->Write(u", welcome to ");
    builder->InsertField(u" MERGEFIELD City ");
    builder->Write(u".");

    System::ArrayPtr<System::String> fieldNames =
        System::MakeArray<System::String>({u"FirstName", u"City"});

    System::ArrayPtr<System::SharedPtr<System::Object>> values =
        System::MakeArray<System::SharedPtr<System::Object>>({
            System::ExplicitCast<System::Object>(System::String(u"Ada")),
            System::ExplicitCast<System::Object>(System::String(u"London"))
        });

    doc->get_MailMerge()->Execute(fieldNames, values);
    doc->Save(u"mail-merge-result.docx");

    return 0;
}
```

The example needs no input document or external service. For production use, apply a valid license before creating Aspose.Words objects; without one, evaluation limitations apply. [Licensing guide](https://docs.aspose.com/words/cpp/licensing/). The configured MCP reference only exposed **latest-stable**, not 26.9.0, so that exact SDK version could not be independently confirmed.

## mail-merge-03

How to populate a Word template with data using Mail Merge?

Origin: copilot-cli. Compilation: passed.

Use [MailMerge::Execute](https://reference.aspose.com/words/cpp/aspose.words.mailmerging/mailmerge/execute/) with matching field names and values. This example creates a template, reloads it, and merges one record:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/MailMerging/MailMerge.h>
#include <system/array.h>
#include <system/object.h>
#include <system/smart_ptr.h>

int main()
{
    auto sample = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(sample);
    builder->Write(u"Dear ");
    builder->InsertField(u"MERGEFIELD CustomerName");
    builder->Write(u", thank you for ordering ");
    builder->InsertField(u"MERGEFIELD Item");
    builder->Write(u".");

    sample->Save(u"sample-template.docx");

    auto doc = System::MakeObject<Aspose::Words::Document>(
        System::String(u"sample-template.docx"));

    auto names = System::MakeArray<System::String>(
        {u"CustomerName", u"Item"});
    auto values = System::MakeArray<System::SharedPtr<System::Object>>(
        {System::ExplicitCast<System::Object>(System::String(u"Ada Lovelace")),
         System::ExplicitCast<System::Object>(System::String(u"a notebook"))});

    doc->get_MailMerge()->Execute(names, values);
    doc->Save(u"merged.docx");
    return 0;
}
```

The arrays must have equal lengths; field names are case-insensitive. For your own template, load its DOCX instead of creating the sample. Both output files are overwritten if present. No external service is needed; an [Aspose license](https://docs.aspose.com/words/cpp/licensing/) removes evaluation limitations.

The API documentation checked was current; version-specific documentation for 26.9.0 was unavailable.

## mail-merge-04

How to generate personalized documents from a template?

Origin: copilot-cli. Compilation: passed.

Use [mail merge](https://docs.aspose.com/words/cpp/simple-mail-merge-operation/) to fill `MERGEFIELD` placeholders. This example creates a template, then reloads it for each recipient so each gets a separate document. The [`Execute`](https://reference.aspose.com/words/cpp/aspose.words.mailmerging/mailmerge/execute/) arrays must have matching lengths.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/MailMerging/MailMerge.h>
#include <system/array.h>
#include <system/object.h>
#include <system/smart_ptr.h>

struct Recipient
{
    const char16_t* name;
    const char16_t* company;
    const char16_t* output;
};

int main()
{
    auto templateDoc = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(templateDoc);

    builder->Write(u"Dear ");
    builder->InsertField(u"MERGEFIELD Name");
    builder->Write(u",\n\nWelcome to ");
    builder->InsertField(u"MERGEFIELD Company");
    builder->Write(u"!");

    templateDoc->Save(u"template.docx");

    const Recipient recipients[] = {
        {u"Alice", u"Contoso", u"alice.docx"},
        {u"Bob", u"Fabrikam", u"bob.docx"}
    };

    for (const auto& recipient : recipients)
    {
        auto doc = System::MakeObject<Aspose::Words::Document>(
            System::String(u"template.docx"));

        auto names = System::MakeArray<System::String>({u"Name", u"Company"});
        auto values = System::MakeArray<System::SharedPtr<System::Object>>({
            System::ObjectExt::Box<System::String>(recipient.name),
            System::ObjectExt::Box<System::String>(recipient.company)
        });

        doc->get_MailMerge()->Execute(names, values);
        doc->Save(recipient.output);
    }

    return 0;
}
```

The program needs no input files or external services. It writes `template.docx`, `alice.docx`, and `bob.docx` in the working directory, overwriting existing files. For an existing template, omit its creation and load your DOCX instead. An Aspose license removes evaluation limitations; see [licensing](https://docs.aspose.com/words/cpp/licensing/).

## mail-merge-05

How to perform mail merge with a data source in C++?

Origin: copilot-cli. Compilation: passed.

Use [`MailMerge::Execute`](https://reference.aspose.com/words/cpp/aspose.words.mailmerging/mailmerge/execute/) with matching field-name and value arrays for one record:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/MailMerging/MailMerge.h>
#include <system/array.h>
#include <system/object.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(doc);

    builder->Write(u"Dear ");
    builder->InsertField(u"MERGEFIELD Name");
    builder->Writeln(u",");
    builder->Write(u"Welcome to ");
    builder->InsertField(u"MERGEFIELD Company");
    builder->Writeln(u".");

    doc->Save(u"template.docx");

    auto names = System::MakeArray<System::String>({u"Name", u"Company"});
    auto values = System::MakeArray<System::SharedPtr<System::Object>>({
        System::ExplicitCast<System::Object>(System::String(u"Ada")),
        System::ExplicitCast<System::Object>(System::String(u"Example Corp"))
    });

    doc->get_MailMerge()->Execute(names, values);
    doc->Save(u"merged.docx");
    return 0;
}
```

The program creates its own template and data; both output files are overwritten if present. For multiple records or database results, implement [`IMailMergeDataSource`](https://reference.aspose.com/words/cpp/aspose.words.mailmerging/imailmergedatasource/). Without a license, [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/) apply.

The documentation endpoint returned latest-stable evidence rather than a version-specific 26.9.0 reference. The requested guidance file was not present locally; its supplied contents were used.

## mail-merge-06

How to use mail merge fields in a Word document?

Origin: copilot-cli. Compilation: passed.

Insert `MERGEFIELD` fields, then call [`MailMerge::Execute`](https://reference.aspose.com/words/cpp/aspose.words.mailmerging/mailmerge/execute/) with matching names and values. This example creates its own [template](https://docs.aspose.com/words/cpp/mail-merge-template/) and merges one record:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/MailMerging/MailMerge.h>
#include <system/array.h>
#include <system/object.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(doc);

    builder->Write(u"Dear ");
    builder->InsertField(u"MERGEFIELD FirstName");
    builder->Write(u", welcome to ");
    builder->InsertField(u"MERGEFIELD Company");
    builder->Write(u"!");

    doc->Save(u"template.docx");

    auto names = System::MakeArray<System::String>(
        {u"FirstName", u"Company"});
    auto values = System::MakeArray<System::SharedPtr<System::Object>>(
        {System::ObjectExt::Box<System::String>(u"Ada"),
         System::ObjectExt::Box<System::String>(u"Example Ltd")});

    doc->get_MailMerge()->Execute(names, values);
    doc->Save(u"merged.docx");
    return 0;
}
```

The files are written in the working directory and overwrite existing files with those names. No input file or external service is needed. The [trial](https://docs.aspose.com/words/cpp/licensing/) adds an evaluation watermark; apply a license before document processing to remove trial limitations.

The documentation service exposes only `latest-stable`, so its evidence could not be pinned specifically to 26.9.0. The requested guidance file was unavailable; the rules included in your prompt were used instead.

## mail-merge-07

How to execute mail merge with regions in Aspose.Words?

Origin: copilot-cli. Compilation: no_code.

Use [`ExecuteWithRegions`](https://reference.aspose.com/words/cpp/aspose.words.mailmerging/mailmerge/executewithregions/) with a custom [`IMailMergeDataSource`](https://reference.aspose.com/words/cpp/aspose.words.mailmerging/imailmergedatasource/). In the template, bracket the repeating content with merge fields named `TableStart:Orders` and `TableEnd:Orders`; the data source’s table name must match. The content is repeated for each record. See the [mail merge regions guide](https://docs.aspose.com/words/cpp/mail-merge-with-regions/).

I cannot provide the requested verified standalone program: the documentation lookup did not expose the interface’s header path, and access to the local SDK headers was denied. The available documentation was for latest stable, not independently verified against 26.9.0.

## mail-merge-08

What is the difference between Mail Merge and LINQ Reporting Engine?

Origin: copilot-cli. Compilation: no_code.

**Mail Merge** fills Word merge fields with data, typically for personalized letters or invoices. It also supports repeating regions, images, and custom logic through callbacks. [Aspose.Words for C++ guide](https://docs.aspose.com/words/cpp/mail-merge-and-reporting/)

**LINQ Reporting Engine** is conceptually more expression-oriented: templates describe calculations and report structure, making it suited to more complex, data-driven reports.

**C++ caveat:** I could not verify LINQ Reporting Engine availability or its detailed capabilities in Aspose.Words for C++ 26.9.0 from the configured documentation. The [features page](https://docs.aspose.com/words/cpp/features/) lists a reporting limitation, but its wording conflicts with the Mail Merge reporting guide, so it is not conclusive about that specific engine.

## compare-01

How to compare two Word documents in C++?

Origin: copilot-cli. Compilation: passed.

[`Document::Compare`](https://reference.aspose.com/words/cpp/aspose.words/document/compare/) adds differences as revisions to the original document. Neither input may already contain revisions.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/RevisionCollection.h>
#include <system/smart_ptr.h>
#include <iostream>

int main()
{
    using Aspose::Words::Document;
    using Aspose::Words::DocumentBuilder;

    auto original = System::MakeObject<Document>();
    auto originalBuilder = System::MakeObject<DocumentBuilder>(original);
    originalBuilder->Writeln(u"The meeting is on Monday.");

    auto edited = System::MakeObject<Document>();
    auto editedBuilder = System::MakeObject<DocumentBuilder>(edited);
    editedBuilder->Writeln(u"The meeting is on Tuesday.");

    original->Save(u"original.docx");
    edited->Save(u"edited.docx");

    if (original->get_Revisions()->get_Count() != 0 ||
        edited->get_Revisions()->get_Count() != 0)
    {
        std::cerr << "Both documents must be free of revisions.\n";
        return 1;
    }

    original->Compare(edited, u"Reviewer", System::DateTime::get_Now());

    std::cout << "Revisions: " << original->get_Revisions()->get_Count() << '\n';
    original->Save(u"comparison.docx");
    return 0;
}
```

The program creates sample inputs and `comparison.docx` in the working directory, overwriting files with those names. For existing files, construct each `Document` with its filename instead. A zero revision count means no differences were represented by the comparison, not necessarily byte-identical files. See the [comparison guide](https://docs.aspose.com/words/cpp/compare-documents/).

No external service is needed. An unlicensed installation has [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/). The available documentation is latest-stable; the 26.9.0 headers were not independently inspected.

## compare-02

How to find differences between DOCX documents using Aspose.Words?

Origin: copilot-cli. Compilation: passed.

Use [`Document::Compare`](https://reference.aspose.com/words/cpp/aspose.words/document/compare/) to record differences as revisions in the original document. Neither input may already contain revisions.

This example creates two sample DOCX files, compares them, and saves the tracked changes in `comparison.docx`. It overwrites all three files if they exist.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/RevisionCollection.h>
#include <system/smart_ptr.h>
#include <iostream>

int main()
{
    using Aspose::Words::Document;
    using Aspose::Words::DocumentBuilder;

    auto originalSample = System::MakeObject<Document>();
    auto originalBuilder = System::MakeObject<DocumentBuilder>(originalSample);
    originalBuilder->Writeln(u"The meeting is on Monday.");
    originalSample->Save(u"original.docx");

    auto editedSample = System::MakeObject<Document>();
    auto editedBuilder = System::MakeObject<DocumentBuilder>(editedSample);
    editedBuilder->Writeln(u"The meeting is on Tuesday.");
    editedSample->Save(u"edited.docx");

    auto original = System::MakeObject<Document>(System::String(u"original.docx"));
    auto edited = System::MakeObject<Document>(System::String(u"edited.docx"));

    if (original->get_Revisions()->get_Count() != 0 ||
        edited->get_Revisions()->get_Count() != 0)
    {
        std::cerr << "Both documents must be free of revisions before comparison.\n";
        return 1;
    }

    original->Compare(edited, u"Comparison", System::DateTime::get_Now());

    std::cout << "Revisions found: "
              << original->get_Revisions()->get_Count() << '\n';

    original->Save(u"comparison.docx");
    return 0;
}
```

For existing files, replace the sample-creation section and paths. A zero revision count means no differences were represented by the comparison, not necessarily byte-identical files. See the [comparison guide](https://docs.aspose.com/words/cpp/compare-documents/).

The example needs no external service. An unlicensed [trial](https://docs.aspose.com/words/cpp/licensing/) adds evaluation watermarks and has document-size limits. The documentation service returned latest-stable API evidence, not a separately verified 26.9.0 reference; `examples\error-correction.md` was unavailable in the workspace.

## compare-03

How to compare two documents and identify changes?

Origin: copilot-cli. Compilation: passed.

Use [`Document::Compare`](https://reference.aspose.com/words/cpp/aspose.words/document/compare/) to add tracked changes to the original document, then inspect the saved DOCX in Word. Both documents must have no existing revisions.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/RevisionCollection.h>
#include <system/smart_ptr.h>
#include <iostream>

int main()
{
    using Aspose::Words::Document;
    using Aspose::Words::DocumentBuilder;

    auto original = System::MakeObject<Document>();
    auto originalBuilder = System::MakeObject<DocumentBuilder>(original);
    originalBuilder->Writeln(u"The meeting is on Monday.");

    auto edited = System::MakeObject<Document>();
    auto editedBuilder = System::MakeObject<DocumentBuilder>(edited);
    editedBuilder->Writeln(u"The meeting is on Tuesday.");

    if (original->get_Revisions()->get_Count() != 0 ||
        edited->get_Revisions()->get_Count() != 0)
    {
        std::cerr << "Both documents must have no existing revisions.\n";
        return 1;
    }

    original->Compare(edited, u"Reviewer", System::DateTime::get_Now());

    std::cout << "Revisions: " << original->get_Revisions()->get_Count()
              << "\nOpen comparison.docx and show tracked changes to inspect them.\n";
    original->Save(u"comparison.docx");
    return 0;
}
```

The example creates both inputs in memory; `comparison.docx` is overwritten if it exists. For real files, load each using the [`Document` filename constructor](https://reference.aspose.com/words/cpp/aspose.words/document/document/). A license removes [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/); no external service is required.

**Version caveat:** the MCP reference supplied only `latest-stable`, not version-specific 26.9.0 evidence.

## compare-04

How to generate a document that shows differences between two versions?

Origin: copilot-cli. Compilation: passed.

Use [`Document::Compare`](https://reference.aspose.com/words/cpp/aspose.words/document/compare/) to add differences as tracked revisions to the original document, then save it as DOCX.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/RevisionCollection.h>
#include <system/smart_ptr.h>
#include <iostream>

int main()
{
    using Aspose::Words::Document;
    using Aspose::Words::DocumentBuilder;

    auto original = System::MakeObject<Document>();
    auto originalBuilder = System::MakeObject<DocumentBuilder>(original);
    originalBuilder->Writeln(u"The delivery date is Monday.");
    original->Save(u"original.docx");

    auto edited = System::MakeObject<Document>();
    auto editedBuilder = System::MakeObject<DocumentBuilder>(edited);
    editedBuilder->Writeln(u"The delivery date is Friday.");
    edited->Save(u"edited.docx");

    original->Compare(edited, u"Reviewer", System::DateTime::get_Now());
    std::cout << "Revisions: " << original->get_Revisions()->get_Count() << '\n';
    original->Save(u"differences.docx");

    return 0;
}
```

The program creates both sample inputs and `differences.docx` in the working directory, overwriting files with those names. Open the result with revision markup displayed. For existing files, load them with `Document` constructors instead; **neither input may contain revisions** before comparison. See the [comparison guide](https://docs.aspose.com/words/cpp/compare-documents/).

No external service is needed. An unlicensed [evaluation version](https://docs.aspose.com/words/cpp/licensing/) adds a watermark and limits document size.

## compare-05

How to compare Word documents programmatically?

Origin: copilot-cli. Compilation: passed.

Use [`Document::Compare`](https://reference.aspose.com/words/cpp/aspose.words/document/compare/) to add tracked differences to the original document, then save it for review:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/RevisionCollection.h>
#include <system/smart_ptr.h>
#include <iostream>

int main()
{
    auto original = System::MakeObject<Aspose::Words::Document>();
    auto originalBuilder = System::MakeObject<Aspose::Words::DocumentBuilder>(original);
    originalBuilder->Writeln(u"The meeting is on Monday.");

    auto edited = System::MakeObject<Aspose::Words::Document>();
    auto editedBuilder = System::MakeObject<Aspose::Words::DocumentBuilder>(edited);
    editedBuilder->Writeln(u"The meeting is on Tuesday.");

    if (original->get_Revisions()->get_Count() != 0 ||
        edited->get_Revisions()->get_Count() != 0)
    {
        std::cerr << "Both documents must be free of revisions before comparison.\n";
        return 1;
    }

    original->Compare(edited, u"Comparison", System::DateTime::get_Now());
    std::cout << "Revisions: " << original->get_Revisions()->get_Count() << '\n';
    original->Save(u"comparison.docx");
    return 0;
}
```

The example creates both inputs in memory. For existing files, construct each `Document` with its path instead. Both inputs must have no existing revisions; the output `comparison.docx` is overwritten if it exists. See the [comparison guide](https://docs.aspose.com/words/cpp/compare-documents/) and [Save](https://reference.aspose.com/words/cpp/aspose.words/document/save/).

A license removes [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/); no external service is needed. The documentation service supplied latest-stable evidence but did not confirm the pinned 26.9.0 version; the requested `examples\error-correction.md` file was not present.

## compare-06

Can Aspose.Words compare documents and mark revisions?

Origin: copilot-cli. Compilation: no_code.

Yes. `Document::Compare` compares two documents and records detected text and formatting differences as revisions in the document you call it on. Supply the other document, revision author, and date/time; an overload also accepts comparison options. **Neither document may already contain revisions** when you compare them. [API reference](https://reference.aspose.com/words/cpp/aspose.words/document/compare/) · [Compare Documents guide](https://docs.aspose.com/words/cpp/compare-documents/)

The MCP documentation lookup resolved to **latest-stable**, not a version-specific 26.9.0 reference.

## compare-07

How to compare documents while ignoring formatting changes?

Origin: copilot-cli. Compilation: passed.

Set [`IgnoreFormatting`](https://reference.aspose.com/words/cpp/aspose.words.comparing/compareoptions/get_ignoreformatting/) to `true`, then call [`Compare`](https://reference.aspose.com/words/cpp/aspose.words/document/compare/). Differences appear as revisions in the first document; neither input may already contain revisions.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/Font.h>
#include <Aspose.Words.Cpp/RevisionCollection.h>
#include <Aspose.Words.Cpp/Comparing/CompareOptions.h>
#include <system/date_time.h>
#include <system/smart_ptr.h>
#include <iostream>

int main()
{
    using namespace Aspose::Words;

    auto original = System::MakeObject<Document>();
    auto originalBuilder = System::MakeObject<DocumentBuilder>(original);
    originalBuilder->Writeln(u"The meeting is on Monday.");

    auto edited = System::MakeObject<Document>();
    auto editedBuilder = System::MakeObject<DocumentBuilder>(edited);
    editedBuilder->get_Font()->set_Bold(true);
    editedBuilder->Writeln(u"The meeting is on Tuesday.");

    auto options = System::MakeObject<Comparing::CompareOptions>();
    options->set_IgnoreFormatting(true);

    original->Compare(edited, u"Reviewer", System::DateTime::get_Now(), options);

    std::cout << "Revisions excluding formatting: "
              << original->get_Revisions()->get_Count() << '\n';
    original->Save(u"comparison.docx");
    return 0;
}
```

The example creates inputs in memory and overwrites `comparison.docx` in the working directory. No external service is needed; an Aspose license removes [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/).

**Verification gap:** MCP returned latest-stable API documentation but did not expose the `CompareOptions` or `date_time` header paths, and local SDK access was denied. Those paths and compatibility with 26.9.0 remain unverified.

## split-01

How to split a Word document into multiple documents in C++?

Origin: copilot-cli. Compilation: passed.

Use [`ExtractPages`](https://reference.aspose.com/words/cpp/aspose.words/document/extractpages/) to save each page as a separate document. Page indexes are zero-based.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <system/smart_ptr.h>
#include <cstdint>

int main()
{
    using namespace Aspose::Words;

    // Set to false to split an existing input.docx instead.
    const bool createSample = true;
    const System::String inputPath = createSample
        ? System::String(u"sample-input.docx")
        : System::String(u"input.docx");

    if (createSample)
    {
        auto sample = System::MakeObject<Document>();
        auto builder = System::MakeObject<DocumentBuilder>(sample);
        builder->Write(u"Sample page 1.\fSample page 2.");
        sample->Save(inputPath);
    }

    auto doc = System::MakeObject<Document>(inputPath);
    const int32_t pageCount = doc->get_PageCount();

    for (int32_t page = 0; page < pageCount; ++page)
    {
        auto part = doc->ExtractPages(page, 1);
        part->Save(System::String::Format(u"page-{0}.docx", page + 1));
    }

    return 0;
}
```

The example creates a sample input by default; set `createSample` to `false` to use `input.docx`. It overwrites existing files with the same output names. A license avoids evaluation limitations; no external service is required. Layout may differ slightly for complex documents ([splitting guide](https://docs.aspose.com/words/cpp/split-a-document/), [licensing guidance](https://docs.aspose.com/words/cpp/insert-checkboxes-text-input-or-images-mail-merge/)).

The requested guidance file was unavailable locally; the included error-correction guidance was used. The documentation service returned latest-stable evidence rather than independently confirming version 26.9.0.

## split-02

How to split a DOCX file by pages using Aspose.Words?

Origin: copilot-cli. Compilation: passed.

Use [`ExtractPages`](https://reference.aspose.com/words/cpp/aspose.words/document/extractpages/) with a zero-based page index and a count of one.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>
#include <cstdint>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    const int32_t pageCount = doc->get_PageCount();

    for (int32_t page = 0; page < pageCount; ++page)
    {
        auto extracted = doc->ExtractPages(page, 1);
        extracted->Save(System::String::Format(u"page_{0}.docx", page + 1));
    }

    return 0;
}
```

Place `input.docx` in the working directory. Output files there are overwritten if they already exist. Evaluation mode may add watermarks or limit functionality; no external service is required. Complex documents may have layout differences after extraction ([splitting guide](https://docs.aspose.com/words/cpp/split-a-document/)).

The documentation endpoint resolved to latest-stable; version 26.9.0 was not separately verified.

## split-03

How to extract each page of a Word document into a separate file?

Origin: copilot-cli. Compilation: passed.

Use [`ExtractPages(index, 1)`](https://reference.aspose.com/words/cpp/aspose.words/document/extractpages/) for each zero-based page, then save each result as DOCX.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <system/smart_ptr.h>

#include <cstring>
#include <iostream>

int main(int argc, char* argv[])
{
    System::SharedPtr<Aspose::Words::Document> doc;

    if (argc == 2 && std::strcmp(argv[1], "--sample") == 0)
    {
        doc = System::MakeObject<Aspose::Words::Document>();
        auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(doc);
        for (int i = 0; i < 120; ++i)
            builder->Writeln(u"Sample paragraph for page extraction.");
        doc->Save(u"sample-input.docx");
    }
    else if (argc == 1)
    {
        doc = System::MakeObject<Aspose::Words::Document>(
            System::String(u"input.docx"));
    }
    else
    {
        std::cerr << "Usage: program [--sample]\n";
        return 1;
    }

    const int pageCount = doc->get_PageCount();
    for (int page = 0; page < pageCount; ++page)
    {
        auto extracted = doc->ExtractPages(page, 1);
        extracted->Save(System::String::Format(u"page-{0}.docx", page + 1));
    }

    return 0;
}
```

Place `input.docx` in the working directory, or use `--sample` to create and split `sample-input.docx`. Existing output files are overwritten. Complex documents may have slight layout differences after splitting ([guide](https://docs.aspose.com/words/cpp/split-a-document/)).

No license is applied here; evaluation adds a watermark and limits document size ([licensing](https://docs.aspose.com/words/cpp/licensing/)). No external service is required. The documentation endpoint returned latest-stable evidence rather than version-specific confirmation for 26.9.0. The requested guidance file was absent; the inline guidance was used.

## split-04

How to split a Word document by sections?

Origin: copilot-cli. Compilation: passed.

Load the document, then [clone it](https://reference.aspose.com/words/cpp/aspose.words/document/clone/) once per section and remove the other sections:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/SectionCollection.h>
#include <system/smart_ptr.h>

int main()
{
    auto source = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    const int count = source->get_Sections()->get_Count();

    for (int i = 0; i < count; ++i)
    {
        auto part = source->Clone();
        auto sections = part->get_Sections();

        for (int j = count - 1; j >= 0; --j)
        {
            if (j != i)
                sections->RemoveAt(j);
        }

        part->Save(System::String::Format(u"section_{0}.docx", i + 1));
    }

    return 0;
}
```

Place `input.docx` in the working directory. Outputs such as `section_1.docx` are overwritten if they exist. A license is needed to avoid evaluation limitations; no external service is required.

[Linked headers and footers](https://reference.aspose.com/words/cpp/aspose.words/headerfootercollection/linktoprevious/) may depend on a removed section. Check those, cross-section fields, and pagination in the outputs.

## split-05

How to split a document by headings or other structural elements?

Origin: copilot-cli. Compilation: passed.

Use `DocumentSplitCriteria::HeadingParagraph` to save separate HTML files at headings; set the maximum heading level to control where splits occur. [Heading-level documentation](https://reference.aspose.com/words/cpp/aspose.words.saving/htmlsaveoptions/get_documentsplitheadinglevel/).

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/ParagraphFormat.h>
#include <Aspose.Words.Cpp/Saving/DocumentSplitCriteria.h>
#include <Aspose.Words.Cpp/Saving/HtmlSaveOptions.h>
#include <system/smart_ptr.h>

int main()
{
    using namespace Aspose::Words;
    using namespace Aspose::Words::Saving;

    auto doc = System::MakeObject<Document>();
    auto builder = System::MakeObject<DocumentBuilder>(doc);

    builder->get_ParagraphFormat()->set_StyleName(u"Heading 1");
    builder->Writeln(u"First chapter");
    builder->get_ParagraphFormat()->set_StyleName(u"Normal");
    builder->Writeln(u"First chapter content.");

    builder->get_ParagraphFormat()->set_StyleName(u"Heading 1");
    builder->Writeln(u"Second chapter");
    builder->get_ParagraphFormat()->set_StyleName(u"Normal");
    builder->Writeln(u"Second chapter content.");

    auto options = System::MakeObject<HtmlSaveOptions>();
    options->set_DocumentSplitCriteria(DocumentSplitCriteria::HeadingParagraph);
    options->set_DocumentSplitHeadingLevel(1);
    doc->Save(u"chapters.html", options);
    return 0;
}
```

The sample creates its input in memory and writes HTML files in the current directory, overwriting matching output names. For an existing document, construct `Document` with its path instead. A license avoids [evaluation restrictions](https://docs.aspose.com/words/cpp/faq/); no external service is needed.

For section, page, or column breaks, choose another [split criterion](https://docs.aspose.com/words/cpp/split-a-document/). For separate DOCX files, import sections into new documents, or extract content between selected nodes using the [documented extraction approach](https://docs.aspose.com/words/cpp/how-to-extract-selected-content-between-nodes-in-a-document/).

**Verification gap:** MCP confirmed the APIs, but did not expose the 26.9.0 header paths, and local shell access was denied. The additional header paths above remain unverified.

## split-06

How to save each page of a Word document separately?

Origin: copilot-cli. Compilation: passed.

Use [`ExtractPages(index, 1)`](https://reference.aspose.com/words/cpp/aspose.words/document/extractpages/) for each zero-based page, then [save](https://reference.aspose.com/words/cpp/aspose.words/document/save/) each result as DOCX.

This example creates a two-page sample. To process your document, set `createSample` to `false` and supply `input.docx` in the working directory.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <system/smart_ptr.h>
#include <cstdint>

int main()
{
    const bool createSample = true;
    System::SharedPtr<Aspose::Words::Document> doc;

    if (createSample)
    {
        doc = System::MakeObject<Aspose::Words::Document>();
        auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(doc);
        builder->Write(u"First page.\fSecond page.");
        doc->Save(u"sample-input.docx");
    }
    else
    {
        doc = System::MakeObject<Aspose::Words::Document>(
            System::String(u"input.docx"));
    }

    const int32_t pageCount = doc->get_PageCount();
    for (int32_t i = 0; i < pageCount; ++i)
    {
        auto page = doc->ExtractPages(i, 1);
        page->Save(System::String::Format(u"page-{0}.docx", i + 1));
    }

    return 0;
}
```

The sample and `page-N.docx` files are written in the working directory and overwrite existing files with those names. The example uses evaluation mode; apply an Aspose license to remove [evaluation limitations](https://docs.aspose.com/words/cpp/installation/).

## split-07

How to use DocumentSplitCriteria in Aspose.Words?

Origin: copilot-cli. Compilation: passed.

Set [`HtmlSaveOptions::DocumentSplitCriteria`](https://reference.aspose.com/words/cpp/aspose.words.saving/htmlsaveoptions/get_documentsplitcriteria/) before saving. This example creates a document and splits HTML at Heading 1 paragraphs:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/Saving/DocumentSplitCriteria.h>
#include <Aspose.Words.Cpp/Saving/HtmlSaveOptions.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(doc);

    builder->InsertHtml(
        u"<h1>Chapter One</h1><p>First chapter.</p>"
        u"<h1>Chapter Two</h1><p>Second chapter.</p>");

    auto options = System::MakeObject<Aspose::Words::Saving::HtmlSaveOptions>();
    options->set_DocumentSplitCriteria(
        Aspose::Words::Saving::DocumentSplitCriteria::HeadingParagraph);
    options->set_DocumentSplitHeadingLevel(1);
    doc->Save(u"chapters.html", options);
    return 0;
}
```

The output is multiple HTML files in the working directory; existing output files may be overwritten. EPUB instead contains the parts in one package; MHTML cannot be split this way. Other criteria include section, column, and page breaks. See [splitting documents](https://docs.aspose.com/words/cpp/split-a-document/) and [heading levels](https://reference.aspose.com/words/cpp/aspose.words.saving/htmlsaveoptions/get_documentsplitheadinglevel/).

No input file or external service is needed. Without a license, [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/) apply. The MCP documentation did not expose the two saving-header paths, and local SDK inspection was unavailable, so those paths remain **unverified**.

## merge-01

How to merge multiple Word documents into one document in C++?

Origin: copilot-cli. Compilation: passed.

Use [`AppendDocument`](https://reference.aspose.com/words/cpp/aspose.words/document/appenddocument/) to append each document in order. `KeepSourceFormatting` preserves the imported content’s formatting when styles conflict; use `UseDestinationStyles` to favor the first document’s styles instead ([format modes](https://reference.aspose.com/words/cpp/aspose.words/importformatmode/)).

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/ImportFormatMode.h>
#include <system/object.h>
#include <system/smart_ptr.h>

int main()
{
    using Aspose::Words::Document;
    using Aspose::Words::DocumentBuilder;
    using Aspose::Words::ImportFormatMode;

    const char16_t* inputs[] = {
        u"merge-example-1.docx",
        u"merge-example-2.docx",
        u"merge-example-3.docx"
    };
    const char16_t* sampleText[] = {
        u"First document.",
        u"Second document.",
        u"Third document."
    };

    // Set to false and edit inputs to merge your existing documents.
    const bool createSamples = true;
    if (createSamples)
    {
        for (int i = 0; i < 3; ++i)
        {
            auto sample = System::MakeObject<Document>();
            auto builder = System::MakeObject<DocumentBuilder>(sample);
            builder->Writeln(sampleText[i]);
            sample->Save(inputs[i]);
        }
    }

    auto merged = System::MakeObject<Document>(System::String(inputs[0]));
    for (int i = 1; i < 3; ++i)
    {
        auto source = System::MakeObject<Document>(System::String(inputs[i]));
        merged->AppendDocument(source, ImportFormatMode::KeepSourceFormatting);
    }
    merged->Save(u"merged.docx");
    return 0;
}
```

The example writes three sample inputs and `merged.docx` in the working directory, **overwriting existing files with those names**. For existing documents, disable sample creation and edit the input paths. An Aspose license removes evaluation limitations; no external service is required. See [installation and licensing](https://docs.aspose.com/words/cpp/installation/).

## merge-02

How to combine DOCX files using Aspose.Words?

Origin: copilot-cli. Compilation: passed.

Use [`AppendDocument`](https://reference.aspose.com/words/cpp/aspose.words/document/appenddocument/) to add each DOCX to the first. `KeepSourceFormatting` preserves the appended document’s formatting when styles conflict; use `UseDestinationStyles` to favor the first document’s styles instead ([format modes](https://reference.aspose.com/words/cpp/aspose.words/importformatmode/)).

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/ImportFormatMode.h>
#include <system/smart_ptr.h>

int main()
{
    using Aspose::Words::Document;
    using Aspose::Words::DocumentBuilder;
    using Aspose::Words::ImportFormatMode;

    const bool createSampleInputs = true;
    const System::String firstPath = u"sample-first.docx";
    const System::String secondPath = u"sample-second.docx";

    if (createSampleInputs)
    {
        auto first = System::MakeObject<Document>();
        auto firstBuilder = System::MakeObject<DocumentBuilder>(first);
        firstBuilder->Writeln(u"Content from the first document.");
        first->Save(firstPath);

        auto second = System::MakeObject<Document>();
        auto secondBuilder = System::MakeObject<DocumentBuilder>(second);
        secondBuilder->Writeln(u"Content from the second document.");
        second->Save(secondPath);
    }

    auto combined = System::MakeObject<Document>(firstPath);
    auto source = System::MakeObject<Document>(secondPath);
    combined->AppendDocument(source, ImportFormatMode::KeepSourceFormatting);
    combined->Save(u"combined.docx");

    return 0;
}
```

The program creates two sample inputs and `combined.docx` in the working directory, **overwriting** files with those names. To combine existing files, set `createSampleInputs` to `false` and change the input paths. Repeat `AppendDocument` for more files. No external service is needed; without a license, [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/) apply.

The requested `examples\error-correction.md` was unavailable in the workspace; the supplied inline guidance was used.

## merge-03

How to append one Word document to another?

Origin: copilot-cli. Compilation: passed.

Use [`AppendDocument`](https://reference.aspose.com/words/cpp/aspose.words/document/appenddocument/) on the destination document. This example creates two sample documents in memory and preserves the source formatting:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/ImportFormatMode.h>
#include <system/smart_ptr.h>

int main()
{
    auto destination = System::MakeObject<Aspose::Words::Document>();
    auto destinationBuilder =
        System::MakeObject<Aspose::Words::DocumentBuilder>(destination);
    destinationBuilder->Writeln(u"Destination document text.");

    auto source = System::MakeObject<Aspose::Words::Document>();
    auto sourceBuilder =
        System::MakeObject<Aspose::Words::DocumentBuilder>(source);
    sourceBuilder->Writeln(u"Source document text.");

    destination->AppendDocument(
        source, Aspose::Words::ImportFormatMode::KeepSourceFormatting);
    destination->Save(u"combined.docx");
    return 0;
}
```

For existing files, construct each `Document` with its path instead of creating it empty. `combined.docx` is overwritten if it exists. [`UseDestinationStyles`](https://reference.aspose.com/words/cpp/aspose.words/importformatmode/) is an alternative for resolving matching styles.

No input files or external services are needed for this sample. An Aspose license removes evaluation limitations; see [licensing](https://docs.aspose.com/words/cpp/licensing/). The requested `examples/error-correction.md` file was not present; the supplied error-correction guidance was used.

## merge-04

How to insert the contents of one document into another?

Origin: copilot-cli. Compilation: passed.

Use [`DocumentBuilder::InsertDocument`](https://reference.aspose.com/words/cpp/aspose.words/documentbuilder/insertdocument/) to insert at the builder’s cursor. This example creates two sample documents in memory and inserts the source at the end of the destination.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/ImportFormatMode.h>
#include <system/smart_ptr.h>

int main()
{
    using namespace Aspose::Words;

    auto destination = System::MakeObject<Document>();
    auto builder = System::MakeObject<DocumentBuilder>(destination);
    builder->Writeln(u"Destination document content.");

    auto source = System::MakeObject<Document>();
    auto sourceBuilder = System::MakeObject<DocumentBuilder>(source);
    sourceBuilder->Writeln(u"Content inserted from the source document.");

    builder->MoveToDocumentEnd();
    builder->InsertDocument(source, ImportFormatMode::KeepSourceFormatting);
    destination->Save(u"combined.docx");

    return 0;
}
```

To use existing files, construct each `Document` with its filename instead. For another insertion point, move the builder first, for example with [`MoveToBookmark`](https://reference.aspose.com/words/cpp/aspose.words/documentbuilder/movetobookmark/). `KeepSourceFormatting` preserves source formatting when styles conflict; `UseDestinationStyles` uses matching destination styles instead ([format modes](https://reference.aspose.com/words/cpp/aspose.words/importformatmode/)).

`combined.docx` is written to the working directory and overwritten if it exists. No input files or external services are required. Without a license, [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/) apply.

## merge-05

How to merge Word documents while preserving formatting?

Origin: copilot-cli. Compilation: passed.

Use [`AppendDocument`](https://reference.aspose.com/words/cpp/aspose.words/document/appenddocument/) with `KeepSourceFormatting` to preserve the appended document’s appearance when styles conflict. Conflicting styles may become direct formatting rather than retained styles. See [ImportFormatMode](https://reference.aspose.com/words/cpp/aspose.words/importformatmode/).

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/Font.h>
#include <Aspose.Words.Cpp/ImportFormatMode.h>
#include <system/smart_ptr.h>

int main()
{
    using namespace Aspose::Words;

    // Set true to merge two sample documents created in memory.
    const bool useSamples = false;

    System::SharedPtr<Document> first;
    System::SharedPtr<Document> second;

    if (useSamples)
    {
        first = System::MakeObject<Document>();
        auto firstBuilder = System::MakeObject<DocumentBuilder>(first);
        firstBuilder->Writeln(u"First document: normal text.");

        second = System::MakeObject<Document>();
        auto secondBuilder = System::MakeObject<DocumentBuilder>(second);
        secondBuilder->get_Font()->set_Bold(true);
        secondBuilder->Writeln(u"Second document: bold text.");
    }
    else
    {
        first = System::MakeObject<Document>(System::String(u"first.docx"));
        second = System::MakeObject<Document>(System::String(u"second.docx"));
    }

    first->AppendDocument(second, ImportFormatMode::KeepSourceFormatting);
    first->Save(u"merged.docx");
    return 0;
}
```

Place `first.docx` and `second.docx` in the working directory, or set `useSamples` to `true`. `merged.docx` is overwritten if it exists. An Aspose license removes evaluation limitations; no external service is required. List numbering and section layout may require additional [import options](https://docs.aspose.com/words/cpp/insert-and-append-documents/).

## merge-06

What is the difference between InsertDocument and AppendDocument?

Origin: copilot-cli. Compilation: no_code.

`DocumentBuilder::InsertDocument` inserts a source document **where the builder’s cursor is**—use it to place content in the middle or at a chosen position. `Document::AppendDocument` adds the source document **to the end of the target document**—use it for straightforward concatenation without positioning a builder. Both accept an `ImportFormatMode` to control how imported formatting is handled.

Sources: [Insert and Append Documents guide](https://docs.aspose.com/words/cpp/insert-and-append-documents/), [InsertDocument API](https://reference.aspose.com/words/cpp/aspose.words/documentbuilder/insertdocument/), [AppendDocument API](https://reference.aspose.com/words/cpp/aspose.words/document/appenddocument/).

## merge-07

How to combine several Word documents into a single DOCX file?

Origin: copilot-cli. Compilation: passed.

Use `Document::AppendDocument` to append each source document in order, then save the result with a `.docx` filename. This example expects three input files in the program’s working directory and overwrites `combined.docx` if it already exists.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/ImportFormatMode.h>
#include <system/smart_ptr.h>

int main()
{
    auto combined = System::MakeObject<Aspose::Words::Document>(u"part1.docx");

    auto second = System::MakeObject<Aspose::Words::Document>(u"part2.docx");
    combined->AppendDocument(second, Aspose::Words::ImportFormatMode::KeepSourceFormatting);

    auto third = System::MakeObject<Aspose::Words::Document>(u"part3.docx");
    combined->AppendDocument(third, Aspose::Words::ImportFormatMode::KeepSourceFormatting);

    combined->Save(u"combined.docx");
    return 0;
}
```

`KeepSourceFormatting` aims to retain the appended documents’ formatting; style conflicts can affect the result. The required inputs are `part1.docx`, `part2.docx`, and `part3.docx`. No credentials or external services are used; provide an Aspose.Words license as required for your deployment. The API lookup did not resolve specifically to 26.9.0 (it returned latest-stable), so confirm these signatures against your pinned SDK before compiling.

Sources: [AppendDocument](https://reference.aspose.com/words/cpp/aspose.words/document/appenddocument/), [ImportFormatMode](https://reference.aspose.com/words/cpp/aspose.words/importformatmode/), [Insert and Append Documents in C++](https://docs.aspose.com/words/cpp/insert-and-append-documents/), [Document.Save](https://reference.aspose.com/words/cpp/aspose.words/document/save/).

## find-replace-01

How to find and replace text in a Word document using C++?

Origin: copilot-cli. Compilation: passed.

Use [`Range::Replace`](https://reference.aspose.com/words/cpp/aspose.words/range/replace/) to replace matching text and return the number of replacements. This example creates a sample document, reloads it, and saves the result separately.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/Range.h>
#include <Aspose.Words.Cpp/Replacing/FindReplaceOptions.h>
#include <system/object.h>
#include <system/smart_ptr.h>

#include <iostream>

int main()
{
    auto sample = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(sample);
    builder->Writeln(u"Ruby bought a ruby necklace.");
    sample->Save(u"sample-input.docx");

    auto doc = System::MakeObject<Aspose::Words::Document>(
        System::String(u"sample-input.docx"));

    auto options =
        System::MakeObject<Aspose::Words::Replacing::FindReplaceOptions>();
    options->set_MatchCase(true);
    options->set_FindWholeWordsOnly(true);

    const auto count = doc->get_Range()->Replace(u"Ruby", u"Jade", options);
    doc->Save(u"replaced-output.docx");

    std::cout << "Replacements: " << count << '\n';
    return 0;
}
```

For an existing document, remove the sample-creation statements and change the input path. Both named output files are overwritten if present. No external service is needed; without a license, [evaluation restrictions](https://docs.aspose.com/words/cpp/faq/) apply. The documentation service returned latest-stable API evidence, not a separately identified 26.9.0 reference.

## find-replace-02

How to replace a string in a DOCX file with Aspose.Words?

Origin: copilot-cli. Compilation: passed.

Use `Document` to load the DOCX, then call `Replace` on its `Range` and save the result. `Replace` treats the search text as a literal string, uses case-insensitive matching by default, and returns the number of replacements. ([API reference](https://reference.aspose.com/words/cpp/aspose.words/range/replace/))

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/Range.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    doc->get_Range()->Replace(u"old text", u"new text");
    doc->Save(u"output.docx");
    return 0;
}
```

Place `input.docx` beside the program or adjust its path. Saving chooses the format from the `.docx` extension and overwrites `output.docx` if it already exists. ([Load](https://reference.aspose.com/words/cpp/aspose.words/document/document/), [Save](https://reference.aspose.com/words/cpp/aspose.words/document/save/)) A valid license file is needed for licensed use; evaluation mode has limitations. No external service is required. ([Licensing](https://docs.aspose.com/words/cpp/licensing/))

The named `examples/error-correction.md` wasn’t present in the workspace; I followed the C++ rules included in your prompt.

## find-replace-03

How to replace all occurrences of a word in a document?

Origin: copilot-cli. Compilation: passed.

Use [`Range::Replace`](https://reference.aspose.com/words/cpp/aspose.words/range/replace/) with [options](https://reference.aspose.com/words/cpp/aspose.words.replacing/findreplaceoptions/) for whole-word and case-sensitive matching:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/Range.h>
#include <Aspose.Words.Cpp/Replacing/FindReplaceOptions.h>
#include <system/object.h>
#include <system/smart_ptr.h>

#include <iostream>

int main()
{
    auto sample = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(sample);
    builder->Writeln(u"Ruby bought a ruby necklace. Ruby likes rubies.");
    sample->Save(u"sample-input.docx");

    auto doc = System::MakeObject<Aspose::Words::Document>(u"sample-input.docx");
    auto options = System::MakeObject<Aspose::Words::Replacing::FindReplaceOptions>();
    options->set_MatchCase(false);
    options->set_FindWholeWordsOnly(true);

    int replacements = doc->get_Range()->Replace(u"ruby", u"jade", options);
    doc->Save(u"replaced.docx");

    std::cout << "Replacements: " << replacements << '\n';
    return 0;
}
```

The program creates `sample-input.docx` and `replaced.docx`, overwriting files with those names. For an existing document, remove the sample-creation statements and change the input path. Set `FindWholeWordsOnly` to `false` to replace matches inside longer words.

A [license](https://docs.aspose.com/words/cpp/licensing/) removes evaluation limitations. The MCP reference exposes latest-stable documentation, not a separately pinned 26.9.0 reference.

## find-replace-04

How to find and replace text using regular expressions?

Origin: copilot-cli. Compilation: passed.

Use the regex overload of [`Range::Replace`](https://reference.aspose.com/words/cpp/aspose.words/range/replace/). The corrected header is `system/text/regularexpressions/regex.h`.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/Range.h>
#include <system/smart_ptr.h>
#include <system/text/regularexpressions/regex.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(doc);

    builder->Writeln(u"I chose gray curtains for the grey-accented room.");

    auto pattern =
        System::MakeObject<System::Text::RegularExpressions::Regex>(u"gr(a|e)y");
    doc->get_Range()->Replace(pattern, u"lavender");

    doc->Save(u"RegexReplace.docx");
    return 0;
}
```

The program creates its own sample and writes `RegexReplace.docx` in the current directory, overwriting an existing file. No external service is needed. Without a license, evaluation restrictions apply; see [licensing](https://docs.aspose.com/words/cpp/licensing/).

The original guide citation was malformed; the correct [find-and-replace guide](https://docs.aspose.com/words/cpp/find-and-replace/) supports this approach. The documentation service returned latest-stable evidence rather than a 26.9.0-specific snapshot.

Compiler-feedback repair requests: 1. See repair-log.md and results.json for attempt history.

## find-replace-05

How to perform a case-insensitive text replacement in Word documents?

Origin: copilot-cli. Compilation: passed.

Set [`MatchCase`](https://reference.aspose.com/words/cpp/aspose.words.replacing/findreplaceoptions/get_matchcase/) to `false` and call [`Range::Replace`](https://reference.aspose.com/words/cpp/aspose.words/range/replace/), which returns the number of replacements.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/Range.h>
#include <Aspose.Words.Cpp/Replacing/FindReplaceOptions.h>
#include <system/smart_ptr.h>
#include <cstdint>
#include <iostream>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(doc);
    builder->Writeln(u"Ruby bought a ruby necklace.");
    doc->Save(u"sample-input.docx");

    auto options =
        System::MakeObject<Aspose::Words::Replacing::FindReplaceOptions>();
    options->set_MatchCase(false);

    int32_t count = doc->get_Range()->Replace(u"ruby", u"jade", options);
    doc->Save(u"output.docx");

    std::cout << "Replacements: " << count << '\n';
    return 0;
}
```

The example creates its own input; for an existing document, construct `Document` with its filename instead of creating the sample. Both output files are overwritten if they exist. No external service is required. The [trial](https://docs.aspose.com/words/cpp/licensing/) adds an evaluation watermark and limits document size.

The requested `examples\error-correction.md` file was not present; I used the guidance included in your prompt.

## find-replace-06

How to replace text while preserving document formatting?

Origin: copilot-cli. Compilation: passed.

Use [`Range::Replace`](https://reference.aspose.com/words/cpp/aspose.words/range/replace/) without applying new font settings. This example creates a document with a bold placeholder, replaces it, and saves the result.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/Font.h>
#include <Aspose.Words.Cpp/Range.h>
#include <Aspose.Words.Cpp/Replacing/FindReplaceOptions.h>
#include <system/smart_ptr.h>
#include <iostream>

int main()
{
    auto sample = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(sample);

    builder->Write(u"Hello ");
    builder->get_Font()->set_Bold(true);
    builder->Write(u"_CustomerName_");
    builder->get_Font()->set_Bold(false);
    builder->Write(u", welcome!");
    sample->Save(u"sample-input.docx");

    auto doc = System::MakeObject<Aspose::Words::Document>(
        System::String(u"sample-input.docx"));
    auto options =
        System::MakeObject<Aspose::Words::Replacing::FindReplaceOptions>();
    options->set_MatchCase(true);

    const int count = doc->get_Range()->Replace(
        u"_CustomerName_", u"James Bond", options);
    doc->Save(u"replaced.docx");

    std::cout << "Replacements: " << count << '\n';
    return 0;
}
```

Both files are written in the working directory and overwritten if they exist. For an existing document, load its path instead of creating the sample. If a match spans differently formatted text, inspect the result: preserving every formatting transition in a differently sized replacement requires a custom policy.

No external service is needed. Without a license, [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/) apply. The retrieved API reference does not identify its exact SDK version.

## find-replace-07

How to use FindReplaceOptions in Aspose.Words?

Origin: copilot-cli. Compilation: passed.

Create a [`FindReplaceOptions`](https://reference.aspose.com/words/cpp/aspose.words.replacing/findreplaceoptions/), set its properties, and pass it to [`Range::Replace`](https://reference.aspose.com/words/cpp/aspose.words/range/replace/). This example replaces only case-sensitive, whole-word matches:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/Range.h>
#include <Aspose.Words.Cpp/Replacing/FindReplaceOptions.h>
#include <system/smart_ptr.h>
#include <iostream>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(doc);
    builder->Writeln(u"Ruby bought a ruby necklace. Rubyville is nearby.");

    auto options =
        System::MakeObject<Aspose::Words::Replacing::FindReplaceOptions>();
    options->set_MatchCase(true);
    options->set_FindWholeWordsOnly(true);

    const auto count = doc->get_Range()->Replace(u"Ruby", u"Jade", options);
    std::cout << "Replacements: " << count << '\n';

    doc->Save(u"find-replace-output.docx");
    return 0;
}
```

The sample creates its own document and overwrites `find-replace-output.docx` if it exists. No external service is needed. Without a license, [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/) apply.

The requested `examples/error-correction.md` was unavailable; I used the error-correction guidance included in your prompt.

## digital-signatures-01

How to digitally sign a Word document in C++?

Origin: copilot-cli. Compilation: passed.

Use `CertificateHolder::Create` to load a PKCS#12 (`.pfx`) certificate containing the private key, then `DigitalSignatureUtil::Sign` to write a signed copy. The MCP verified these C++ APIs against its latest-stable reference, but it did not provide 26.9.0-specific metadata or confirm the installed header paths; verify those paths against your 26.9.0 SDK before building.

```cpp
#include <Aspose.Words.Cpp/DigitalSignatures/CertificateHolder.h>
#include <Aspose.Words.Cpp/DigitalSignatures/DigitalSignatureUtil.h>
#include <system/smart_ptr.h>

int main()
{
    System::SharedPtr<Aspose::Words::DigitalSignatures::CertificateHolder> certificateHolder =
        Aspose::Words::DigitalSignatures::CertificateHolder::Create(
            u"signing.pfx",
            u"REPLACE_WITH_PFX_PASSWORD");

    Aspose::Words::DigitalSignatures::DigitalSignatureUtil::Sign(
        u"unsigned.docx",
        u"signed.docx",
        certificateHolder);

    return 0;
}
```

Provide `unsigned.docx` and a password-protected `.pfx` with its private key; keep the certificate password out of source control. The output is written separately, preserving the input. Aspose.Words’ guide lists DOCX among the supported signing formats and says no separate digital-signature license is required, though a valid Aspose.Words license enables full functionality. [Digital-signature guide](https://docs.aspose.com/words/cpp/working-with-digital-signatures/) · [CertificateHolder::Create reference](https://reference.aspose.com/words/cpp/aspose.words.digitalsignatures/certificateholder/create/) · [DigitalSignatureUtil::Sign reference](https://reference.aspose.com/words/cpp/aspose.words.digitalsignatures/digitalsignatureutil/sign/)

## digital-signatures-02

How to add a digital signature to a DOCX file using Aspose.Words?

Origin: copilot-cli. Compilation: passed.

Use `CertificateHolder::Create` to load a PKCS#12 certificate (`.pfx`) containing its private key, then pass it to `DigitalSignatureUtil::Sign` with separate input and output paths. The example creates a DOCX to sign; replace that input with your document as needed.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DigitalSignatures/CertificateHolder.h>
#include <Aspose.Words.Cpp/DigitalSignatures/DigitalSignatureUtil.h>
#include <system/smart_ptr.h>

int main()
{
    const System::String inputDocx = u"unsigned.docx";
    const System::String signedDocx = u"signed.docx";
    const System::String certificatePath = u"signing-certificate.pfx";
    const System::String certificatePassword = u"<replace-with-pfx-password>";

    auto sampleDocument = System::MakeObject<Aspose::Words::Document>();
    sampleDocument->Save(inputDocx);

    auto certificateHolder =
        Aspose::Words::DigitalSignatures::CertificateHolder::Create(
            certificatePath, certificatePassword);

    Aspose::Words::DigitalSignatures::DigitalSignatureUtil::Sign(
        inputDocx, signedDocx, certificateHolder);

    return 0;
}
```

Provide a PFX file with its password and a private key; replace the password placeholder, and avoid hard-coding production credentials. The example does not use a timestamping service. Use an appropriately licensed Aspose.Words for C++ deployment.

Sources: [CertificateHolder::Create](https://reference.aspose.com/words/cpp/aspose.words.digitalsignatures/certificateholder/create/), [DigitalSignatureUtil::Sign](https://reference.aspose.com/words/cpp/aspose.words.digitalsignatures/digitalsignatureutil/sign/), [Working with Digital Signatures in C++](https://docs.aspose.com/words/cpp/working-with-digital-signatures/).

## digital-signatures-03

How to verify digital signatures in a Word document?

Origin: copilot-cli. Compilation: no_code.

Use [`DigitalSignatureUtil::LoadSignatures`](https://reference.aspose.com/words/cpp/aspose.words.digitalsignatures/digitalsignatureutil/loadsignatures/) on the original file, then check each signature’s [`get_IsValid()`](https://reference.aspose.com/words/cpp/aspose.words.digitalsignatures/digitalsignature/get_isvalid/). Check the collection count first: its [`get_IsValid()`](https://reference.aspose.com/words/cpp/aspose.words.digitalsignatures/digitalsignaturecollection/get_isvalid/) also returns true for an unsigned document.

I couldn’t provide the requested standalone program: the MCP results did not identify the required header paths, and access to the local SDK was denied. The example guidance file was also unavailable in the workspace.

## digital-signatures-04

How to check whether a Word document is digitally signed?

Origin: copilot-cli. Compilation: passed.

Use [`DetectFileFormat`](https://reference.aspose.com/words/cpp/aspose.words/fileformatutil/detectfileformat/) and [`get_HasDigitalSignature()`](https://reference.aspose.com/words/cpp/aspose.words/fileformatinfo/get_hasdigitalsignature/):

```cpp
#include <Aspose.Words.Cpp/FileFormatUtil.h>
#include <Aspose.Words.Cpp/FileFormatInfo.h>
#include <iostream>

int main()
{
    auto info = Aspose::Words::FileFormatUtil::DetectFileFormat(u"input.docx");
    std::cout << (info->get_HasDigitalSignature() ? "Signed\n" : "Not signed\n");
    return 0;
}
```

Place `input.docx` in the working directory. This checks **presence, not validity**; signature validation is a separate operation. No certificate or external service is needed to check presence.

The MCP verified the APIs against latest-stable documentation, but did not expose version-specific 26.9.0 evidence or header paths; the two include paths above remain **unverified**.

## digital-signatures-05

How to sign a document with a PFX certificate?

Origin: copilot-cli. Compilation: passed.

`CertificateHolder::Create` loads the PKCS#12/PFX using its password; `DigitalSignatureUtil::Sign` writes a signed copy. The certificate must contain its private key. [CertificateHolder API](https://reference.aspose.com/words/cpp/aspose.words.digitalsignatures/certificateholder/create/) · [Sign API](https://reference.aspose.com/words/cpp/aspose.words.digitalsignatures/digitalsignatureutil/sign/)

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DigitalSignatures/CertificateHolder.h>
#include <Aspose.Words.Cpp/DigitalSignatures/DigitalSignatureUtil.h>
#include <system/smart_ptr.h>

int main()
{
    const System::String inputPath = u"unsigned.docx";
    const System::String outputPath = u"signed.docx";
    const System::String pfxPath = u"signing-certificate.pfx";
    const System::String pfxPassword = u"YOUR_PFX_PASSWORD";

    // Create a sample DOCX. Replace this with your existing unsigned document if needed.
    auto document = System::MakeObject<Aspose::Words::Document>();
    document->Save(inputPath);

    auto certificate =
        Aspose::Words::DigitalSignatures::CertificateHolder::Create(pfxPath, pfxPassword);

    Aspose::Words::DigitalSignatures::DigitalSignatureUtil::Sign(
        inputPath, outputPath, certificate);

    return 0;
}
```

Place the PFX at the specified path and replace the password placeholder; keep real credentials out of source control. The basic signing call needs no timestamp service. For licensed use, load your `.lic` before processing; trial mode has evaluation limitations ([licensing](https://docs.aspose.com/words/cpp/licensing/)). The requested `examples/error-correction.md` was not present in the workspace, so I followed the C++ rules included in your prompt.

## digital-signatures-06

How to remove digital signatures from a Word document?

Origin: copilot-cli. Compilation: passed.

Loading and saving a signed document removes its digital signatures from the saved copy. This **rewrites the document**, so other content or formatting may also change. See [Aspose’s signature documentation](https://reference.aspose.com/words/cpp/aspose.words/document/get_digitalsignatures/).

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(
        System::String(u"signed.docx"));
    doc->Save(u"unsigned.docx");
    return 0;
}
```

Place a signed `signed.docx` in the working directory. The output is `unsigned.docx`; an existing output file is overwritten. No certificate or external service is needed. An Aspose.Words license removes evaluation limitations.

For direct signature removal without a document-model round trip, Aspose also provides [`DigitalSignatureUtil::RemoveAllSignatures`](https://reference.aspose.com/words/cpp/aspose.words.digitalsignatures/digitalsignatureutil/removeallsignatures/). The documentation lookup resolved to latest stable, not specifically 26.9.0.

## digital-signatures-07

How to use DigitalSignatureUtil in Aspose.Words?

Origin: copilot-cli. Compilation: passed.

Use [`DigitalSignatureUtil::Sign`](https://reference.aspose.com/words/cpp/aspose.words.digitalsignatures/digitalsignatureutil/sign/) with a PKCS#12 certificate containing a private key, then use [`LoadSignatures`](https://reference.aspose.com/words/cpp/aspose.words.digitalsignatures/digitalsignatureutil/loadsignatures/) to inspect the result.

The program creates `sample-input.docx` and `signed.docx` in the working directory, overwriting existing files with those names. Supply `certificate.pfx` and replace the password placeholder; use a secure credential source in production. An Aspose license is needed to avoid evaluation limitations. No external service is required.

**Limitations:** The MCP documentation resolved to latest stable, not specifically 26.9.0. Local SDK access was denied, so the digital-signature header paths below could not be verified against that package. The requested `examples/error-correction.md` file was not present; its guidance supplied in the prompt was used instead.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/DigitalSignatures/CertificateHolder.h>
#include <Aspose.Words.Cpp/DigitalSignatures/DigitalSignatureCollection.h>
#include <Aspose.Words.Cpp/DigitalSignatures/DigitalSignatureUtil.h>
#include <Aspose.Words.Cpp/DigitalSignatures/SignOptions.h>
#include <system/smart_ptr.h>

#include <iostream>

int main()
{
    using namespace Aspose::Words;
    using namespace Aspose::Words::DigitalSignatures;

    auto document = System::MakeObject<Document>();
    auto builder = System::MakeObject<DocumentBuilder>(document);
    builder->Writeln(u"Example document to sign.");
    document->Save(u"sample-input.docx");

    auto certificate = CertificateHolder::Create(
        u"certificate.pfx", u"REPLACE_WITH_CERTIFICATE_PASSWORD");

    auto options = System::MakeObject<SignOptions>();
    options->set_Comments(u"Approved");

    DigitalSignatureUtil::Sign(
        u"sample-input.docx", u"signed.docx", certificate, options);

    auto signatures = DigitalSignatureUtil::LoadSignatures(u"signed.docx");
    const auto count = signatures->get_Count();
    std::cout << "Signature count: " << count << '\n';

    if (count == 0 || !signatures->get_IsValid())
    {
        std::cerr << "No signature found or at least one signature is invalid.\n";
        return 1;
    }

    std::cout << "All signatures are valid.\n";
    return 0;
}
```

Check the count as well as `get_IsValid()`: [an empty collection also reports valid](https://reference.aspose.com/words/cpp/aspose.words.digitalsignatures/digitalsignaturecollection/get_isvalid/). Opening and saving a signed document with Aspose.Words can remove its signatures; sign after editing. See the [digital-signature guide](https://docs.aspose.com/words/cpp/working-with-digital-signatures/).

## watermark-01

How to add a watermark to a Word document in C++?

Origin: copilot-cli. Compilation: no_code.

Use [`Document::get_Watermark()->SetText(...)`](https://reference.aspose.com/words/cpp/aspose.words/watermark/settext/) and then [save the document](https://reference.aspose.com/words/cpp/aspose.words/document/save/).

I can’t provide the requested complete program reliably: the documentation lookup did not identify the `Watermark` header, and access to the installed SDK headers was denied. The MCP reference also could not confirm the pinned 26.9.0 version. The [watermark guide](https://docs.aspose.com/words/cpp/working-with-watermark/) shows the API usage but not the required includes.

## watermark-02

How to insert a text watermark into a DOCX file?

Origin: copilot-cli. Compilation: passed.

Load the DOCX, call [`Watermark::SetText`](https://reference.aspose.com/words/cpp/aspose.words/watermark/settext/), and save it under a new name.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/Watermark.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    doc->get_Watermark()->SetText(u"CONFIDENTIAL");
    doc->Save(u"watermarked.docx");
    return 0;
}
```

Place `input.docx` in the working directory. An existing `watermarked.docx` is overwritten. Without a license, [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/) apply.

**Verification gap:** The documentation confirms the APIs, but I could not inspect the installed 26.9.0 SDK to verify the watermark header; the requested guidance file was also unavailable.

## watermark-03

How to add an image watermark to a Word document?

Origin: copilot-cli. Compilation: passed.

Use [`Watermark::SetImage`](https://reference.aspose.com/words/cpp/aspose.words/watermark/setimage/) with an image path and [`ImageWatermarkOptions`](https://reference.aspose.com/words/cpp/aspose.words/imagewatermarkoptions/).

The MCP reference confirms the APIs, but did not expose the two watermark header paths or version-specific 26.9.0 evidence; those include paths remain **unverified**.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/ImageWatermarkOptions.h>
#include <Aspose.Words.Cpp/Watermark.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    auto options = System::MakeObject<Aspose::Words::ImageWatermarkOptions>();

    options->set_Scale(0);       // Automatic sizing.
    options->set_IsWashout(true);

    doc->get_Watermark()->SetImage(u"watermark.png", options);
    doc->Save(u"watermarked.docx");
    return 0;
}
```

Place `input.docx` and `watermark.png` in the working directory. The output path may overwrite an existing file. An Aspose license removes evaluation limitations; no external service is needed.

## watermark-04

How to remove a watermark from a Word document using Aspose.Words?

Origin: copilot-cli. Compilation: passed.

Call [`Watermark::Remove()`](https://reference.aspose.com/words/cpp/aspose.words/watermark/remove/). The missing `Watermark.h` include caused the reported errors.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/Watermark.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");
    doc->get_Watermark()->Remove();
    doc->Save(u"output.docx");
    return 0;
}
```

Place a watermarked `input.docx` in the working directory. The program overwrites `output.docx` if it exists. For custom shape watermarks, see the [shape-removal guidance](https://docs.aspose.com/words/cpp/working-with-watermark/). An unlicensed evaluation adds its own watermark; apply a [license](https://docs.aspose.com/words/cpp/licensing/) before processing to avoid evaluation limitations.

Compiler-feedback repair requests: 1. See repair-log.md and results.json for attempt history.

## watermark-05

How to change the font, size, or color of a text watermark?

Origin: copilot-cli. Compilation: passed.

Use [`TextWatermarkOptions`](https://reference.aspose.com/words/cpp/aspose.words/textwatermarkoptions/) and pass it to [`SetText`](https://reference.aspose.com/words/cpp/aspose.words/watermark/settext/). The example creates a sample document and sets the watermark to Arial, size 36, black.

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/DocumentBuilder.h>
#include <Aspose.Words.Cpp/TextWatermarkOptions.h>
#include <Aspose.Words.Cpp/Watermark.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>();
    auto builder = System::MakeObject<Aspose::Words::DocumentBuilder>(doc);
    builder->Writeln(u"Sample document.");

    auto options = System::MakeObject<Aspose::Words::TextWatermarkOptions>();
    options->set_FontFamily(u"Arial");
    options->set_FontSize(36);
    options->set_Color(System::Drawing::Color::get_Black());
    options->set_IsSemitrasparent(false);

    doc->get_Watermark()->SetText(u"CONFIDENTIAL", options);
    doc->Save(u"watermarked.docx");
    return 0;
}
```

The output path is relative to the working directory and an existing file may be overwritten. For an existing document, construct `Document` with its input path instead. A license is optional for evaluation; no external service is needed. The MCP reference did not establish the watermark header paths or specifically confirm SDK 26.9.0, so those remain unverified.

## watermark-06

How to add a diagonal watermark to a document?

Origin: copilot-cli. Compilation: passed.

Use `TextWatermarkOptions` with `WatermarkLayout::Diagonal`, then pass it to `SetText`. This program adds the watermark to an existing document:

```cpp
#include <Aspose.Words.Cpp/Document.h>
#include <Aspose.Words.Cpp/TextWatermarkOptions.h>
#include <Aspose.Words.Cpp/Watermark.h>
#include <Aspose.Words.Cpp/WatermarkLayout.h>
#include <system/smart_ptr.h>

int main()
{
    auto doc = System::MakeObject<Aspose::Words::Document>(u"input.docx");

    auto options = System::MakeObject<Aspose::Words::TextWatermarkOptions>();
    options->set_Layout(Aspose::Words::WatermarkLayout::Diagonal);

    doc->get_Watermark()->SetText(u"CONFIDENTIAL", options);
    doc->Save(u"output.docx");

    return 0;
}
```

Place `input.docx` in the program’s working directory; it saves the result as `output.docx`. The diagonal layout and `SetText` options overload are documented in the [watermark guide](https://docs.aspose.com/words/cpp/working-with-watermark/) and [API reference](https://reference.aspose.com/words/cpp/aspose.words/watermark/settext/). The example requires Aspose.Words for C++ 26.9.0 and its CodePorting dependency; provide a valid license as needed for your use. No credentials or external services are required.

## watermark-07

How to use the Watermark class in Aspose.Words?

Origin: copilot-cli. Compilation: no_code.

Access the document’s watermark with [`doc->get_Watermark()`](https://reference.aspose.com/words/cpp/aspose.words/document/get_watermark/). Use [`SetText`](https://reference.aspose.com/words/cpp/aspose.words/watermark/settext/) with optional `TextWatermarkOptions`, [`SetImage`](https://reference.aspose.com/words/cpp/aspose.words/watermark/setimage/) for an image, or [`Remove`](https://reference.aspose.com/words/cpp/aspose.words/watermark/remove/) to remove it. See the [watermark guide](https://docs.aspose.com/words/cpp/working-with-watermark/).

**Limitation:** I could not verify the required watermark headers for 26.9.0: the documentation lookup did not expose them, and access to the local SDK was denied. I therefore cannot provide the requested verified standalone program without guessing headers. The requested `examples/error-correction.md` file was also unavailable in the workspace.

## ai-01

What AI-powered features are available in Aspose.Words?

Origin: copilot-cli. Compilation: no_code.

Aspose.Words for C++ documents three AI-powered tasks: [summarizing documents](https://docs.aspose.com/words/cpp/summarize-a-document/), [translating documents](https://docs.aspose.com/words/cpp/translate-a-document/), and [grammar checking](https://docs.aspose.com/words/cpp/grammar-checking/).

- **Summarization:** Create summaries from one or multiple documents and adjust their length.
- **Translation:** Translate document content into a target language. The guide describes Google generative models and support for 300+ languages.
- **Grammar and style checking:** Analyze a document for grammar issues; an option enables stylistic improvements.

The documented provider families include OpenAI, Google, and Anthropic/Claude. The docs also describe integrating self-hosted LLMs. These features call an AI provider, so you need its credentials and service access; Aspose.Words itself does not require a separate AI-feature license. See [supported AI models](https://docs.aspose.com/words/cpp/supported-ai-models/) and the [AI features overview](https://docs.aspose.com/words/cpp/ai-powered-features/).

**Version note:** The configured documentation lookup could not resolve 26.9.0 and returned latest-stable documentation, so check the pinned SDK’s release documentation to confirm version-specific availability.

## ai-02

How to use AI with Aspose.Words in C++?

Origin: copilot-cli. Compilation: no_code.

Aspose.Words can use AI to **summarize, translate, and check grammar** with OpenAI, Google, or Claude models ([supported models](https://docs.aspose.com/words/cpp/supported-ai-models/)).

For summarization, create an [`OpenAiModel`](https://reference.aspose.com/words/cpp/aspose.words.ai/openaimodel/openaimodel/) with a model name and API key, then call [`Summarize`](https://reference.aspose.com/words/cpp/aspose.words.ai/openaimodel/summarize/) with a `Document` and save the returned document. This requires provider credentials and network access; document content is sent to the provider. An Aspose license removes evaluation limitations.

**Limitation:** I could not verify the AI header paths for 26.9.0: the documentation lookup did not provide them, and access to the installed package was denied. I therefore cannot supply the requested standalone program without guessing headers. The API evidence returned was for latest-stable, not explicitly 26.9.0.

## ai-03

How to summarize a document using AI in Aspose.Words?

Origin: copilot-cli. Compilation: no_code.

Aspose.Words provides AI summarization through `AiModel::Create`, `WithApiKey`, `SummarizeOptions::set_SummaryLength`, and `AiModel::Summarize`; the result is a `Document` you can save. The [summarization guide](https://docs.aspose.com/words/cpp/summarize-a-document/) shows this workflow, and the [API reference](https://reference.aspose.com/words/cpp/aspose.words.ai/aimodel/summarize/) confirms the `Summarize` overload.

I can’t provide the requested standalone program with **verified headers for Aspose.Words C++ 26.9.0**: the configured MCP exposes only `latest-stable`, and it doesn’t provide header paths. I won’t guess those includes. The OpenAI example also requires an API key and access to the external provider; see [`WithApiKey`](https://reference.aspose.com/words/cpp/aspose.words.ai/aimodel/withapikey/). The requested `examples/error-correction.md` was not present in the workspace; I followed the guidance included in your prompt.

## ai-04

How to translate a document using AI?

Origin: copilot-cli. Compilation: no_code.

Use [AiModel::Translate](https://reference.aspose.com/words/cpp/aspose.words.ai/aimodel/translate/) to produce a new document in a target [Language](https://reference.aspose.com/words/cpp/aspose.words.ai/language/). Create a model, supply its API key, translate the loaded document, and save the result. A Google model requires a Google API key and network access.

**Limitation:** I can’t provide the requested standalone program reliably: the documentation lookup did not expose the AI header paths, and access to the installed SDK headers was denied. The lookup also could not confirm the API specifically for 26.9.0.

## ai-05

How to use a large language model to process Word documents?

Origin: copilot-cli. Compilation: no_code.

Aspose.Words can use an LLM to [summarize](https://docs.aspose.com/words/cpp/summarize-a-document/), translate, or check grammar in a Word document. For summarization, load a `Document`, create an `AiModel` for a supported provider, configure its API key, call `Summarize`, and save the returned document. See the [supported models guide](https://docs.aspose.com/words/cpp/supported-ai-models/).

A complete 26.9.0 program remains blocked: the documentation endpoint returned latest-stable API evidence but not the required AI header paths, and access to the local SDK was denied. An external provider account, API key and network access are required; review its data-handling terms before sending sensitive documents.

## ai-06

How to integrate Aspose.Words with OpenAI?

Origin: copilot-cli. Compilation: no_code.

Aspose.Words can use OpenAI to [summarize documents](https://docs.aspose.com/words/cpp/summarize-a-document/): create an `AiModel` with `AiModelType::Gpt4OMini`, supply an API key with `WithApiKey`, then call `Summarize` and save the returned document.

The standalone program is **incomplete**: the MCP documentation did not identify the required AI header paths, and access to the installed SDK headers was denied. The available reference also resolves to latest-stable, so compatibility with 26.9.0 could not be established.

Running the integration requires an OpenAI API key, service access and network connectivity. Document content is sent to the AI service; review its data-handling requirements before processing sensitive files. An Aspose license removes [evaluation limitations](https://docs.aspose.com/words/cpp/licensing/).

## ai-07

How to use AI models to analyze document content?

Origin: copilot-cli. Compilation: no_code.

Aspose.Words can analyze document content by sending it to an AI model for tasks such as [summarization](https://reference.aspose.com/words/cpp/aspose.words.ai/aimodel/summarize/) and [grammar checking](https://reference.aspose.com/words/cpp/aspose.words.ai/aimodel/checkgrammar/). Create an AI model, supply the provider’s API key, then pass a `Document` to the desired operation. Review generated results against the source.

**Limitation:** I couldn’t verify the AI header paths or the API specifically for SDK 26.9.0: the documentation endpoint resolved to latest-stable, and local SDK access was denied. I therefore can’t provide the requested standalone program without guessing. AI processing also requires provider credentials and sends document content to an external service.

## ai-08

What classes are available in the Aspose.Words.AI namespace?

Origin: copilot-cli. Compilation: no_code.

The C++ reference lists six classes in [`Aspose::Words::AI`](https://reference.aspose.com/words/cpp/aspose.words.ai/):

- [`AiModel`](https://reference.aspose.com/words/cpp/aspose.words.ai/aimodel/) — abstract base for AI model integration.
- [`AnthropicAiModel`](https://reference.aspose.com/words/cpp/aspose.words.ai/anthropicaimodel/) — Anthropic model integration.
- [`GoogleAiModel`](https://reference.aspose.com/words/cpp/aspose.words.ai/googleaimodel/) — Google Gemini model integration.
- [`OpenAiModel`](https://reference.aspose.com/words/cpp/aspose.words.ai/openaimodel/) — OpenAI model integration.
- [`CheckGrammarOptions`](https://reference.aspose.com/words/cpp/aspose.words.ai/checkgrammaroptions/) — options for grammar checking.
- [`SummarizeOptions`](https://reference.aspose.com/words/cpp/aspose.words.ai/summarizeoptions/) — options for document summarization.

The namespace also contains the enums `AiModelType`, `Language`, and `SummaryLength`. The available documentation did not independently confirm the list specifically for version 26.9.0.
