import pandas as pd

def filter_sample_type(fungi_metadata, sample_type, outfile_metadata):
    '''Filter metadata by sample type'''
    min_count = 20
    fungi_metadata_cols = ['disease_type','sample_type'] 
    
    # grab needed columns
    fungi_metadata = fungi_metadata[fungi_metadata_cols] 
    
    #filter by given sample_type
    fungi_metadata = fungi_metadata[fungi_metadata['sample_type'] == sample_type]

    # drop cancers with fewer than 20 samples
    fungi_metadata = fungi_metadata[fungi_metadata['disease_type'].map(
        fungi_metadata['disease_type'].value_counts()) > min_count]
    
    fungi_metadata.to_csv(outfile_metadata, sep="\t", index=False)
    
    return fungi_metadata
 
def disease_type_count(fungi_metadata):
    '''One hot encode disease_type'''
    return pd.get_dummies(fungi_metadata['disease_type']) 
    
def relevant_feature_data(fungi_metadata, feature_table, feature_table_name):
    '''Filter feature tables for relevant samples '''
    df = feature_table.filter(items = fungi_metadata.index, axis = 0)
    df.to_csv("data/temp/" + feature_table_name + "_filtered_samples",sep='\t',index=False)
    return df

def relevant_feature_table_samples(fungi_metadata, datasets):
    '''Filter all feature tables for relevant samples'''
    dataset_names = ["high_coverage","WIS_intersect","decontaminated"]
    return map(lambda feature_table, feature_table_name: 
        relevant_feature_data(fungi_metadata, feature_table, feature_table_name), datasets, dataset_names)