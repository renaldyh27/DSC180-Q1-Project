import pandas as pd

def read_fungi_data(path):
    dataset = pd.read_csv(path, sep='\t',header=0, index_col='sampleid')
    return dataset

def read_tcga_abbrev(path):
    return pd.read_csv(path, index_col='dz')