import pandas as pd

def filter_sample_type(fungi_metadata, sample_type):
    """Filter metadata by sample type

    Args:
        fungi_metadata (DataFrame): Dataframe of fungi metadata
        sample_type (String): Sample type that will be explored in analysis. ex. Primary Tumor, Blood Derived Normal

    Returns:
        DataFrame: Dataframe containing only samples of given sample_type
    """
    min_count = 20
    fungi_metadata_cols = ['disease_type','sample_type'] 
    
    # grab needed columns
    fungi_metadata = fungi_metadata[fungi_metadata_cols] 
    
    #filter by given sample_type
    fungi_metadata = fungi_metadata[fungi_metadata['sample_type'] == sample_type]

    # drop cancers with fewer than 20 samples
    fungi_metadata = fungi_metadata[fungi_metadata['disease_type'].map(
        fungi_metadata['disease_type'].value_counts()) > min_count]
    
    fungi_metadata.to_csv("data/temp/metadata_" + '_'.join(sample_type.lower().split()) + '.csv')
    
    return fungi_metadata
 
def disease_type_count(fungi_metadata):
    """Function for one hot encoding disease_type

    Args:
        fungi_metadata (DataFrame): Dataframe of fungi metadata

    Returns:
        DataFrame: One hot encoded dataframe of disease types
    """
    one_hot_df = pd.get_dummies(fungi_metadata['disease_type'])
    one_hot_df.to_csv("data/temp/one_hot_disease_type.csv")
    
    return one_hot_df
    
def relevant_feature_data(fungi_metadata, feature_table, feature_table_name):
    """Filter given feature table for relevant samples

    Args:
        fungi_metadata (DataFrame): Dataframe of fungi metadata
        feature_table (DataFrame): Dataframe of feature table
        feature_table_name (String): Name of feature table

    Returns:
        DataFrame: Feature table containing relevant samples
        String: Feature table name
    """
    filter_df = feature_table.filter(items = fungi_metadata.index, axis = 0)
    filter_df.to_csv("./data/temp/" + feature_table_name + "_filtered_samples.csv")
    return filter_df, feature_table_name

def relevant_feature_table_samples(fungi_metadata, datasets):
    """Filter all feature tables for relevant samples

    Args:
        fungi_metadata (DataFrame): Dataframe of metadata
        datasets (List(DataFrame)): List of feature table dataframes

    Returns:
        map: Returns a map of feature tables containing relevant samples
    """
    
    dataset_names = ["high_coverage","wis_intersect", "decontaminated"]
    return map(lambda feature_table, feature_table_name: 
        relevant_feature_data(fungi_metadata, feature_table, feature_table_name), datasets, dataset_names)
