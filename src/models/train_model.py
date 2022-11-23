from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

## TODO Py script to train and output model ## 
def train_models(datasets, cancer_types):
    '''Take in as input the cleaned datasets of the features(X) and the one-hot encoded cancer types/targets(Y)
       then perform 10-fold validation split and use them to train the model.
       
       Output: Trained Model for all the datasets
       
    '''
    models = []
    #Get the cleaned dataset to use for Model Training
    
        #Output cleaned datasets features (Predictors/X) & cancer types (Prediction/Y) dataset to use for model training


    #Perform the CV splits 

    #Train model for each cancer type

    #Return the trained model for the specified dataset
    return models