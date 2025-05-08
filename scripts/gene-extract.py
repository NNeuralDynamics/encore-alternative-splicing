#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from pandas import DataFrame
import glob
import os
import sys


def get_all_splice(ensg):
    ''' a function to load the rMATS data from the ../data directory and extract the specified gene
        argument:
            ensg: the Ensembl ID for the gene
        returns:
            df_as: a dictionary of datasets pertaining to the gene specified. Schema:
            { cell_line:
                rbp:
                    splice_type: dataframe containing the extracted alternative splicing data
            }
    '''
    rbp_list = dict()

    for cl in ['HepG2', 'K562']:
        rbp_list[cl] = dict()
        for elem in glob.glob('../data/rMATS/*'+cl):
            rbp_list[cl][elem.split('/')[-1].split('-')[0]] = elem.split('/')[-1]

    df_as = dict()
    for cl in ['HepG2', 'K562']:
        df_as[cl] = dict()
        for rbp, path in rbp_list[cl].items():
            df_as[cl][rbp] = dict()
            for spl in ['SE', 'MXE', 'A5SS', 'A3SS', 'RI']:
                df = pd.read_csv('../data/rMATS/'+path+'/'+spl+'.MATS.JC.txt', sep='\t')
                df = df[df.GeneID.str.contains(ensg)]
                df['cell_line'] = cl
                df['RBP'] = rbp
                df['alt_splice_type'] = spl
                if not df.empty: df_as[cl][rbp][spl] = df
    return df_as

def save_data(df_dict, gene):
    ''' a function to save the data extracted to the ../output folder
        argument:
            df_dict: the dictionary of data frame passed by the get_all_splice function
    '''
    df_list = dict()
    for spl in ['SE', 'MXE', 'A5SS', 'A3SS', 'RI']: df_list[spl] = list()
    df_all = dict()
    for key0, value0 in df_dict.items():
        for key1, value1 in value0.items():
            for key2, value2 in value1.items():
                df_list[key2].append(value2)
    for spl in ['SE', 'MXE', 'A5SS', 'A3SS', 'RI']: 
        if len(df_list[spl]) != 0: df_all[spl] = pd.concat(df_list[spl]) 

    os.makedirs('../output/'+gene, exist_ok=True)
    for key, value in df_all.items():
        value.reset_index(drop=True).to_csv('../output/'+gene+'/'+gene+'_'+key+'.csv', index=True)


def main(argv):
    if len(sys.argv) < 2:
        print('ERROR: please specify Ensembl ID of gene')
        exit(1)
    gene = str(argv[1])
    all_splice = get_all_splice(gene)
    save_data(all_splice, gene)


if __name__ == "__main__":
    main(sys.argv)