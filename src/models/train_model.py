from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import precision_recall_curve, average_precision_score, auc
from sklearn.metrics import roc_auc_score


import numpy as np

## TODO Py script to train and output model ## 
def model_predict(dataset, cancer_types):
    '''Take in as input the cleaned datasets of the features(X) and the one-hot encoded cancer types/targets(Y)
       then perform 10-fold validation split and use them to train the model.
       
       Output: Auroc and Aupr scores of the model
       
    '''
    
    #TODO: define cross validation hyperparams
    n_splits = 10
    skf_random = 0 #DO NOT TOUCH
    shuffle=True
    #TODO: define model hyperparams, can automate tuning later
    loss = 'exponential'
    learning_rate = 0.1
    n_estimators = 150
    max_depth = 3
    clf_random = 0 #DO NOT TOUCH
   
    skf = StratifiedKFold(n_splits=n_splits, random_state=skf_random, shuffle=shuffle)

    clf = GradientBoostingClassifier(loss=loss, learning_rate=learning_rate, n_estimators=n_estimators, max_depth=max_depth, random_state=clf_random)
    
    for i, cancer in enumerate(cancer_types.columns, start=1):
        X = dataset
        y = cancer_types[cancer]
        
        auroc_plt_data = np.array([])
        aupr_plt_data = np.array([])
        
        for train_index, val_index in skf.split(X, y):
            train_X, train_y = X.iloc[train_index], y.iloc[train_index]
            val_X, val_y = X.iloc[val_index], y.iloc[val_index]

            clf.fit(train_X, train_y) #re-fit model
            
            preds = clf.predict_proba(val_X)[:,1] #predict, probability of positive class predict

            auroc = roc_auc_score(val_y, preds) #TODO: implement separate score function to return multiple scores
            aupr = average_precision_score(val_y, preds)
            
            auroc_plt_data = np.append(auroc_plt_data, auroc)
            aupr_plt_data = np.append(aupr_plt_data, aupr)
    
    return auroc_plt_data, aupr_plt_data