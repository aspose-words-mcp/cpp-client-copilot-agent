"""Bounded, path-redacted feedback for Copilot; no builds or network calls here."""
import re
from pathlib import Path

def redact_paths(text):
    text=re.sub(r"(?i)[a-z]:[\\/][^\r\n\"'<>]*", '[local-path]', text)
    text=re.sub(r"\\\\[^\s\"'<>]+", '[local-path]', text)
    text=re.sub(r"(?<![:/\w])/(?:home|Users|tmp|opt|mnt|var)/[^\s\"'<>]*", '[local-path]', text)
    return text

def compiler_feedback(verification):
    errors=[]
    for block in verification.get('blocks',[]):
        if block.get('status')=='passed':continue
        for line in block.get('diagnostics','').splitlines():
            match=re.search(r'(?:fatal )?error\s+[A-Z]+\d+\s*:',line)
            if match:
                error=line[match.start():].split(' [')[0]
                errors.append(redact_paths(error))
    return '\n'.join(dict.fromkeys(errors))[:5000]

def sdk_header_context(packages, answer='', diagnostics='', include_symbols=False):
    if not packages:return ''
    names=set('Document DocumentBuilder SaveFormat ImportFormatMode Font Range RevisionCollection SectionCollection MailMerge FindReplaceOptions PdfSaveOptions ImageSaveOptions PageSet object array smart_ptr'.split())
    names.update(re.findall(r'([A-Za-z_]\w*)\.(?:h|hpp)',answer))
    names.update(x.split('::')[-1] for x in re.findall(r"undefined type '([^']+)'",diagnostics))
    symbols=set(re.findall(r'\b[A-Za-z_]\w*\b',answer)) if include_symbols else set()
    headers=[];symbol_headers=[]
    for package in ('Aspose.Words.Cpp.26.9.0','CodePorting.Translator.Cs2Cpp.Framework.26.9.0'):
        root=Path(packages)/package/'build/native/include'
        if not root.exists():continue
        for path in root.rglob('*.h'):
            rel=path.relative_to(root).as_posix()
            if '/Model/' in rel:continue
            if path.stem in names:headers.append(rel)
            if path.stem in symbols:symbol_headers.append(rel)
    selected=list(dict.fromkeys(sorted(set(symbol_headers))+sorted(set(headers))))[:100]
    return '\nExisting SDK-relative headers (selected, not exhaustive):\n'+'\n'.join(selected) if selected else ''

def repair_prompt(base_prompt,answer,verification,packages):
    feedback=compiler_feedback(verification)
    context=sdk_header_context(packages,answer,feedback)
    return (base_prompt+context+'\nRepair the entire answer using these compiler errors. Preserve requested behavior and supporting citations. Do not delete functionality, invent APIs, or replace the program with a trivial main to get a pass.\nPrevious answer:\n'+redact_paths(answer)[:12000]+'\nCompiler feedback:\n'+feedback)
