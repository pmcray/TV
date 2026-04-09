import random
import os

months = [
    ("The First Visibility", 31, "The first step is always into the unknown."),
    ("The Leap of Logic", 29, "A leap of faith requires a leap of logic."),
    ("The Invisible Winds", 31, "The winds of change are often invisible."),
    ("The Data Wash", 30, "Showers of data wash away the noise."),
    ("The Hidden Roots", 31, "Blossoming patterns reveal hidden roots."),
    ("The Shortest Shadow", 30, "The longest day sees the shortest shadows."),
    ("The Heat Mirage", 31, "Heat reveals the mirage of the real."),
    ("The Strange Harvest", 31, "Harvesting the fruits of a strange loop."),
    ("The Mental Equinox", 30, "The equinox of the mind."),
    ("The Lengthening Light", 31, "Shadows lengthen, but the light is clearer."),
    ("The Fog of Disguise", 30, "Fog is just visibility in disguise."),
    ("The Closing Circle", 31, "The circle closes, but the loop continues.")
]

month_names_real = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]

def generate_title():
    prefixes = ["The", "A", "Invisible", "Recursive", "Quantum", "Shadowed", "Redacted", "Neutron", "Imperial", "Logical", "Strange", "Visible", "Hidden", "Echoing", "Binary", "Fragmented", "Tangled", "Infinite", "Nuclear", "Optical"]
    middles = ["Loop", "Dossier", "Scattering", "Ambition", "Paradox", "Mirror", "Ledger", "Protocol", "Tesseract", "Reflection", "Resonance", "Symmetry", "Hierarchy", "Labyrinth", "Ghost", "Cipher", "Lens", "Void", "Prism", "Engine"]
    suffixes = ["of Salford", "at Oxford", "in London", "for Extra Freshness", "of the Soul", "between Levels", "without End", "in the Night", "beyond Sight", "under Pressure", "of the Unseen", "of Power", "of the Mind", "against the Grain", "from the Gaps"]
    
    if random.random() < 0.02:
        return "Picowaved for Extra Freshness"
    return f"{random.choice(prefixes)} {random.choice(middles)} {random.choice(suffixes)}"

def generate_month_file(part_title, days, epigraph, start_day_num, month_name_real):
    filename = f"TV_{month_name_real.lower()}.tex"
    with open(filename, "w") as f:
        # Use \parttitle macro for months
        f.write(f"\\parttitle{{{part_title.upper()}}}{{{epigraph}}}{{The Unseen Observer}}\n\n")
        for d in range(1, days + 1):
            day_num = start_day_num + d - 1
            title = generate_title()
            # Use \daytitle macro for sections
            f.write(f"\\daytitle{{{month_name_real}}}{{{d}}}{{{title}}}{{{day_num}}}\n")
            f.write("This is the placeholder text for this day. The logic of the seen and the unseen unfolds here, in the space between the lines. Every neutron scattered is a thought redirected; every loop closed is a story begun.\n")
            f.write("\\vfill\n")
            f.write("\\achilles I feel as though we have been here before, Mr. T.\n")
            f.write("\\tortoise In a recursive world, Achilles, 'before' is just another word for 'again'.\n")
            f.write("\\endday\n\n")
    return day_num + 1

if __name__ == "__main__":
    current_day = 1
    for i, (p_title, m_days, m_epi) in enumerate(months):
        current_day = generate_month_file(p_title, m_days, m_epi, current_day, month_names_real[i])
    print("TV month files regenerated.")
