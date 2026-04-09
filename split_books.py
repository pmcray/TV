import re
import os
import shutil

def clean_text(text):
    text = text.replace('\f', '\n')
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        s_line = line.strip()
        if re.match(r'^\d+$', s_line): continue
        if re.match(r'^(Contents|Overview|Introduction|Chapter|Minds and Thoughts|Artificial Intelligence|Stuff and Nonsense|Lisp:|Dilemmas for Superrational Thinkers)\s+[vix0-9]+$', s_line, re.I):
            continue
        cleaned_lines.append(line)
    return '\n'.join(cleaned_lines)

def convert_to_optex(body):
    # Escape TeX special characters
    body = body.replace('&', r'\&')
    body = body.replace('#', r'\#')
    body = body.replace('_', r'\_')
    body = body.replace('%', r'\%')
    
    body = re.sub(r'^\s*ACHILLES:\s+', r'\\achilles ', body, flags=re.MULTILINE)
    body = re.sub(r'^\s*TORTOISE:\s+', r'\\tortoise ', body, flags=re.MULTILINE)
    body = re.sub(r'^\s*Zeno:\s+', r'\\zeno ', body, flags=re.MULTILINE)
    # Ensure \rule has a \par
    body = re.sub(r'RULE\s+(\w+):\s+([^\n]+)', r'\\rule \1: \2\\par\n', body)
    body = body.replace('\\separator', r'\separator')
    return body

def process_book(book_name, file_path, titles, start_char_hint):
    if os.path.exists(book_name):
        shutil.rmtree(book_name)
    os.makedirs(book_name)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pages = content.split('\f')
    
    body_start_page = 0
    first_title = titles[0].lower()
    total_chars = 0
    for i, page in enumerate(pages):
        total_chars += len(page)
        if total_chars > start_char_hint and first_title in page.lower():
            body_start_page = i
            break
            
    front_matter = pages[:body_start_page]
    body_pages = pages[body_start_page:]
    
    with open(f'{book_name}/{book_name}_FrontMatter.tex', 'w') as f:
        f.write(convert_to_optex(clean_text("\n".join(front_matter))))
        
    main_tex = [f"\\input hofstadter.opm\n", f"\\input {book_name}/{book_name}_FrontMatter.tex\n"]
    
    current_title = titles[0]
    current_content = []
    
    def save_part(title, content):
        if not content: return
        safe_title = re.sub(r'[^a-zA-Z0-9]', '_', title)[:60].strip('_')
        filename = f"{book_name}_{safe_title}.tex"
        full_path = f"{book_name}/{filename}"
        with open(full_path, 'w') as f:
            if "Chapter" in title:
                match = re.match(r'Chapter ([IVX0-9]+):\s*(.*)', title)
                if match:
                    f.write(f"\\chapter{{{match.group(1)}}}\n")
                    f.write(f"\\chaptertitle{{{match.group(2)}}}\n\n")
                else:
                    f.write(f"\\chaptertitle{{{title}}}\n\n")
            elif "Section" in title:
                f.write(f"\\sectiontitle{{{title}}}\n\n")
            else:
                f.write(f"\\chaptertitle{{{title}}}\n\n")
            f.write(convert_to_optex(clean_text("\n".join(content))))
            f.write("\n")
        main_tex.append(f"\\input {book_name}/{filename}\n")

    for page in body_pages:
        found_new_title = False
        page_head = page.lower()[:300]
        
        for t in titles:
            t_clean = t.lower()
            if t_clean in page_head:
                pattern = rf'^\s*(?:\d+\.?\s*)?{re.escape(t_clean)}\s*$'
                if re.search(pattern, page_head, re.MULTILINE):
                    save_part(current_title, current_content)
                    current_title = t
                    current_content = [page]
                    found_new_title = True
                    break
        
        if not found_new_title:
            current_content.append(page)
            
    save_part(current_title, current_content)
    
    with open(f'{book_name}_main.tex', 'w') as f:
        f.write("".join(main_tex))
        f.write("\\bye\n")

if __name__ == "__main__":
    geb_titles = [
        "Introduction: A Musico-Logical Offering",
        "Three-Part Invention",
        "Chapter I: The MU-puzzle",
        "Two-Part Invention",
        "Chapter II: Meaning and Form in Mathematics",
        "Sonata for Unaccompanied Achilles",
        "Chapter III: Figure and Ground",
        "Contracrostipunctus",
        "Chapter IV: Consistency, Completeness, and Geometry",
        "Little Harmonic Labyrinth",
        "Chapter V: Recursive Structures and Processes",
        "Canon by Intervallic Augmentation",
        "Chapter VI: The Location of Meaning",
        "Chromatic Fantasy, And Feud",
        "Chapter VII: The Propositional Calculus",
        "Crab Canon",
        "Chapter VIII: Typographical Number Theory",
        "A Mu Offering",
        "Chapter IX: Mumon and Gödel",
        "Prelude ...",
        "Chapter X: Levels of Description, and Computer Systems",
        "Ant Fugue",
        "Chapter XI: Brains and Thoughts",
        "English French German Suit",
        "Chapter XII: Minds and Thoughts",
        "Aria with Diverse Variations",
        "Chapter XIII: BlooP and FlooP and GlooP",
        "Air on G's String",
        "Chapter XIV: On Formally Undecidable Propositions of TNT",
        "Birthday Cantatatata ...",
        "Chapter XV: Jumping out of the System",
        "Edifying Thoughts of a Tobacco Smoker",
        "Chapter XVI: Self-Ref and Self-Rep",
        "The Magn fierab, Indeed",
        "Chapter XVII: Church, Turing, Tarski, and Others",
        "SHRDLU, Toy of Man's Designing",
        "Chapter XVIII: Artificial Intelligence: Retrospects",
        "Contrafactus",
        "Chapter XIX: Artificial Intelligence: Prospects",
        "Sloth Canon",
        "Chapter XX: Strange Loops, Or Tangled Hierarchies",
        "Six-Part Ricercar",
        "Notes",
        "Bibliography",
        "Credits",
        "Index"
    ]
    
    mt_titles = [
        "Introduction",
        "Section I:",
        "Snags and Snarls",
        "On Self-Referential Sentences",
        "The Virus of Self-Reference",
        "Self-Referential Sentences: A Follow-up",
        "Section II:",
        "Sense and Nonsense",
        "WorldViews in Collision",
        "Number Theory as a World of Pure Form",
        "The Game of Nomic",
        "Section III:",
        "The Architecture of Computation",
        "Lisp: Atoms and Lists",
        "Lisp: Functions and Recursion",
        "Lisp: Lists and Recursion",
        "Section IV:",
        "Treasure Troves of Thought",
        "The Genetic Code: A Language for Life",
        "Section V:",
        "Structure and Strangeness",
        "Analogies and Roles in Human Language",
        "Section VI:",
        "Spirit and Substance",
        "Artificial Intelligence: A Retrospect",
        "Section VII:",
        "Selection and Stability",
        "The Evolution of Cooperation",
        "Section VIII:",
        "Sanity and Survival",
        "On the Real Nature of the Crisis",
        "Annotated Bibliography",
        "Index"
    ]
    
    process_book("GEB", "GEB_extracted.txt", geb_titles, 60000)
    process_book("MT", "MT_extracted.txt", mt_titles, 40000)
