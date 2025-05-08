# encore-alternative-splicing
Code for analyzing alternative splicing results from ENCORE


### directory structure
```
.
├── data
│   ├── get_rMATS_results_encore.sh
│   ├── rMATS                                 # run get_rMATS_results_encore.sh to get this folder
│   └── rmats-04-2024-1.tar.gz                # run get_rMATS_results_encore.sh to get this file
├── LICENSE
├── notebooks
│   └── gene-extract.ipynb                    # notebook for extracting all alternative splicing for a particular gene
├── output
│   └── ENSG00000090621                       # sample results for PABPC4
├── README.md
├── requirements.txt
└── scripts
    └── gene-extract.py                       # script for extracting all alternative splicing for a particular gene

```

### 1. get the data
```{sh}
cd data
sh get_rMATS_results_encore.sh
```

### 2. run the script
```{sh}
cd scripts
python gene-extract.py ENSG00000090621
```

output will be save to the ```output``` directory
