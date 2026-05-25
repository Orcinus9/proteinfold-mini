from Bio import SeqIO

def read_first_fasta(filepath):
    records = list(SeqIO.parse(filepath, "fasta"))
    if not records:
        raise ValueError("No FASTA records found.")
    record = records[0]
    return record.id, str(record.seq)