#!/usr/bin/env python
# coding: utf-8
'''This script finds the best parameters for SVC and LGR models and fits the data to these two models and outputs the classification images and the classification reports as the csv documents.

Usage: src/model.py --data_input=<data_input> --result_output=<result_output> 

Arguments:
--data_input=<data_input>         The path for all the clean data
--result_output=<result_output>      The path where to store the csv data
'''
import numpy as np
import pandas as pd
from docopt import docopt
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
#from plot_classifier import plot_classifier
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import lightgbm as lgb

opt = docopt(__doc__)

def get_model_results(X, y, X_train, y_train, X_test, y_test, result_output):
    
    parameters_svc = {'C':np.logspace(-3,3,7), 'gamma':np.logspace(-4,2,7)}
    pd.DataFrame(parameters_svc).to_csv(result_output + '/hyper_parameters.csv')
    svc = SVC()
    svc_opt = RandomizedSearchCV(svc, parameters_svc, cv=5, iid=False, n_iter = 25)
    # svc_opt.fit(X_train, y_train)
    # train_score_svc = svc_opt.score(X_train,y_train)
    # test_score_svc= svc_opt.score(X_test,y_test)
    #svc_opt = GridSearchCV(svc, parameters_svc, cv=5, iid=False)
    
    svc_opt.fit(X_train.to_numpy(), y_train.to_numpy().ravel())
    train_score_svc = svc_opt.score(X_train.to_numpy(),y_train.to_numpy().ravel())
    test_score_svc = svc_opt.score(X_test.to_numpy(),y_test.to_numpy().ravel())
    parameters_lgr = {'C':np.logspace(-3,3,7)}
    
    lgr = LogisticRegression()

    #lgr_opt = GridSearchCV(lgr, parameters_lgr, cv=5, iid=False)
    lgr_opt = RandomizedSearchCV(lgr, parameters_lgr, cv=5, iid=False, n_iter = 25)

    lgr_opt.fit(X_train.to_numpy(), y_train.to_numpy().ravel())
    train_score_lgr = lgr_opt.score(X_train.to_numpy(),y_train.to_numpy().ravel())
    test_score_lgr = lgr_opt.score(X_test.to_numpy(),y_test.to_numpy().ravel())
    
    lgbm = lgb.LGBMClassifier()
    lgbm.fit(X_train.to_numpy(),y_train.to_numpy().ravel())
    train_score_lgbm = lgbm.score(X_train.to_numpy(),y_train.to_numpy().ravel())
    test_score_lgbm = lgbm.score(X_test.to_numpy(),y_test.to_numpy().ravel())
    
    data = {'train_accuracy':[train_score_svc, train_score_lgr, train_score_lgbm], 'test_accuracy':[test_score_svc, test_score_lgr,test_score_lgbm]}
    accuracy_df = pd.DataFrame(data, index = ['SVC','LGR','LGBM'])
    accuracy_df.to_csv(result_output+'/accuracy.csv')
    
    predictions_svc = svc_opt.predict(X_test)
    predictions_lgr = lgr_opt.predict(X_test)
    predictions_lgbm = lgbm.predict(X_test)
    svc_report = pd.DataFrame(classification_report(y_test, predictions_svc, output_dict=True))
    lgr_report = pd.DataFrame(classification_report(y_test, predictions_lgr, output_dict=True))
    lgbm_report = pd.DataFrame(classification_report(y_test, predictions_lgbm, output_dict=True))
    svc_report.to_csv(result_output+'/svc_classification_report.csv')
    lgr_report.to_csv(result_output+'/lgr_classification_report.csv')
    lgbm_report.to_csv(result_output+'/lgbm_classification_report.csv')
    
    try:
        pd.read_csv(result_output+'/svc_classification_report.csv')
        pd.read_csv(result_output+'/lgr_classification_report.csv')
        pd.read_csv(result_output+'/lgbm_classification_report.csv')
       
    except: 
        raise Exception("result doesn't save successfully")
    
    return svc_opt, lgr_opt, lgbm

def main(data_input, result_output):
    X_train = pd.read_csv(data_input+'/X_train_clean.csv')
    y_train = pd.read_csv(data_input+'/y_train.csv',usecols = ["Target"])
    X_test = pd.read_csv(data_input+'/X_test_clean.csv')
    y_test = pd.read_csv(data_input+'/y_test.csv',usecols = ["Target"])
    X = pd.read_csv(data_input+'/X_original.csv')
    y = pd.read_csv(data_input+'/y_original.csv')
    svc_opt, lgr_opt, lgbm = get_model_results(X, y, X_train, y_train, X_test, y_test, result_output)
    plt.figure(figsize=(18,3))
    # model = [svc_opt, lgr_opt]
    # for i in range(2):
    #     plt.subplot(1,4,i+1)
    #     classifier = model[i]
    #     plot_classifier(X,y,classifier,ax=plt.gca())
    #     plt.savefig(result_output+'classifier_plot.png')
if __name__ == "__main__":
        main(opt["--data_input"], opt["--result_output"])

