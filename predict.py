import os
import requests

def predict_structure_esmfold(sequence, output_dir="output", output_name="predicted_structure.pdb"):
    url = "https://api.esmatlas.com/foldSequence/v1/pdb/"
    headers = {
        "Content-Type": "text/plain"
    }

    response = requests.post(url, headers=headers, data=sequence, timeout=120)
    response.raise_for_status()

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, output_name)

    with open(output_file, "w") as f:
        f.write(response.text)

    return output_file