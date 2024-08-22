
import pandas as pd
from Bio import SeqIO

# Function to extract sequence from FASTA file
def extract_sequence(fasta_file, chromosome, start, end):
    for record in SeqIO.parse(fasta_file, "fasta"):
        if record.id == chromosome:
            return record.seq[start-1:end]

# Read the CSV file
df = pd.read_csv("LTR2B.csv")

# Path to the FASTA file
fasta_file = "hg38.fa"

# Create an empty DataFrame to store results
new_df = pd.DataFrame(columns=["Chromosomes", "Query begin", "Query end", "Strand", "Repeat ID", "Sequence"])

# Iterate over rows of the DataFrame
for index, row in df.iterrows():
    chromosome = row["Chromosomes"]
    start = row["Query begin"]
    end = row["Query end"]
    strand = row["Strand"]
    repeat_id = row["Repeat ID"]
    
    # Extract sequence
    sequence = extract_sequence(fasta_file, chromosome, start, end)
    
    # Append to the new DataFrame
    new_df = pd.concat([new_df, pd.DataFrame({"Chromosomes": [chromosome], 
                                               "Query begin": [start], 
                                               "Query end": [end], 
                                               "Strand": [strand], 
                                               "Repeat ID": [repeat_id], 
                                               "Sequence": [sequence]})], ignore_index=True)

# Write the new DataFrame to a new CSV file
new_df.to_csv("LTR2B_Seq.csv", index=False)
