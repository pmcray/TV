import html
import csv
import re
from datetime import datetime

input_file_path = '/home/pmc/Documents/TV/US_Kindle_Book_List_20260612'
output_file_path = '/home/pmc/Documents/TV/US_Kindle_Book_List_20260612.csv'

with open(input_file_path, 'r', encoding='utf-8') as f:
    lines = [line.rstrip('\n') for line in f]

# Find matches using the date pattern
date_pattern = re.compile(r"^Acquired on ([A-Z][a-z]+ \d{1,2}, \d{4})$")
acquired_indices = []
acquired_dates_raw = []

for i, line in enumerate(lines):
    match = date_pattern.match(line.strip())
    if match:
        acquired_indices.append(i)
        acquired_dates_raw.append(match.group(1))

def parse_date_iso(date_str):
    try:
        dt = datetime.strptime(date_str, "%B %d, %Y")
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return ""

books = []
for i in range(len(acquired_indices)):
    idx = acquired_indices[i]
    title = html.unescape(lines[idx-2].strip())
    author = html.unescape(lines[idx-1].strip())
    acquired_date_raw = acquired_dates_raw[i]
    acquired_date_iso = parse_date_iso(acquired_date_raw)
    
    if i < len(acquired_indices) - 1:
        end = acquired_indices[i+1] - 2
    else:
        end = len(lines)
    
    details = [line.strip() for line in lines[idx+1 : end] if line.strip()]
    
    # Parse detail fields
    read_status = "No"
    shared_with = ""
    acquired_by = ""
    devices_count = 0
    update_available = "No"
    additional_formats = "No"
    
    for k, detail in enumerate(details):
        if detail == "READ":
            read_status = "Yes"
        elif detail.startswith("Shared with "):
            shared_with = detail.replace("Shared with ", "").strip()
        elif detail.startswith("Acquired by "):
            acquired_by = detail.replace("Acquired by ", "").strip()
        elif detail == "Update available":
            update_available = "Yes"
        elif detail == "Download available in additional formats":
            additional_formats = "Yes"
        elif detail == "In" and k + 2 < len(details) and details[k+2] in ("Device", "Devices"):
            try:
                devices_count = int(details[k+1])
            except ValueError:
                pass
                
    books.append({
        "Title": title,
        "Author": author,
        "Acquired Date": acquired_date_raw,
        "Acquired Date ISO": acquired_date_iso,
        "Read Status": read_status,
        "Shared With": shared_with,
        "Acquired By": acquired_by,
        "Devices": devices_count,
        "Update Available": update_available,
        "Additional Formats": additional_formats
    })

# Write to CSV
headers = [
    "Title", 
    "Author", 
    "Acquired Date", 
    "Acquired Date ISO", 
    "Read Status", 
    "Shared With", 
    "Acquired By", 
    "Devices", 
    "Update Available", 
    "Additional Formats"
]

with open(output_file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(books)

print(f"Successfully generated clean CSV with {len(books)} books.")
print(f"Output saved to: {output_file_path}")
