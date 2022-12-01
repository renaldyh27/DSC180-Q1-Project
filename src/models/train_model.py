from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_auc_score

import numpy as np

def model_predict(dataset, disease_types, gbc_model, skf_model):
    """Take in as input the cleaned datasets of the features(X) and one-hot encoded cancer types/targets(Y)
       then perform 10-fold validation split and use them to train the model.

    Args:
        dataset (Dataframe): Dataframe of feature table
        disease_types (DataFrame): One hot encoded dataframe of disease_types
        gbc_model (GradientBoostingClassifier): Initialized GradientBoostingClassifier
        skf_model (StratifiedKFold): Initialized StratifiedKFold 

    Returns:
        (List, List): Outputs two lists of AUROC and AUPR scores of the model
    """
   
    skf = skf_model

    clf = gbc_model
    
    for i, cancer in enumerate(disease_types.columns, start=1):
        X = dataset
        y = disease_types[cancer]
        
        auroc_plt_data = np.array([])
        aupr_plt_data = np.array([])
        
        # Loop trough folds
        for train_index, val_index in skf.split(X, y):
            train_X, train_y = X.iloc[train_index], y.iloc[train_index]
            val_X, val_y = X.iloc[val_index], y.iloc[val_index]
            
            # fit model
            clf.fit(train_X, train_y) 
            
            # Predict probability of positive class
            preds = clf.predict_proba(val_X)[:,1] 
            
            # Calculate scores on given fold
            auroc = roc_auc_score(val_y, preds)
            aupr = average_precision_score(val_y, preds)
            
            auroc_plt_data = np.append(auroc_plt_data, auroc)
            aupr_plt_data = np.append(aupr_plt_data, aupr)
    
    return auroc_plt_data, aupr_plt_data

def init_gbc_model(loss, learning_rate, n_estimators, max_depth, gbc_random_state):
    """Function for initializing the gradient boosting classifier model

    Args:
        loss (String): loss function
        learning_rate (float): learning rate
        n_estimators (int): Number of boosting stages to perform
        max_depth (int): Max depth of nodes in a tree
        gbc_random_state (int): random_state

    Returns:
        GradientBoostingClassifier: _description_
    """
    return GradientBoostingClassifier(loss=loss, learning_rate=learning_rate, n_estimators=n_estimators, max_depth=max_depth, random_state=gbc_random_state)

def init_skf_model(n_splits, shuffle, skf_random_state):
    """Function for initializing the stratified k folding model

    Args:
        n_splits (int): Number of splits to seperate data
        shuffle (boolean): Wheter to shuffle data
        skf_random_state (int): random_state

    Returns:
        StratifiedKFold: _description_
    """
    return StratifiedKFold(n_splits=n_splits,shuffle=shuffle, random_state=skf_random_state)