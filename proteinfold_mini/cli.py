import argparse
from proteinfold_mini.fasta_utils import read_first_fasta
from proteinfold_mini.validators import validate_protein_sequence
from proteinfold_mini.structure_fetch import download_pdb_structure, fetch_rcsb_entry_json
from proteinfold_mini.predict import predict_structure_esmfold
from proteinfold_mini.report import build_rh50_report, write_report
from proteinfold_mini.confidence import extract_bfactors_from_pdb, summarize_confidence

def main():
    parser = argparse.ArgumentParser(description="ProteinFold Mini")
    parser.add_argument("input", help="Input FASTA file")
    parser.add_argument("--fetch-pdb", help="Fetch known structure from RCSB PDB, e.g. 3B9W")
    parser.add_argument("--esmfold", action="store_true", help="Predict structure from sequence using ESMFold-style API")
    parser.add_argument("--report", help="Write JSON report, e.g. output/report.json")
    parser.add_argument("--rh50-mode", action="store_true", help="Annotate report using Rh50 dissertation residues")

    args = parser.parse_args()

    sequence_id, sequence = read_first_fasta(args.input)
    sequence = validate_protein_sequence(sequence)

    pdb_file = None
    rcsb_title = None
    mode = "basic"
    confidence_summary = None
    prediction_error = None

    if args.fetch_pdb:
        pdb_file = download_pdb_structure(args.fetch_pdb)
        entry = fetch_rcsb_entry_json(args.fetch_pdb)
        rcsb_title = entry.get("struct", {}).get("title")
        mode = "fetch_pdb"

    elif args.esmfold:
        prediction_result = predict_structure_esmfold(
            sequence,
            output_dir="output",
            output_name=f"{sequence_id}_esmfold.pdb"
        )
        mode = "esmfold_prediction"
        pdb_file = prediction_result["pdb_file"]
        prediction_error = prediction_result["error"]

    if pdb_file:
        bfactors = extract_bfactors_from_pdb(pdb_file)
        confidence_summary = summarize_confidence(bfactors)

    if args.rh50_mode:
        report = build_rh50_report(
            sequence_id=sequence_id,
            sequence=sequence,
            pdb_id=args.fetch_pdb,
            pdb_file=pdb_file,
            rcsb_title=rcsb_title
        )
        report["mode"] = mode
        report["confidence_summary"] = confidence_summary
        report["prediction_error"] = prediction_error
    else:
        report = {
            "project": "ProteinFold Mini",
            "mode": mode,
            "sequence_id": sequence_id,
            "sequence_length": len(sequence),
            "pdb_id": args.fetch_pdb,
            "pdb_file": pdb_file,
            "rcsb_title": rcsb_title,
            "confidence_summary": confidence_summary,
            "prediction_error": prediction_error
        }

    if args.report:
        write_report(report, args.report)
        print(f"Report written to: {args.report}")
        if pdb_file:
            print(f"Structure file written to: {pdb_file}")
        if confidence_summary:
            print(f"Mean confidence: {confidence_summary['mean_confidence']}")
        if prediction_error:
            print(f"Prediction warning: {prediction_error}")
    else:
        print(report)