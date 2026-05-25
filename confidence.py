def extract_bfactors_from_pdb(pdb_file):
    bfactors = []

    with open(pdb_file, "r") as f:
        for line in f:
            if line.startswith("ATOM"):
                try:
                    bfactor = float(line[60:66].strip())
                    bfactors.append(bfactor)
                except ValueError:
                    continue

    return bfactors


def summarize_confidence(bfactors):
    if not bfactors:
        return {
            "num_atoms_with_confidence": 0,
            "mean_confidence": None,
            "min_confidence": None,
            "max_confidence": None,
            "confidence_note": "No confidence values found in PDB file."
        }

    mean_conf = round(sum(bfactors) / len(bfactors), 2)
    min_conf = round(min(bfactors), 2)
    max_conf = round(max(bfactors), 2)

    if max_conf <= 1.0:
        scale_note = "Confidence values appear to be on a 0 to 1 scale."
    else:
        scale_note = "Confidence values appear to be on a 0 to 100 pLDDT-like scale."

    return {
        "num_atoms_with_confidence": len(bfactors),
        "mean_confidence": mean_conf,
        "min_confidence": min_conf,
        "max_confidence": max_conf,
        "confidence_note": scale_note
    }