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
