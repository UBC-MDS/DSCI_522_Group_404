# Author: Group 404
# Date: 2020-01-23
#
"""Reads in raw csv data and performs the necessary wrangling and transformations.
Usage: src/dataprocessing.py --path_in=<path_in> --path_out=<path_out>
Options:
--path_in=<path_in>    Path (including filename) of where to read source data
--path_out=<path_out>    Path (excluding filename) of where to locally write the file
"""

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from docopt import docopt
import requests
import os

opt = docopt(__doc__)

def wrangler(input_path, output_path):
    df = pd.read_csv(input_path)


    X = df.drop(['DEPARTURE_DELAY'], axis = 1)
    y = df['DEPARTURE_DELAY']

    # First drop all the irrelevant files that won't be used in our analysis before splitting
    #X_relevant = X[['MONTH', 'AIRLINE', 'ORIGIN_AIRPORT', 'DESTINATION_AIRPORT', 'DISTANCE', 'DAY_OF_WEEK']]
    X_relevant = X[['MONTH', 'AIRLINE', 'DISTANCE', 'DAY_OF_WEEK']]
    y_numpy = np.array(y)


    # Converting the departure delay into binary targets based on the threshold of 5 mins. Greater than 5 minutes 
    # indicate late flight
    y = np.where(y_numpy > 5.0, 1, 0).tolist()

    # Turn y back into a dataframe
    y = pd.DataFrame(y, columns = ["Target"])

    # Split the dataset into training and testing datasets 
    X_train, X_test, y_train, y_test = train_test_split(X_relevant,
                                                        y,
                                                        test_size=0.4,
                                                        random_state=123)



    # Convert `MONTH` and `DAY_OF_WEEK` columns into object columns instead of numerical columns 
    # so we can get dummy columns for `MONTH` and `DAY_OF_WEEK`
    X_train[['MONTH', 'DAY_OF_WEEK']] = X_train[['MONTH', 'DAY_OF_WEEK']].astype(str)
    X_test[['MONTH', 'DAY_OF_WEEK']] = X_test[['MONTH', 'DAY_OF_WEEK']].astype(str)



    # THE DATA BASE IS TOO BIG I CAN'T RUN IT WOULD HAVE 3.5 MIL ROW WITH 1.2K COL
    # Work with a smaller dataset, because of computational and time restrictions 
    X_train_small = X_train.head(8000)
    X_test_small = X_test.head(8000)
    y_train_small = y_train[:8000]
    y_test_small = y_test[:8000]

    numerics = ["DISTANCE"]
    categoricals = ["MONTH", "AIRLINE", "DAY_OF_WEEK"]

    # Column Transformer 
    preprocessor = ColumnTransformer(
        transformers = [
            ('minmax', MinMaxScaler(), numerics),
            ('ohe', OneHotEncoder(drop = "first", sparse = False, dtype = int), categoricals)
        ]
    )

    # Clean X training dataset
    X_train_clean = pd.DataFrame(preprocessor.fit_transform(X_train_small),
            index = X_train_small.index,
            columns = (numerics +
                      list(preprocessor.named_transformers_['ohe']
                          .get_feature_names(categoricals))))

    # Clean X testing dataset
    X_test_clean = pd.DataFrame(preprocessor.transform(X_test_small),
                           index = X_test_small.index,
                           columns = X_train_clean.columns)


    # # Scale the distance column with a min max scaler 
    # scaler = MinMaxScaler()
    # X_train_small[['DISTANCE']] = scaler.fit_transform(X_train_small[['DISTANCE']])
    # X_test_small[['DISTANCE']] = scaler.transform(X_test_small[['DISTANCE']])


    # # Get dummies columns for categorical columns 
    # X_train_temp = pd.get_dummies(X_train_small, prefix_sep='_', drop_first=True)
    # X_test_temp = pd.get_dummies(X_test_small, prefix_sep='_', drop_first=True)





    # SHOULD RETURN all the X_train, test y_train, test AND the original X_train without scaling/dummy variable 
    # as the EDA dataset so data exploration will be easier. 
    X_train_clean.to_csv(output_path+"X_train_clean.csv")
    X_test_clean.to_csv(output_path+"X_test_clean.csv")
    y_train_small.to_csv(output_path+"y_train.csv")
    y_test_small.to_csv(output_path+"y_test.csv")

    X_train_small.to_csv(output_path+"eda_X_train.csv")

    X_relevant.to_csv(output_path+"X_original.csv")
    y.to_csv(output_path+"y_original.csv")


def main(path_in, path_out):
    EDA(path_in, path_out)
if __name__ == "__main__":
    main(opt["--path_in"], opt["--path_out"])

