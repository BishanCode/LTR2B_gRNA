import csv
from collections import OrderedDict

# List of gRNAs from the paper
gRNAs = [
    "TTAACTACTGGGTTTAGGCC",
    "TAGTGTTGTGAGCCCTTAAA",
    "GACACCGAGTTGTAGAAGGA",
    "CTTTATTCAGCTGGGAGCAT"
]

def find_matches(target):
    """Find matches for each gRNA and return detailed information."""
    matches = []
    unique_locations = set()
    for row in target:
        for gRNA in gRNAs:
            if gRNA in row['Sequence'].upper():
                location = f"{row['Chromosomes']} {row['Query begin']} {row['Query end']}"
                matches.append(location)  # Store only the location
                unique_locations.add(location)
    return matches, len(unique_locations)

# Read LTR2B file
with open('LTR2B_Seq.csv', 'r') as f:
    csv_reader = list(csv.DictReader(f))

# Find matches
match_details, unique_match_count = find_matches(csv_reader)

# Write results to output file
with open('check_study_detailed.txt', 'w') as out_file:
    out_file.write(f"Total matches (including duplicates): {len(match_details)}\n")
    out_file.write(f"Unique location matches: {unique_match_count}\n\n")
    out_file.write("Detailed matches (Chromosome Query_begin Query_end):\n")
    for location in match_details:
        out_file.write(f"{location}\n")

print("Detailed results have been written to check_study_detailed.txt")
