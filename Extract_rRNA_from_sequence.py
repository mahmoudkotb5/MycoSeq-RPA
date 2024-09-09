
from Bio.Seq import Seq
import os,psutil
from Bio import  SeqIO
from Bio.Restriction import *
r=RestrictionBatch()
path = "F:/Data set of Mycobacterial"
path2 = "F:/Data set of Mycobacterial/"
dir_list = os.listdir(path)
# import pandas lib as pd
import pandas as pd

# read by default 1st sheet of an excel file
annoation_information = pd.read_excel('70_annotation_sequence.xlsx')
PN=annoation_information["PN"].tolist()
SPEC=annoation_information["SPEC"].tolist()
S51FROM=annoation_information["5S1FROM"].tolist()
S5TO=annoation_information["5STO"].tolist()
S23SFROM=annoation_information["23SFROM"].tolist()
S23STO=annoation_information["23STO"].tolist()
S16SFROM=annoation_information["16SFROM"].tolist()
S16STO=annoation_information["16STO"].tolist()
ALL_rRNA=[]
count=0
for i in  range(0,len(SPEC)):
      if count==3:
          break
      else:
          count=count+1

      path_ofsequence = path2 + str(SPEC[i]) + ".fasta"
      print(SPEC[i])
      sequeces = SeqIO.parse(path_ofsequence, 'fasta')
      for sequence in sequeces:

         NAME, SEQUENCE = str(sequence.name), str(sequence.seq)

         if PN[i]=="POSTIVE":
            if S51FROM[i]!=0 and S5TO[i]!= 0 :
                S5_region = SEQUENCE[S51FROM[i]:S5TO[i]]
                print(len(S5_region))
            if S23SFROM[i]!=0 and S23STO[i]!= 0 :
               S23_region = SEQUENCE[S23SFROM[i]:S23STO[i]]

            if S16SFROM[i]!=0 and S16STO[i]!= 0 :
               S16_region = SEQUENCE[S16SFROM[i]:S16STO[i]]
               print("16s"+S16_region)

               print(len(S16_region))
               is1=SEQUENCE[S16STO[i]:S23SFROM[i]]
               print("is1" + is1)
               is2=SEQUENCE[ S23STO[i]:S51FROM[i]]
               print("is2"+is2)

            rRNA_REGION= S16_region + is1 + S23_region + is2 + S5_region
            from Bio.SeqRecord import SeqRecord
            rRNA=Seq(rRNA_REGION)
            id=NAME
            s=NAME+".fasta"
            print(rRNA.index(S5_region))

            Sequence_record_rRNA = SeqRecord(seq=rRNA, id=id)
            ALL_rRNA.append(Sequence_record_rRNA)



         elif PN[i]=="NEGATIVE":

             SEQUENCE2= str(Seq(SEQUENCE).complement())
             if S51FROM[i] != 0 and S5TO[i] != 0:
                 S5_region = SEQUENCE2[S51FROM[i]:S5TO[i]]
                 S5_region= S5_region[::-1]
                 print(len(S5_region))
                 new_sequence = SEQUENCE
             if S23SFROM[i] != 0 and S23STO[i] != 0:
                 S23_region = SEQUENCE2[S23SFROM[i]:S23STO[i]]
                 S23_region = S23_region[::-1]

             if S16SFROM[i] != 0 and S16STO[i] != 0:
                 S16_region = SEQUENCE2[S16SFROM[i]:S16STO[i]]
                 S16_region = S16_region[::-1]
                 print(len(S16_region))




             is1 = SEQUENCE2[S23STO[i]:S16SFROM[i]]
             is1=is1[::-1]
             is2 = SEQUENCE2[S5TO[i]:S23SFROM[i]]
             is2 = is2[::-1]



             rRNA_REGION = S16_region + is1 + S23_region + is2 + S5_region
             com=rRNA_REGION
             from Bio.SeqRecord import SeqRecord

             rRNA = Seq(com)
             id = NAME
             s = NAME + ".fasta"
             print(rRNA.index(S5_region))
             Sequence_record_rRNA = SeqRecord(seq=rRNA, id=id)
             ALL_rRNA.append(Sequence_record_rRNA)


SeqIO.write(ALL_rRNA, "3SEQUENCE.fasta", 'fasta')
print(len(ALL_rRNA))


