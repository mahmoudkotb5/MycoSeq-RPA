# rRNA Extraction Script

This script extracts rRNA regions from genomic sequences based on annotation data.

## Requirements

- Python 3.6+
- Biopython
- pandas
- openpyxl

## Installation

1. Clone this repository:
   
   git clone https://github.com/mahmoudkotb5/MycoSeq-RPA.git


2. Navigate to the project directory:

   cd MycoSeq-RPA
 

3. Install the required packages:

   pip install -r requirements.txt
 

## Usage

1. Place your annotation Excel file and FASTA sequence files in the same directory as the script.

2. Update the `path` and `annotation_file_name` variables in the script if necessary.

3. Run the script:
 
   python rRNA_extraction.py


The script will generate a file named "73rRNA.fasta" containing the extracted rRNA sequences.


# Getting primers and enzymes Script

This tool performs DNA analysis using primers and restriction enzymes. It can be used both interactively through a Jupyter notebook and as a command-line application.

## Requirements

- Python 3.8 or higher
- Required Python packages:
  - jupyter
  - numpy
  - pandas
  - biopython
  - openpyxl
  - matplotlib

## Installation

1. Clone the repository:

   git clone [https://github.com/your-username/dna-analysis-tool.git](https://github.com/mahmoudkotb5/MycoSeq-RPA.git)



2. Install the required packages:
 
   pip install -r requirements.txt


## Usage
### Command-line Application

To use the tool from the command line:


python  getting_primer_enzymes.py <primers_file> <sequences_file> <output_file>


- `<primers_file>`: Path to the Excel file containing primers (e.g., CONSERVE_REGION.xlsx)
- `<sequences_file>`: Path to the FASTA file containing sequences (e.g., rRNAsequence.fasta)
- `<output_file>`: Path for the output Excel file with results (e.g., Primers_enzyme_results.xlsx)

Example:

python dna_analysis_tool.py CONSERVE_REGION.xlsx rRNAsequence.fasta Primers_enzyme_results.xlsx



