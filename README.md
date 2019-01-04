# RNA sub-cellular localization with fast-training Quasi-Recurrent Neural Networks

This repo contains the code and the report of a final project for the course '**02456 Deep Learning**' held at **DTU** - Technical University of Denmark, Lyngby, by professor Ole Winther.  

### Authors
- Alessandro Montemurro, DTU Compute
- Léa Riera, DTU Compute
- Niels Mølgaard Knudsen DTU Bioengineering  

### Supervisors
- Alexander Rosenberg Johansen
- José Armenteros
 
 
### Description
**Quasi-Recurrent Neural Networks (QRNNs)** are used for the RNA sub-cellular localization (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5210605/).  
QRNNs embrace the benefits of both convolutional and recurrent neural networks alike. QRNNs beat other networks such as LSTM in both accuracy and speed.  

A description of QRNNs can be found in https://arxiv.org/abs/1611.01576. The PyTorch implementation follows https://github.com/salesforce/pytorch-qrnn.

### Running
Note: we are currently in the process of making a pretrained network for loading. 
1. Install Python package requirements from requirements.txt
2. Run notebook QRNN-train.ipynb
