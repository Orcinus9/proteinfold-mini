import os
import requests

def download_pdb_structure(pdb_id, output_dir="output"):
    pdb_id = pdb_id.lower()
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{pdb_id}.pdb")

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    with open(output_file, "w") as f:
        f.write(response.text)

    return output_file

def fetch_rcsb_entry_json(pdb_id):
    pdb_id = pdb_id.upper()
    url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()