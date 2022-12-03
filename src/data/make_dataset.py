import pandas as pd

def read_fungi_file(path):
    """Reads fungi data from file into a DataFrame

    Args:
        path (String): Path of fungi file containing data

    Returns:
        DataFrame: Dataframe containing fungi data
    """
    return pd.read_csv(path, sep="\t",header=0,index_col="sampleid")

def read_fungi_data(metadata_path, tcga_abbrev_path, high_coverage_path, wis_intersect_path, decontaminated_path):
    """Reads Fungi Feature Tables, Metadata and TCGA Abbrev Files

    Args:
        metadata_path (String): Path of fungi metadata file
        tcga_abbrev_path (String): Path of TCGA abbrevation file
        high_coverage_path (String): Path of High Coverage fungi data file
        wis_intersect_path (String): Path of WIS intersect fungi data file
        decontaminated_path (String): Path of decontaminiated fungi data file

    Returns:
        Tuple(DataFrames): Tuple of dataframes containing fungi data
    """
    
    metadata_df = read_fungi_file(metadata_path)
    tcga_abbrev_df = read_tcga_abbrev_file(tcga_abbrev_path)
    high_coverage_df = read_fungi_file(high_coverage_path)
    wis_intersect_df = read_fungi_file(wis_intersect_path)
    decontaminated_df = read_fungi_file(decontaminated_path)
    
    return (metadata_df, tcga_abbrev_df, high_coverage_df, wis_intersect_df, decontaminated_df)

def read_tcga_abbrev_file(tcga_abbrev_path):
    """Read TCGA abbrev file

    Args:
        path (String): Path of TCGA abbrevation file

    Returns:
        DataFrame: Dataframe of TCGA cancer abbreviations
    """
    return pd.read_csv(tcga_abbrev_path, index_col='dz')
