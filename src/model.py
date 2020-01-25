#!/usr/bin/env python
# coding: utf-8
'''This script finds the best parameters for SVC and LGR models and fits the data to these two models and outputs the classification images and the classification reports as the csv documents.

Usage: src/model.py <data_input> <data_result_output> <image_output>

Arguments:

<data_input>         The path for all the clean data
<data_result_output> The path where to store the csv data
<image_output>       The path where to store images

'''

import numpy as np
import pandas as pd
from docopt import docopt

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from plot_classifier import plot_classifier
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report

opt = docopt(__doc__)


def get_model_results(X, y, X_train, y_train, X_test, y_test, output):
  parameters_svc = {'C':np.logspace(-3,3,7), 'gamma':np.logspace(-5,2,8)}
  svc = SVC()
  svc_opt = GridSearchCV(svc, parameters_svc, cv=5, iid=False)
  svc_opt.fit(X_train, y_train.to_numpy().ravel())
  train_score_svc = svc_opt.score(X_train,y_train)
  test_score_svc= svc_opt.score(X_test,y_test)
  svc_confusion_matrix = pd.DataFrame(confusion_matrix(y, svc_opt.predict(X)))
  
  parameters_lgr = {'C':np.logspace(-3,3,7)}
  lgr = LogisticRegression()
  lgr_opt = GridSearchCV(lgr, parameters_lgr, cv=5, iid=False)
  lgr_opt.fit(X_train, y_train.to_numpy().ravel())
  train_score_lgr = lgr_opt.score(X_train,y_train)
  test_score_lgr = lgr_opt.score(X_test,y_test)
  lgr_confusion_matrix = pd.DataFrame(confusion_matrix(y, lgr_opt.predict(X)))
  
  data = {'train_accuracy': [train_score_svc, train_score_lgr], 'test_accuracy':[test_score_svc, test_score_lgr]}
  accuracy = pd.DataFrame(data, index = ['SVC','LGR'])
  
  accuracy_df.to_csv(f'./{data_result_output}/accuracy.csv')
  
  predictions_svc = svc_opt.predict(X_test)
  predictions_lgr = lgr_opt.predict(X_test)
  svc_report = pd.DataFrame(classification_report(y_test, predictions_svc))
  lgr_report = pd.DataFrame(classification_report(y_test, predictions_lgr))
 
  svc_report.to_csv(f'./{data_result_output}/svc_classification_report.csv')
  lgr_report.to_csv(f'./{data_result_output}/svc_classification_report.lgr')
  


def main(data_input, image_output, data_result_output):
  X_train = pd.read_csv("{data_input}/X_train_temp.csv")
  y_train = pd.read_csv("{data_input}/y_train.csv")

  X_test = pd.read_csv("{data_input}/X_test_temp.csv")
  y_test = pd.read_csv("{data_input}/y_test.csv")
  
  #X = pd.read_csv("{data_input}/X_path")
  #y = pd.read_csv("{data_input}/y_path")
  
  get_model_results(X, y, X_train, y_train, X_test, y_test, data_result_output)

  
  plt.figure(figsize=(18,3))
  model = [svc_opt, lgr_opt]
  for i in range(2):
    plt.subplot(1,4,i+1)
    classifier = model[i]
    plot_classifier(X,y,classifier,ax=plt.gca())
  plt.savefig(f'./{image_output}/classifier_plot.png')
 
 
  
if __name__ == "__main__":
  main(input=opt["--input"], output=opt["--output"])


