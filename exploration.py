import matplotlib.pyplot as plt
import numpy as np  
import sys

#Files data 
VAL = "data/val.rna.txt"
TRAIN = "data/train.rna.txt"
TEST = "data/test.rna.txt"

loc = {0: "Nucleus",1: "Cytoplasm", 2: "Secreted", 3: "Ribosome", 4: "Endoplasmic\nreticulum", 5: "Mitochondrion"}

def extract_stat(file_name):
    """ Extract information from a data file"""
    sequences = []
    lengths = []
    categories = []

    with open(file_name, 'r') as fIn : 
        for line in fIn :
            splited_line = line.strip().split(',')
            sequences.append(splited_line[0])
            categories.append(loc[int(splited_line[1])] )
            lengths.append(len(splited_line[0]))
            
    return(sequences, lengths, categories)



def sequences_present_several_times(file_name):
    seq,leng,cat = extract_stat(file_name)
    print("total number " + str(len(seq)), "unique" +str(len(set(seq))))
    uniques = list(set(seq))
    notuniques = [i for i in seq if seq.count(i)>1]
    for u in notuniques : 
        print(u)
        pos = [i for i in range(len(seq)) if seq[i]==u]
        print([cat[i] for i in pos])

def compute_size_data_set(file_names):
    nbr_rna_seq = 0
    for f in file_names :
        seq,leng,cat = extract_stat(f)
        nbr_rna_seq += len(seq)
    print(nbr_rna_seq)

# compute_size_data_set([TRAIN, VAL, TEST])
# sys.exit()

def sequence_length_plot(file_name):
    seq,leng,cat = extract_stat(file_name)
    n, bins, patches = plt.hist(x=leng, bins='sturges', color='#0504aa',
                                alpha=0.7, rwidth=0.85, histtype = 'barstacked')
    plt.xlabel('Sequence length', fontsize=18)
    plt.ylabel('Frequency', fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=14)

def RNA_destination_plot(file_name):
    seq,leng,cat = extract_stat(file_name)
    n, bins, patches = plt.hist(x=cat, bins='auto', color='#0504aa',
                                alpha=0.7)
    plt.xlabel('Sequence destination', fontsize=18)
    plt.ylabel('Frequency', fontsize=18)
    plt.xticks(rotation=30, fontsize=11)
    plt.yticks(fontsize=14)


plt.subplot(211)
sequence_length_plot(TRAIN)
plt.subplot(212)
RNA_destination_plot(TRAIN)

plt.show()