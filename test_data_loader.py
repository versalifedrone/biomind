#https://stanford.edu/~shervine/blog/pytorch-how-to-generate-data-parallel
import sys
import torch
from torch.utils import data
import numpy as np


RNA_DICT = {'A': 0, 'T': 1, 'C': 2, 'G': 3, 'N': 4, '-': 6}

def sparse_encode(seq, rna_dict):
    """For a given nucleotide sequence, return a sequence with each nucleotide encoded as a one hot vector"""
    enc_seq = np.zeros([len(seq),len(RNA_DICT)])
    for i, nuc in enumerate(seq):
        enc_seq[i, rna_dict[nuc]] = 1
    return enc_seq

VAL = "data/val_filtered.txt"
TRAIN = "data/train_filtered.txt"

partition = {'train':[], 'validation':[]}
labels = {}
sequences = {}
index = 0

############ LOAD DATA SET 

with open(VAL, 'r') as fIn : 
    for line in fIn : 
        #manage seq id 
        seq_id = "id_"+str(index)
        index +=1

        #read line in file 
        seq = line.replace(" ", "").strip().split(",")
        seq[0] = seq[0][:10]

        #encode sequence
        encod_seq = sparse_encode(seq[0], RNA_DICT)

        #store data
        partition['validation'].append(seq_id)
        labels[seq_id]=int(seq[1])
        sequences[seq_id] = encod_seq


with open(VAL, 'r') as fIn : 
    for line in fIn : 
        #manage seq id 
        seq_id = "id_"+str(index)
        index +=1

        #read line in file 
        seq = line.replace(" ", "").strip().split(",")
        seq[0] = seq[0][:10]

        #encode sequence
        encod_seq = sparse_encode(seq[0], RNA_DICT)

        #store data
        partition['train'].append(seq_id)
        labels[seq_id]=int(seq[1])
        sequences[seq_id] = encod_seq


list_IDs = partition['train'] + partition['validation']


############ Create data loader

class Dataset(data.Dataset):
  'Characterizes a dataset for PyTorch'
  def __init__(self, list_IDs, labels, sequences):
        'Initialization'
        self.labels = labels
        self.list_IDs = list_IDs
        self.sequences = sequences

  def __len__(self):
        'Denotes the total number of samples'
        return len(self.list_IDs)

  def __getitem__(self, index):
        'Generates one sample of data'
        # Select sample
        ID = self.list_IDs[index]

        # Load data and get label
        X = self.sequences[ID]
        Y = self.labels[ID]

        return X, Y


# CUDA for PyTorch
use_cuda = torch.cuda.is_available()
device = torch.device("cuda:0" if use_cuda else "cpu")

# Parameters
params = {'batch_size': 64,
          'shuffle': True,
          'num_workers': 6}
max_epochs = 100

training_set = Dataset(partition['train'], labels, sequences)
training_generator = data.DataLoader(training_set, **params)

validation_set = Dataset(partition['validation'], labels, sequences)
validation_generator = data.DataLoader(validation_set, **params)

for epoch in range(max_epochs):
    # Training
    for local_batch, local_labels in training_generator:
        # Transfer to GPU
        local_batch, local_labels = local_batch.to(device), local_labels.to(device)

        # Model computations


    # Validation
    with torch.set_grad_enabled(False):
        for local_batch, local_labels in validation_generator:
            # Transfer to GPU
            local_batch, local_labels = local_batch.to(device), local_labels.to(device)

            # Model computations
