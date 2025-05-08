#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from pandas import DataFrame
import glob
import os
import sys


def get_all_splice(ensg):

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

def save_data(df_dict):
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
        value.to_csv('../output/'+gene+'/'+gene+'_'+key+'.csv', index=True)


if len(sys.argv) < 2:
    print('ERROR: please specify Ensembl ID of gene')
    exit(1)
gene = str(sys.argv[1])
all_splice = get_all_splice(gene)
save_data(all_splice)

