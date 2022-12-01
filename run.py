#!/usr/bin/env python


## NECESSARY IMPORTS
import sys
import os
import json

sys.path.insert(0, 'src')

from src.data import make_dataset, test_data_generator
from src.features import build_features
from src.models import train_model
from src.visualization import visualize



def main(targets):
    if "test" in targets:
        
        test_path_metadata, test_path_fungi = test_data_generator.generate_test_data()

        metadata = make_dataset.read_fungi_file(test_path_metadata)
        feature_table = make_dataset.read_fungi_file(test_path_fungi)
        metadata_table = build_features.filter_sample_type(metadata,'Primary Tumor',"test/test_metadata_filtered.csv")

        # X
        filtered_feature_table = build_features.relevant_feature_data(metadata_table,feature_table)
        # target - Y
        disease_types = build_features.disease_type_count(metadata_table)
        # training model
        with open("config/model-params.json") as fh:
            model_cfg = json.load(fh)
            
        auroc_scores, aupr_scores = train_model.model_predict(filtered_feature_table, disease_types,**model_cfg)
        
        return auroc_scores, aupr_scores
    
    if "all" in targets:
        with open("config/data-params.json") as fh:
            file_paths = json.load(fh)
            
        metadata_table, tcga_abbrev, high_coverage_feature, wis_intersect_feature, decontaminated_feature = make_dataset.read_fungi_data(**file_paths)
       
        datasets = (high_coverage_feature, wis_intersect_feature,decontaminated_feature)
        
        with open("config/feature-params.json") as fh:
            feature_params = json.load(fh)
            
        filtered_metadata = build_features.filter_sample_type(metadata_table, **feature_params)
        # X (three datasets)
        filtered_feature_tables = build_features.relevant_feature_table_samples(filtered_metadata, datasets)
        # Target - Y
        disease_types_count = build_features.disease_type_count(filtered_metadata)
        
        with open("config/gbc-model-params.json") as fh:
            gbc_model_params = json.load(fh)
        
        with open("config/skf-model-params.json") as fh:
            skf_model_params = json.load(fh)
            
        for dataset in filtered_feature_tables:
            gbc_model = train_model.init_gbc_model(**gbc_model_params)
            skf_model = train_model.init_skf_model(**skf_model_params)
            auroc_scores, aupr_scores = train_model.model_predict(dataset, disease_types_count, gbc_model, skf_model)

        #TODO: Add visualization code here

        return auroc_scores, aupr_scores
        

if __name__ == "__main__":
    # python run.py test
    targets = sys.argv[1:]
    auroc_scores, aupr_scores = main(targets)
    print(auroc_scores, aupr_scores)
    
