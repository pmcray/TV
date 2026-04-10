import random
import os

months = [
    ("The First Visibility", 31, "The first step is always into the unknown.", "The Unseen Observer", "Introduction", "Every visibility is a kind of concealment.", "The Hidden Hand", "Mirror of Salford"),
    ("The Leap of Logic", 29, "A leap of faith requires a leap of logic.", "The Unseen Observer", "", "Logic is the art of going wrong with confidence.", "Joseph Wood Krutch", "The Leap"),
    ("The Invisible Winds", 31, "The winds of change are often invisible.", "The Unseen Observer", "", "You cannot see the wind, but you can see the damage it does.", "Unknown", ""),
    ("The Data Wash", 30, "Oh, to be in England / Now that April’s there,", "Robert Browning", "Home-Thoughts, from Abroad", "April is the cruellest month, breeding / Lilacs out of the dead land,", "T.S. Eliot", "The Waste Land"),
    ("The Hidden Roots", 31, "Blossoming patterns reveal hidden roots.", "The Unseen Observer", "", "The root of all superstition is that men observe when a thing hits, but not when it misses.", "Francis Bacon", "Novum Organum"),
    ("The Shortest Shadow", 30, "The longest day sees the shortest shadows.", "The Unseen Observer", "", "Even the smallest shadow has a source of light.", "The Unseen Observer", ""),
    ("The Heat Mirage", 31, "Heat reveals the mirage of the real.", "The Unseen Observer", "", "Reality is merely an illusion, albeit a very persistent one.", "Albert Einstein", ""),
    ("The Strange Harvest", 31, "Harvesting the fruits of a strange loop.", "The Unseen Observer", "", "The harvest is plenty, but the laborers are few.", "Matthew 9:37", ""),
    ("The Mental Equinox", 30, "The equinox of the mind.", "The Unseen Observer", "", "Balance is not something you find, it's something you create.", "Unknown", ""),
    ("The Lengthening Light", 31, "Shadows lengthen, but the light is clearer.", "The Unseen Observer", "", "Light is the shadow of God.", "Sir Thomas Browne", ""),
    ("The Fog of Disguise", 30, "Fog is just visibility in disguise.", "The Unseen Observer", "", "Fog is the medium of the ghost.", "The Unseen Observer", ""),
    ("The Closing Circle", 31, "The circle closes, but the loop continues.", "The Unseen Observer", "", "The end is where we start from.", "T.S. Eliot", "Little Gidding")
]

month_names_real = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def generate_title():
    prefixes = ["The", "A", "Invisible", "Recursive", "Quantum", "Shadowed", "Redacted", "Neutron", "Imperial", "Logical", "Strange", "Visible", "Hidden", "Echoing", "Binary", "Fragmented", "Tangled", "Infinite", "Nuclear", "Optical"]
    middles = ["Loop", "Dossier", "Scattering", "Ambition", "Paradox", "Mirror", "Ledger", "Protocol", "Tesseract", "Reflection", "Resonance", "Symmetry", "Hierarchy", "Labyrinth", "Ghost", "Cipher", "Lens", "Void", "Prism", "Engine"]
    suffixes = ["of Salford", "at Oxford", "in London", "for Extra Freshness", "of the Soul", "between Levels", "without End", "in the Night", "beyond Sight", "under Pressure", "of the Unseen", "of Power", "of the Mind", "against the Grain", "from the Gaps"]
    
    if random.random() < 0.02:
        return "Picowaved for Extra Freshness"
    return f"{random.choice(prefixes)} {random.choice(middles)} {random.choice(suffixes)}"

def generate_month_file(part_title, days, e1, a1, b1, e2, a2, b2, start_day_num, month_name_real):
    filename = f"TV_{month_name_real.lower()}.tex"
    with open(filename, "w") as f:
        # Use \parttitle macro for months
        f.write(f"\\parttitle{{{part_title}}}{{{e1}}}{{{a1}}}{{{b1}}}{{{e2}}}{{{a2}}}{{{b2}}}\n\n")
        for d in range(1, days + 1):
            day_num = start_day_num + d - 1
            title = generate_title()
            
            # Special case for November 18
            if month_name_real == "November" and d == 18:
                title = "Proposition 7"
                f.write(f"\\daytitle{{{month_name_real}}}{{{d}}}{{{title}}}{{{day_num}}}\n")
                f.write("\\blackblock{140mm}\n")
                f.write("\\startdialogue\n")
                f.write("\\blackblock{160mm}\n")
                f.write("\\endday\n\n")
                continue
            
            # Special case for April 16
            if month_name_real == "April" and d == 16:
                title = "Lucky Him"

            # Use \daytitle macro for sections
            f.write(f"\\daytitle{{{month_name_real}}}{{{d}}}{{{title}}}{{{day_num}}}\n")
            f.write("\\filler \\filler \\filler \\filler \\filler \n\n")
            f.write("\\startdialogue\n")
            f.write("\\filler \\filler \\filler \\filler \\filler \n\n")
            f.write("\\endday\n\n")
    return day_num + 1

if __name__ == "__main__":
    current_day = 1
    for i, (p_title, m_days, e1, a1, b1, e2, a2, b2) in enumerate(months):
        current_day = generate_month_file(p_title, m_days, e1, a1, b1, e2, a2, b2, current_day, month_names_real[i])
    print("TV month files regenerated.")
