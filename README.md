# DSC180-Q1-Project
Abstract:
In this study, we are reproducing a pan-cancer analysis on cancer tumor samples to characterize the fungal mycobiome within multiple cancer types and explore the correlation between fungi and tumor cells. There currently exist some methods of early-cancer detection using bacterial microbiomes but no way of detecting early types of cancer using the fungal mycobiome. The results of this analysis suggest prognostic and diagnostic capabilities of tissue mycobiomes, especially in junction with bacterial microbiomes.

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
