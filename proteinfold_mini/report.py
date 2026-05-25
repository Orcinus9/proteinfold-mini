import json
import os
from proteinfold_mini.rh50_annotations import RH50_KEY_RESIDUES

def write_report(report_data, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(report_data, f, indent=2)

def build_rh50_report(sequence_id, sequence, pdb_id=None, pdb_file=None, rcsb_title=None):
    return {
        "project": "ProteinFold Mini",
        "mode": "rh50_example",
        "sequence_id": sequence_id,
        "sequence_length": len(sequence),
        "pdb_id": pdb_id,
        "pdb_file": pdb_file,
        "rcsb_title": rcsb_title,
        "key_residues": RH50_KEY_RESIDUES,
        "biological_context": "Based on MSc dissertation work on Nitrosomonas europaea Rh50 ammonium transport."
    }