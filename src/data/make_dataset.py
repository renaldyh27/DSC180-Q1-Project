import pandas as pd

def read_fungi_data(metadata_path, tcga_path, high_coverage_path, wis_intersect_path, decontaminated_path):
    '''Read Fungi Feature Tables, Metadata and TCGA Abbrev Files'''
    
    metadata_df = pd.read_csv(metadata_path, sep='\t',header=0, index_col='sampleid')
    tcga_abbrev_df = pd.read_csv(tcga_path, index_col='dz')
    high_coverage_df = pd.read_csv(high_coverage_path, sep='\t',header=0, index_col='sampleid')
    wis_intersect_df = pd.read_csv(wis_intersect_path, sep='\t',header=0, index_col='sampleid')
    decontaminated_df = pd.read_csv(decontaminated_path, sep='\t',header=0, index_col='sampleid')
    
    return (metadata_df,tcga_abbrev_df, high_coverage_df, wis_intersect_df, decontaminated_df)

def proces_metadata(metadata_file):
    '''Takes in raw metadata file and outputs 2 things: extract the relevant sample IDs and extract one hot encoding of the Cancer Types'''
    fungi_metadata = metadata_file
    
    fungi_metadata_cols = ['disease_type','sample_type'] 
    fungi_metadata = fungi_metadata[fungi_metadata_cols] #grab needed columns
    fungi_metadata = fungi_metadata[fungi_metadata['sample_type'] == 'Primary Tumor'] #filter only Primary Tumors

    min_count = 20 #drop cancers with fewer than 20 samples
    fungi_metadata = fungi_metadata[fungi_metadata['disease_type'].map(fungi_metadata['disease_type'].value_counts()) > min_count]

    sample_ids = fungi_metadata.index #relevant sampleID's after final cleaning
    #TODO Create sample relevant sample IDs tsvs in interim data

    cancer_types = pd.get_dummies(fungi_metadata['disease_type']) #one hot encode disease types
    #TODO Create relevant cancer types encoding tsvs in interim data

    return 

def process_fungi_data(data, sample_ids):
    '''Takes in the raw fungi data and filter for relevant samples and creates the dataset for interim data'''
    filtered_dataset = data.filter(items = sample_ids, axis=0) #filter feature tables for relevant samples
    #TODO Create dataset for interim data
    return filtered_dataset