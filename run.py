#!/usr/bin/env python


## NECESSARY IMPORTS
import sys
import json
import os
import shutil

from src.data import make_dataset
from src.features import build_features
from src.models import train_model
from src.visualization import visualize



def main(targets):
    if "test" in targets:
        if not os.path.exists("data/temp"):
            os.makedirs("data/temp")
        if not os.path.exists("data/out"):
            os.makedirs("data/out")
        
        test_path_metadata="test/test_metadata.tsv"
        test_path_fungi = "test/test_fungi_data.tsv"

        metadata = make_dataset.read_fungi_file(test_path_metadata)
        feature_table = make_dataset.read_fungi_file(test_path_fungi)
        tcga_abbrev = make_dataset.read_tcga_abbrev_file("test/tcga_abbreviations.csv")
        
        metadata_table = build_features.filter_sample_type(metadata,'Primary Tumor')

        # X
        filtered_feature_table = build_features.relevant_feature_data(metadata_table, feature_table, 'test')
        # target - Y
        disease_types = build_features.disease_type_count(metadata_table)
        # training model
        with open("config/gbc-model-params.json") as fh:
            gbc_model_params = json.load(fh)
        
        with open("config/skf-model-params.json") as fh:
            skf_params = json.load(fh)
        
        
        plot_data = {}
        
        gbc_model = train_model.init_gbc_model(**gbc_model_params)
        skf = train_model.init_skf(**skf_params)
        auroc_scores, aupr_scores = train_model.model_predict(filtered_feature_table[0], disease_types, gbc_model, skf)
        plot_data['test'] = (auroc_scores, aupr_scores)
        
        plot_data_path = visualize.save_plot_data(plot_data)
        visualize.plot_model_metrics(plot_data_path, disease_types, tcga_abbrev, ['test'])

        return 

    
    if "all" in targets:
        if not os.path.exists("data/temp"):
            os.makedirs("data/temp")
        if not os.path.exists("data/out"):
            os.makedirs("data/out")
            
        with open("config/data-params.json") as fh:
            file_paths = json.load(fh)
            
        metadata_table, tcga_abbrev, high_coverage_feature, wis_intersect_feature, decontaminated_feature = make_dataset.read_fungi_data(**file_paths)
       
        datasets = (high_coverage_feature, wis_intersect_feature,decontaminated_feature)
        plot_data = {}
        
        with open("config/feature-params.json") as fh:
            feature_params = json.load(fh)
            
        filtered_metadata = build_features.filter_sample_type(metadata_table, **feature_params)
        # X (three datasets)
        filtered_feature_tables = build_features.relevant_feature_table_samples(filtered_metadata, datasets)
        # Target - Y
        disease_types = build_features.disease_type_count(filtered_metadata)
        
        with open("config/gbc-model-params.json") as fh:
            gbc_model_params = json.load(fh)
        
        with open("config/skf-model-params.json") as fh:
            skf_params = json.load(fh)
        
        
        for dataset, dataset_name in filtered_feature_tables:
            gbc_model = train_model.init_gbc_model(**gbc_model_params)
            skf = train_model.init_skf(**skf_params)
            auroc_scores, aupr_scores = train_model.model_predict(dataset, disease_types, gbc_model, skf)
            plot_data[dataset_name] = (auroc_scores, aupr_scores)
        
        plot_data_path = visualize.save_plot_data(plot_data)
        # question about lablels
        visualize.plot_model_metrics(plot_data_path, disease_types, tcga_abbrev,['Species high coverage','Species ∩ WIS','Species decontaminated'])

        return 
        
    if 'clean' in targets:
        try:
            os.remove('final_figure.png')
        except OSError as e: 
            print ("Error: %s - %s." % (e.filename, e.strerror))
        try:
            shutil.rmtree("data/temp")
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
        try:
            shutil.rmtree("data/out")
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))

if __name__ == "__main__":
    # python run.py test
    targets = sys.argv[1:]
    main(targets)
    #generates graph in final_figure.png
