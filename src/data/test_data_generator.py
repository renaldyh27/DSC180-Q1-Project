import pandas as pd
import numpy as np

#test data generator params
n_samples = 150

cancers = ['Lung Adenocarcinoma', 'Uterine Corpus Endometrial Carcinoma',
       'Breast Invasive Carcinoma', 'Bladder Urothelial Carcinoma',
       'Thyroid Carcinoma', 'Stomach Adenocarcinoma',
       'Head and Neck Squamous Cell Carcinoma'] #subset of all cancers in raw data

taxa_columns = ['Candida_glabrata', 'Candida_tropicalis', 'Debaryomyces_hansenii',
           'Schizophyllum_commune', 'Saccharomyces_cerevisiae',
           'Fusarium_oxysporum', 'Pyrenophora_tritici-repentis',
           'Malassezia_globosa', 'Candida_albicans', 'Torulaspora_delbrueckii',
           'Stereum_hirsutum', 'Coniosporium_apollinis', 'Trichosporon_asahii',
           'Agaricus_bisporus', 'Candida_orthopsilosis', 'Malassezia_sympodialis',
           'Cyphellophora_europaea', 'Wallemia_ichthyophaga',
           'Pseudozyma_hubeiensis', 'Bipolaris_zeicola'] #subset of all taxas in raw data

def generate_test_data(n_samples=n_samples):
    
    test_metadata = pd.DataFrame(np.random.choice(cancers,size=(n_samples, 1)), columns=['disease_type'])
    test_metadata['sampleid'] = np.arange(1, n_samples+1)
    test_metadata['sample_type'] = 'Primary Tumor'

    test_fungi_data = pd.DataFrame(np.random.randint(0, 300, size=(n_samples,len(taxa_columns))), columns=taxa_columns)
    test_fungi_data['sampleid'] = np.arange(1, n_samples+1)

    paths = ('test/test_metadata.tsv', 'test/test_fungi_data.tsv')
    
    test_metadata.to_csv(paths[0], sep="\t", index=False)
    test_fungi_data.to_csv(paths[1], sep="\t", index=False)
    
    return paths