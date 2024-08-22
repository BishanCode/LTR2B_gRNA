import csv
from collections import OrderedDict

def count_matches(sequence, target):
    return sum(1 for row in target if sequence in row['Sequence'].upper())

# Read alignment file
alignment_sequences = OrderedDict()
with open('extracted_gRNA_DF_T_1.txt', 'r') as f:
    next(f)  # Skip header
    for line in f:
        chrom, start, end, seq = line.strip().split('\t')
        if seq not in alignment_sequences:
            alignment_sequences[seq] = {'count': 0, 'occurrences': 1}
        else:
            alignment_sequences[seq]['occurrences'] += 1

# Read LTR2B file
with open('LTR2B_Seq.csv', 'r') as f:
    csv_reader = list(csv.DictReader(f))

# Count matches
for seq in alignment_sequences:
    alignment_sequences[seq]['count'] = count_matches(seq, csv_reader)

# Write results to output file
with open('alignment_matches.txt', 'w') as out_file:
    for seq, data in alignment_sequences.items():
        for _ in range(data['occurrences']):
            out_file.write(f"Sequence: {seq}\tMatches: {data['count']}\n")

print("Results have been written to alignment_matches.txt")

