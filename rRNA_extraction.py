from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os
import pandas as pd


def read_annotation_file(file_path):
    """Read the annotation Excel file and return lists of annotations."""
    annotations = pd.read_excel(file_path)
    return (
        annotations["PN"].tolist(),
        annotations["SPEC"].tolist(),
        annotations["5S1FROM"].tolist(),
        annotations["5STO"].tolist(),
        annotations["23SFROM"].tolist(),
        annotations["23STO"].tolist(),
        annotations["16SFROM"].tolist(),
        annotations["16STO"].tolist()
    )


def extract_rRNA_region(sequence, indices):
    """Extract rRNA regions based on provided indices."""
    S51FROM, S5TO, S23SFROM, S23STO, S16SFROM, S16STO = indices
    rRNA_regions = []

    if S51FROM != 0 and S5TO != 0:
        rRNA_regions.append(sequence[S51FROM:S5TO])
    if S23SFROM != 0 and S23STO != 0:
        rRNA_regions.append(sequence[S23SFROM:S23STO])
    if S16SFROM != 0 and S16STO != 0:
        rRNA_regions.append(sequence[S16SFROM:S16STO])

    return ''.join(rRNA_regions)


def process_sequences(annotation_info, path):
    """Process sequences from files and extract rRNA regions."""
    ALL_rRNA = []
    for i in range(len(annotation_info[0])):
        spec = annotation_info[1][i]
        path_ofsequence = os.path.join(path, f"{spec}.fasta")

        try:
            sequences = SeqIO.parse(path_ofsequence, 'fasta')
            for sequence in sequences:
                rRNA_region = extract_rRNA_region(str(sequence.seq), (annotation_info[2][i], annotation_info[3][i],
                                                                      annotation_info[4][i], annotation_info[5][i],
                                                                      annotation_info[6][i], annotation_info[7][i]))
                rRNA = Seq(rRNA_region)
                ALL_rRNA.append(SeqRecord(seq=rRNA, id=sequence.name))
        except FileNotFoundError:
            print(f"File not found: {path_ofsequence}")
    return ALL_rRNA


# Main execution
path = "F:/Data set of Mycobacterial"
annotation_file = 'annotation_sequence.xlsx'

annotation_info = read_annotation_file(annotation_file)
all_rRNA_records = process_sequences(annotation_info, path)

SeqIO.write(all_rRNA_records, "rRNAsequence.fasta", 'fasta')
print(f"Total rRNA records extracted: {len(all_rRNA_records)}")
