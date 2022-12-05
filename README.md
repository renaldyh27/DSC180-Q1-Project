# DSC180-Q1-Project
In this study, we perform a pan-cancer analysis on patients’ tissue to characterize the fungal mycobiome within multiple cancer types and explore the correlation between fungi and tumor cells. Specifically we will be analyzing the Harvard Medical School cohort of The Cancer Genome Atlas (TCGA) primary tumor dataset, extracting the relevant metadata features, and applying a one-cancer-type-versus-all binary classification to classify cancer types based on the cancer-type-specific mycobiomes. After validating our model results using cross validation techniques, we visualized the average test scores along with the confidence intervals and found that we are able to achieve significant results in discriminating cancer types using these methods. These results may affect clinical diagnoses and outcomes of treatments and warrant further exploration of fungi in the world of cancer research.

Full report can be found here: https://docs.google.com/document/d/1ms6KzcOIcRoE3XDqbN9lE-cxh08DgB7hJR8SoUVEIP0/edit#heading=h.ao4fmmeqtphu
## Retrieving the data locally:
(1) Download the data files from the following Google Drive: https://drive.google.com/drive/u/0/folders/10fizMmiwPm-ziLHgRkqbN7f0nO7SR-cZ

(2) Place files in `data/raw` directory

## Running the Project:
* To revert to a clean repository, from the project root dir, run `python run.py clean`
  * This deletes all built files
* To run the entire project on test data, from the project root dir, run `python run.py test`
  * This fetches the test data, creates features, cleans the data, creates GBM model
  and creates a performance graph
* To run the entire project on the real data, from the project root dir, run `python run.py all`
  * This fetches the data, creates features, cleans the data, creates GBM model
  and creates a performance graph

Collaborator: Renaldy Herlim, Emerson Chao, Amando Jimenez, Benjamin Sacks, Mark Zheng, Ethan Chan
