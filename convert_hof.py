import re
import sys

def convert_text_to_optex(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output = ["\\input hofstadter.opm\n\n"]
    
    characters = {
        "ACHILLES": "\\achilles",
        "TORTOISE": "\\tortoise",
        "Zeno": "\\zeno",
        "ZENO": "\\zeno",
        "Achilles": "\\achilles",
        "Tortoise": "\\tortoise",
    }

    for line in lines:
        line = line.strip()
        
        if not line:
            output.append("\n\n")
            continue

        if line.replace(" ", "") == "***" or line.replace(" ", "") == "* * *":
            output.append("\n\\separator\n")
            continue

        if re.search(r'\s{5,}\d+$', line) or (re.search(r'^\d+$', line)):
            continue
            
        match_chapter = re.match(r'^Chapter\s+([\d\w]+)', line, re.I)
        if match_chapter:
            output.append(f"\n\\chapter {{{match_chapter.group(1)}}}\n")
            continue

        match_section = re.match(r'^Section\s+([\d\wIVX]+):', line, re.I)
        if match_section:
            output.append(f"\n\\sectiontitle {{{line}}}\n")
            continue
            
        match_rule = re.match(r'^RULE\s+([\w\d]+):(.*)', line, re.I)
        if match_rule:
            output.append(f"\n\\rule {match_rule.group(1)}: {match_rule.group(2).strip()}\\par\n")
            continue

        match_dialogue = re.match(r'^([A-Za-z]+):+:?\s*(.*)', line)
        if match_dialogue:
            name = match_dialogue.group(1)
            content = match_dialogue.group(2)
            if name.upper() in characters:
                output.append(f"\n{characters[name.upper()]} {content}\\par\n")
                continue
            elif name in characters:
                output.append(f"\n{characters[name]} {content}\\par\n")
                continue

        if line.startswith("(") and line.endswith(")"):
            output.append(f"\n\\intro {line} \\endintro\n")
            continue
            
        # Default text
        output.append(f"{line} ")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("".join(output))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_hof.py input.txt output.tex")
    else:
        convert_text_to_optex(sys.argv[1], sys.argv[2])
