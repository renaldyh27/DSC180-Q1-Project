import pandas as pd

def filter_sample_type(fungi_metadata, sample_type):
    min_count = 20
    fungi_metadata_cols = ['disease_type','sample_type'] 
    
    # grab needed columns
    fungi_metadata = fungi_metadata[fungi_metadata_cols] 
    
    #filter by given sample_type
    fungi_metadata = fungi_metadata[fungi_metadata['sample_type'] == sample_type]

    # drop cancers with fewer than 20 samples
    fungi_metadata = fungi_metadata[fungi_metadata['disease_type'].map(
        fungi_metadata['disease_type'].value_counts()) > min_count]
    
    return fungi_metadata
    
def relevant_feature_data(fungi_metadata, feature_table):
    # filter feature tables for relevant samples
    return feature_table.filter(items = fungi_metadata.index, axis = 0)

def disease_type_count(fungi_metadata):
    # one hot encode disease types
    return pd.get_dummies(fungi_metadata['disease_type'])
