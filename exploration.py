import matplotlib.pyplot as plt
import numpy as np  

#Files data 
VAL = "val.rna.txt"
TRAIN = "train.rna.txt"
TEST = "test.rna.txt"

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


def sequence_length_plot(file_name):
    seq,leng,cat = extract_stat(file_name)
    n, bins, patches = plt.hist(x=leng, bins='auto', color='#0504aa',
                                alpha=0.7, rwidth=0.85)
    plt.xlabel('Sequence length')
    plt.ylabel('Frequency')

def RNA_destination_plot(file_name):
    seq,leng,cat = extract_stat(file_name)
    n, bins, patches = plt.hist(x=cat, bins='auto', color='#0504aa',
                                alpha=0.7, rwidth=10)
    plt.xlabel('Sequence length')
    plt.ylabel('Frequency')
    plt.xticks(rotation=30)

plt.subplot(121)
sequence_length_plot(TRAIN)
plt.subplot(122)
RNA_destination_plot(TRAIN)

plt.show()