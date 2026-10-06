import re
import os

def parse_bibliography(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    entries = []
    current_entry = None
    start_parsing = False
    
    for line in lines:
        s_line = line.strip()
        if not s_line: continue
        if "Bibliography" in s_line and any(char.isdigit() for char in s_line): continue
        if "\\chaptertitle" in s_line: continue
        if "The presence of two asterisks" in s_line:
            start_parsing = True
            continue
        if not start_parsing:
            if line[0].isalnum() and not line.startswith(' '):
                start_parsing = True
            else:
                continue
        if "The presence of a single asterisk" in s_line: continue
        if "I have not given many direct pointers" in s_line: continue
        if "chosen to give \"meta-pointers\"" in s_line: continue

        is_new_entry = False
        if (line[0].isalnum() or line.startswith('*') or line.startswith('.')) and not line.startswith(' '):
            is_new_entry = True

        if is_new_entry:
            if current_entry:
                entries.append(current_entry)
            current_entry = line
        else:
            if current_entry:
                current_entry += " " + s_line
            else:
                current_entry = s_line

    if current_entry:
        entries.append(current_entry)
    return entries

def clean_entry(text):
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def to_primitive_tex(entries, prefix, last_author_global):
    tex_entries = []
    last_author = last_author_global
    
    for i, raw_entry in enumerate(entries):
        text = clean_entry(raw_entry)
        if not text: continue
        if len(text) < 15: continue
        if "The presence of two asterisks" in text: continue

        importance = ""
        if text.startswith('**'):
            importance = "**"
            text = text[2:].strip()
        elif text.startswith('*'):
            importance = "*"
            text = text[1:].strip()
        
        author = "Unknown"
        title = "Unknown"
        rest = ""
        
        if text.startswith('.'):
            author = last_author
            text = text[1:].strip()
        else:
            match = re.match(r'^([^.]{3,})\.\s+(.*)', text)
            if match:
                author = match.group(1).strip()
                text = match.group(2).strip()
                last_author = author
            else:
                parts = text.split('.', 1)
                if len(parts) > 1:
                    author = parts[0].strip()
                    text = parts[1].strip()
                    last_author = author

        title_match = re.match(r'^([^.?!]+[.?!])\s+(.*)', text)
        if title_match:
            title = title_match.group(1).strip()
            rest = title_match.group(2).strip()
        else:
            title = text
            rest = ""

        # OpTeX uses \it for italics/slanted
        if '"' in title or '“' in title or '`' in title:
            # Article
            clean_title = title.strip('"“"”`\'')
            formatted_title = f"`{clean_title}'"
        else:
            # Book
            formatted_title = f"{{\\it {title}}}"
        
        note = rest
        imp_str = f"\\llap{{{importance}\\enspace}}" if importance else ""
        
        # USE ONLY PRIMITIVES AND OPTEX COMPATIBLE MACROS
        line = f"\\par\\noindent\\hangindent=2em {imp_str}{{\\bf {author}.}} {formatted_title} {note}\n"
        tex_entries.append(line)
        
    return "\n".join(tex_entries), last_author

if __name__ == "__main__":
    geb_entries = parse_bibliography("GEB/GEB_Bibliography.tex")
    geb_tex, last_a = to_primitive_tex(geb_entries, "GEB", "Unknown")
    with open("GEB_formatted.tex", "w", encoding="utf-8") as f:
        f.write(geb_tex)
    
    mt_entries = parse_bibliography("MT/MT_Bibliography.tex")
    mt_tex, last_a = to_primitive_tex(mt_entries, "MT", last_a)
    with open("MT_formatted.tex", "w", encoding="utf-8") as f:
        f.write(mt_tex)
        
    print("GEB_formatted.tex and MT_formatted.tex regenerated with \\it.")
