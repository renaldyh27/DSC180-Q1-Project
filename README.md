# DSC180-Q1-Project
Numerous studies have explored the relationship between bacteria microbiome and cancer and have found that microbes could be used to discriminate and classify different cancer types as well as detect early stages of cancer in patients. However the association of fungal mycobiome with cancer has not been thoroughly explored before. Fungi have been found to interact heavily with bacteria by physical and biochemical mechanisms. Symbiotic, synergetic and antagonistic relationships occur between fungi, bacteria and the immune system, therefore it is imperative to explore the impacts of the mycobiome has on tumors. In this study, we perform a pan-cancer analysis on patients’ tissue, blood and plasma to characterize the mycobiome within multiple cancer types. We are applying statistical and machine learning analyses to detect and classify cancer-types and found that we are able to discriminate cancer-types based on the cancer-type-specific mycobiomes. Results of the analyses also displayed strong correlation between fungal diversity and abundance with occurrences of several cancer types suggesting permissive/supportive environments for tumor cells. This warrants further exploration of fungi in the world of cancer research.

## Retrieving the data locally:
(1) Download the data files from the following Google Drive: https://drive.google.com/drive/u/0/folders/10fizMmiwPm-ziLHgRkqbN7f0nO7SR-cZ

(2) Edit the file: config/data-params.json to include the paths of the downloaded data in the value of their correponding keys which is indicated by their file names

## Running the Project
* To revert to a clean repository, from the project root dir, run `python run.py clean`
  * This deletes all built files
* To run the entire project on test data, from the project root dir, run `python run.py test`
  * This fetches the test data, creates features, cleans the data, creates GBM model
  and creates a performance graph
* To run the entire project on the real data, from the project root dir, run `python run.py all`
  * This fetches the data, creates features, cleans the data, creates GBM model
  and creates a performance graph

Collaborator: Renaldy Herlim, Emerson Chao, Amando Jimenez, Benjamin Sacks, Mark Zheng, Ethan Chan
