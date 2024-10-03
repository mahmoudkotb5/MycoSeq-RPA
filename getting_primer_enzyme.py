import time
from Bio.Seq import Seq
from Bio.Restriction import AllEnzymes
from Bio import SeqIO
import pandas as pd
import openpyxl

def subtract_lists(list1, list2):
    return [abs(list1[i] - list2[i]) for i in range(len(list1))]

def check_greater_than_50(lst):
    return any(num >= 50 for num in lst)

def find_nearest_numbers(query_numbers, numbers):
    nearest_numbers = []
    for query_number in query_numbers:
        nearest_number = min(numbers, key=lambda x: abs(x - query_number))
        nearest_numbers.append(nearest_number)
    return nearest_numbers

def analyze_sequence(sequence, forward_primer, reversed_primer, restriction_enzyme):
    NAME, SEQUENCE = str(sequence.name), str(sequence.seq)
    subsequence = SEQUENCE[SEQUENCE.index(str(forward_primer)):SEQUENCE.index(str(reversed_primer)) + len(str(reversed_primer))]
    final_sequence = Seq(subsequence)

    try:
        cutting_Pattern = restriction_enzyme.catalyze(final_sequence)
        if len(cutting_Pattern) < 2:
            return None

        sort_cutting_pattern = sorted(set(len(pattern) for pattern in cutting_Pattern if len(pattern) >= 50))
        return NAME, sort_cutting_pattern
    except:
        return None

def calculate_total_difference(all_cutting_list_pattern):
    total = 0
    for i, query_numbers in enumerate(all_cutting_list_pattern):
        for j, numbers in enumerate(all_cutting_list_pattern):
            if i == j:
                continue
            nearest_numbers = find_nearest_numbers(query_numbers, numbers)
            sub = subtract_lists(query_numbers, nearest_numbers)
            if check_greater_than_50(sub):
                total += 1
    return total

def analyze_primers_and_enzymes(primers, sequences_file, output_file):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    data = []
    max_score = []
    
    start_time = time.time()
    
    for forward_primer in primers:
        for reversed_primer in primers:
            if forward_primer == reversed_primer:
                continue

            for restriction_enzyme in AllEnzymes:
                sequences = SeqIO.parse(sequences_file, 'fasta')
                all_cutting_list_pattern = []
                names_species = []

                for sequence in sequences:
                    result = analyze_sequence(sequence, forward_primer, reversed_primer, restriction_enzyme)
                    if result:
                        name, sort_cutting_pattern = result
                        if sort_cutting_pattern:
                            all_cutting_list_pattern.append(sort_cutting_pattern)
                            names_species.append(name)

                if len(all_cutting_list_pattern) == 66:
                    total_difference = calculate_total_difference(all_cutting_list_pattern)
                    
                    if total_difference >= 4200:
                        length_between_primer = len(Seq(sequence.seq[sequence.seq.index(str(forward_primer)):sequence.seq.index(str(reversed_primer)) + len(str(reversed_primer))]))
                        differentiation = float(total_difference) / 4290
                        
                        filter_primer = [
                            forward_primer,
                            reversed_primer,
                            length_between_primer,
                            total_difference,
                            differentiation,
                            str(restriction_enzyme)
                        ]
                        data.append(filter_primer)
                    
                    max_score.append(total_difference)

    for row in data:
        ws.append(row)
    
    wb.save(output_file)
    
    end_time = time.time()
    print(f"Time taken to complete: {end_time - start_time:.6f} seconds")

# Main execution
if __name__ == "__main__":
    dataframe1 = pd.read_excel('CONSERVE_REGION.xlsx')
    primers = dataframe1["PN"].tolist()
    analyze_primers_and_enzymes(primers, "rRNAsequence.fasta", "Primers_enzyme.xlsx")
