#!/usr/bin/env python
# count_aip_kmers.py
import re
import os
fastq = open('/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq','r')
aip_kmers = open("aip_kmers.txt",'w')
#Assign an empty string variable to contain the stripped data. 
line = ' '
#Specify the kmer length, in this case, 6. 
kmer_length = 6
#Assign an empty dictionary to contain the enteri kmer data. 
kmer_dictionary = {}
#Initiate while loop to extract sequence containing only ATGC characters.
while line:
      line = fastq.readline()
      line = line.rstrip(os.linesep)
      if re.match('^[ATGCN]+$', line):
          seq = line
          stop = len(seq) - kmer_length + 1
#Specify the start and stop range for the program to read and print all the possible 6-mers in the sequence. 
#This would also exclude all the other lower mers from being added to the kmer dictionary.           
	  for start in range(0, stop):
              kmer = seq[start:start + kmer_length]
              if kmer in kmer_dictionary:
                 kmer_dictionary[kmer] += 1
              else:
                 kmer_dictionary[kmer] = 1
#Assign a variable for the tab separation between the 6-mer and the count of the corresponding 6-mer
separate = "\t"

for kmer in kmer_dictionary:
   kmer_count = kmer_dictionary[kmer]
   out_file = (kmer, str(kmer_count))
   print(separate.join(out_file))
   aip_kmers.write(separate.join(out_file) + "\n")
fastq.close()
aip_kmers.close()  
