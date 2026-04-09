import re
import os

def clean_bib(text):
    text = text.replace('\f', '\n')
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        s_line = line.strip()
        # Skip page headers/numbers
        if re.match(r'^Bibliography\s+\d+$', s_line): continue
        if re.match(r'^\d+$', s_line): continue
        cleaned_lines.append(line)
    return '\n'.join(cleaned_lines)

def convert_bib_to_optex(text):
    # Basic formatting: try to detect author/title and apply \it etc.
    # In Hofstadter's bib, entries usually start with Author. Title.
    # But for now, let's just do basic escaping.
    text = text.replace('&', r'\&')
    text = text.replace('#', r'\#')
    text = text.replace('_', r'\_')
    text = text.replace('%', r'\%')
    return text

if __name__ == "__main__":
    with open("MT_extracted.txt", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Bibliography starts around line 32506
    # Let's find the exact position
    match = re.search(r'\n\s*Bibliography\s*\n', content[1000000:])
    if match:
        bib_start = 1000000 + match.end()
        # Look for Index or end of file
        index_match = re.search(r'\n\s*Index\s*\n', content[bib_start:])
        if index_match:
            bib_end = bib_start + index_match.start()
        else:
            bib_end = len(content)
            
        bib_content = content[bib_start:bib_end]
        
        if not os.path.exists("MT"): os.makedirs("MT")
        with open("MT/MT_Bibliography.tex", "w") as f:
            f.write(convert_bib_to_optex(clean_bib(bib_content)))
        print("MT Bibliography extracted.")
