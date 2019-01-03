# RNA sub-cellular localization with fast-training Quasi-Recurrent Neural Networks

This repo contains the code and the report of a final project for the course '**02456 Deep Learning**' held at **DTU** - Technical University of Denmark, Lyngby, by professor Ole Winther.  
*Authors of the project:* Alessandro Montemurro, DTU Compute; Léa Riera, ; Niels, DTU Bioinformatics  
*Supervisors:* Alexander R. Johansen; Josè  
 
 
The subcellular localization of produced RNA molecules is often of interest in biological research, as misplaced RNA can,  for  example,  lead  to  neurological  disease  in  humans.  
A  novel  networktype,  **Quasi-Recurrent Neural Networks (QRNNs)** are used. QRNNs embrace the benefits of both convolutional and recurrent neural networks alike.  
A basic QRNN was benchmarked against a similar LSTMin a simple two-class problem, reaching a higher accuracy and training more than 10 times faster at the same batch size.  Inthe full six-class problem, a complex QRNN model reached an accuracy  of  44.5%,  beating  the  largest-class  baseline  of 37.6%
