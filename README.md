# ProteinFold Mini

A Python command-line tool for small-scale protein structure analysis, combining sequence validation, structure retrieval, ESMFold-based prediction, and dissertation-linked annotation for Rh50 from *Nitrosomonas europaea*.

## What it does

ProteinFold Mini accepts a protein FASTA sequence and supports two main workflows:

- Fetch a known experimental structure from the RCSB Protein Data Bank
- Predict a structure from sequence using an ESMFold-style API

It also includes a special **Rh50 mode** based on my MSc dissertation work on bacterial ammonium transport, highlighting important residues involved in the NeRh50 transport pathway.

## Why I built this

I built this project to strengthen my structural bioinformatics and Python skills after completing my MSc in 2023.

The project is inspired by my dissertation on the Rh50 protein from *Nitrosomonas europaea*, where I investigated ammonium transport and the importance of key residues such as E146. This repository extends that work into a computational setting by linking protein sequence input to structure retrieval, prediction, and residue-level annotation.

## Features

- Protein FASTA input parsing
- Protein sequence validation
- Experimental structure download from RCSB PDB
- ESMFold-based sequence-to-structure prediction
- JSON report generation
- Rh50-specific annotation mode for dissertation-linked residues
- Output of PDB structure files for downstream visualization

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Orcinus9/proteinfold-mini.git
cd proteinfold-mini
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Dependencies

- Biopython
- requests

## Project structure

```text
proteinfold-mini/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── sample_data/
│   ├── rh50_wt.fasta
│   └── rh50_e146q.fasta
├── output/
└── proteinfold_mini/
    ├── __init__.py
    ├── cli.py
    ├── fasta_utils.py
    ├── validators.py
    ├── structure_fetch.py
    ├── predict.py
    ├── report.py
    └── rh50_annotations.py
```

## Example usage

### Fetch an experimental Rh50 structure from the PDB

```bash
python main.py sample_data/rh50_wt.fasta --fetch-pdb 3B9W --rh50-mode --report output/rh50_report.json
```

### Predict a structure from sequence using ESMFold mode

```bash
python main.py sample_data/rh50_wt.fasta --esmfold --rh50-mode --report output/rh50_esmfold_report.json
```

## Example outputs

The tool can generate:

- `.pdb` structure files
- `.json` summary reports

Example output files include:

- `output/3b9w.pdb`
- `output/rh50_report.json`
- `output/NeRh50_WT_example_esmfold.pdb`
- `output/rh50_esmfold_report.json`
The JSON report includes a confidence_summary section computed from the PDB B-factor column:

- num_atoms_with_confidence
- mean_confidence
- min_confidence
- max_confidence
- confidence_note (scale interpretation)
## Rh50 dissertation link

This project is directly inspired by my MSc dissertation:

**Selective bacterial ammonium transport: an exploration of biological mechanism**

The dissertation focused on the Rh50 protein from *Nitrosomonas europaea*, including ammonium transport activity, selectivity, and the importance of E146 in the transport mechanism. In this tool, Rh50 mode provides a simple structural-bioinformatics extension of that work by annotating key residues relevant to the transport pathway.

## Skills demonstrated

- Python programming
- Command-line bioinformatics tool development
- FASTA parsing
- Protein sequence validation
- Structural bioinformatics workflow design
- API-based scientific data retrieval
- Protein structure file handling
- Research-to-code translation
- Git and GitHub version control

## Future improvements

- Add interactive 3D structure visualization
- Add mutation comparison mode for wild-type vs mutant sequences
- Add pLDDT confidence extraction where available
- Add support for additional prediction backends
- Export HTML reports with residue summaries