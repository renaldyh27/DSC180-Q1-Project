#!/usr/bin/env python


## NECESSARY IMPORTS
import sys
import os
import json

from src.data import make_dataset
from src.features import build_features
from src.models import train_model
from src.visualization import visualize

sys.path.insert(0, 'src')

def main(targets):
    if "test" in targets:
        test_path_metadata = 'test/test_metadata.tsv'
        test_path_fungi = 'test/test_fungi_data.tsv'

        metadata = make_dataset.read_fungi_data(test_path_metadata)
        feature_table = make_dataset.read_fungi_data(test_path_fungi)
        metadata_table = build_features.filter_sample_type(metadata,'Primary Tumor')

        # X
        filtered_feature_table = build_features.relevant_feature_data(metadata_table,feature_table)
        # target - Y
        disease_types = build_features.disease_type_count(metadata_table)
        
        # training model
        auroc_scores, aupr_scores = train_model.model_predict(filtered_feature_table,disease_types)
        
        return auroc_scores, aupr_scores
    else:
        return [],[]
            

if __name__ == "__main__":
    # python run.py test
    targets = sys.argv[1:]
    auroc_scores, aupr_scores = main(targets)
    print(auroc_scores, aupr_scores)
    