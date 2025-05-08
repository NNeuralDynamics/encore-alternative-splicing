#!/bin/bash

# shRNA processed data (04/19/2024). Specs:
## batch-uncorrected
## rMATS v 4.2.0
## STAR v2.7.11a
## genome index and GTF from ENCODE (GRCH38 v29)
## all RBPs available as of 03/24/2024 (460 in total)

wget http://129.10.224.71/~apaul/data/rmats/04-2024/rmats-04-2024-1.tar.gz
tar zxvf rmats-04-2024-1.tar.gz
