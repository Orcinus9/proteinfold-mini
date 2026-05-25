VALID_AA = set("ACDEFGHIKLMNPQRSTVWY")

def validate_protein_sequence(sequence):
    sequence = sequence.strip().upper()
    if len(sequence) < 20:
        raise ValueError("Protein sequence is too short. Use at least 20 amino acids.")
    invalid = sorted(set(sequence) - VALID_AA)
    if invalid:
        raise ValueError(f"Invalid amino acid characters found: {', '.join(invalid)}")
    return sequence