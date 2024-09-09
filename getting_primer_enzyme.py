from Bio.Seq import Seq
from Bio.Restriction import *
import matplotlib.pyplot as plt
import os,psutil
from Bio import  SeqIO
import  numpy as np
import pandas as pd
import openpyxl

# create a new workbook and select the Sheet1 worksheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Sheet1"

dataa = []
strrrr=""
# read by default 1st sheet of an excel file
x = []
# Define a list of colors to use for each point
import numpy as np
Enzyme_list=[]
max_score=[]
total_cutting_list=[]

def subtract_lists(list1, list2):
    return [abs(list1[i] - list2[i]) for i in range(len(list1))]

def check_greater_than_50(lst):
    for num in lst:
        if num >=50:
            return True
    return False
names_species=[]
max_score_for_each_enzyme=[]
# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('CONSERVE_REGION_66.xlsx')
primers=dataframe1["PN"].tolist()

numberr=1
for forward_primer in primers :

    for reversed_primer in primers:
        if forward_primer==reversed_primer:
            continue

        for restrication_enzyme in AllEnzymes:
              tb = 0
              sequences = SeqIO.parse("allMYCOBACTERIUM70.fasta", 'fasta')
              namespecies_theircuttinglist = {}
              all_cutting_list_pattern = []
              for sequence in sequences:

                   NAME, SEQUENCE = str(sequence.name), str(sequence.seq)

                   subsequence = SEQUENCE[SEQUENCE.index(str(forward_primer)):SEQUENCE.index(str(reversed_primer)) + len(str(reversed_primer))]
                   final_sequence=Seq(subsequence)

                   try:
                     cutting_Pattern = restrication_enzyme.catalyze(final_sequence)
                     print(cutting_Pattern)
                     if len(cutting_Pattern)<2:
                         break
                     sort_cutting_pattern = []
                     for pattern in cutting_Pattern:
                         if len(pattern) in sort_cutting_pattern :
                             continue
                         if len(pattern)>=50:
                            sort_cutting_pattern.append(len(pattern))
                     sort_cutting_pattern.sort()
                     namespecies_theircuttinglist[NAME]=sort_cutting_pattern
                     if sort_cutting_pattern !=[]:
                       all_cutting_list_pattern.append(sort_cutting_pattern)
                       names_species.append(NAME)
                   except:
                     pass
              if len(all_cutting_list_pattern)==66:
                  Enzyme_list.append(restrication_enzyme)
                  totla_number_of_pattern_for_all_sequnce=0
                  total = 0
                  index=0
                  for i in all_cutting_list_pattern:
                      nameofrrna=str(names_species[index])
                      #print(nameofrrna)
                      index = index + 1
                      for j in all_cutting_list_pattern:
                          if i == j:

                              continue
                          query_numbers = i
                          numbers = j
                          nearest_numbers = []
                          for query_number in query_numbers:
                              nearest_number = None
                              nearest_distance = float('inf')
                              for number in numbers:
                                  distance = abs(number - query_number)
                                  if distance < nearest_distance:
                                      nearest_number = number
                                      nearest_distance = distance
                              nearest_numbers.append(nearest_number)
                          sub = subtract_lists(query_numbers, nearest_numbers)

                          if check_greater_than_50(sub) == True:

                              total = total + 1




                      totla_number_of_pattern_for_all_sequnce = totla_number_of_pattern_for_all_sequnce + total
                      total = 0
                  if totla_number_of_pattern_for_all_sequnce>4200:
                     print(totla_number_of_pattern_for_all_sequnce)
                  if totla_number_of_pattern_for_all_sequnce>=4200:
                      length_btween_primer=len(final_sequence)
                      FILTER_PRIMER=[]
                      FILTER_PRIMER.append(forward_primer)
                      FILTER_PRIMER.append(reversed_primer)
                      FILTER_PRIMER.append(length_btween_primer)
                      FILTER_PRIMER.append(totla_number_of_pattern_for_all_sequnce)
                      differnation=float(float(totla_number_of_pattern_for_all_sequnce) / float(4290))
                      FILTER_PRIMER.append(differnation)
                      FILTER_PRIMER.append(str(restrication_enzyme))
                      dataa.append(FILTER_PRIMER)
                  max_score_for_each_enzyme.append(totla_number_of_pattern_for_all_sequnce)
                  sorted_dict = dict(sorted(namespecies_theircuttinglist.items(), key=lambda x: len(x[1])))
                  all_cutting_list_pattern.sort()
                  x = list(sorted_dict.keys())

        if max_score_for_each_enzyme !=[]:
           c=max(max_score_for_each_enzyme)
           max_score.append(c)
# Save the workbook
for row in dataa:
    ws.append(row)

# save the workbook to a file
wb.save("Primers_enzyme.xlsx")