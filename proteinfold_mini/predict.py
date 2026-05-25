import os
import requests

def predict_structure_esmfold(sequence, output_dir="output", output_name="predicted_structure.pdb"):
    url = "https://api.esmatlas.com/foldSequence/v1/pdb/"
    headers = {
        "Content-Type": "text/plain"
    }

    try:
        response = requests.post(url, headers=headers, data=sequence, timeout=120)
        response.raise_for_status()

        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, output_name)

        with open(output_file, "w") as f:
            f.write(response.text)

        return {
            "success": True,
            "pdb_file": output_file,
            "error": None
        }

    except requests.exceptions.SSLError as e:
        return {
            "success": False,
            "pdb_file": None,
            "error": f"SSL error while contacting ESMFold endpoint: {str(e)}"
        }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "pdb_file": None,
            "error": f"Request failed while contacting ESMFold endpoint: {str(e)}"
        }