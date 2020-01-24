#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer


# In[57]:


df = pd.read_csv("flights.csv")


# In[58]:


X = df.drop(['DEPARTURE_DELAY'], axis = 1)
y = df['DEPARTURE_DELAY']


# In[59]:


# First drop all the irrelevant files that won't be used in our analysis before splitting
X_relevant = X[['MONTH', 'AIRLINE', 'ORIGIN_AIRPORT', 'DESTINATION_AIRPORT', 'DISTANCE', 'DAY_OF_WEEK']]
y_numpy = np.array(y)


# In[60]:


# Converting the departure delay into binary targets based on the threshold of 5 mins. Greater than 5 minutes 
# indicate late flight
y = np.where(y_numpy > 5.0, 1, 0).tolist()


# In[61]:


# Split the dataset into training and testing datasets 
X_train, X_test, y_train, y_test = train_test_split(X_relevant,
                                                    y,
                                                    test_size=0.4,
                                                    random_state=123)


# In[62]:


# Convert `MONTH` and `DAY_OF_WEEK` columns into object columns instead of numerical columns 
# so we can get dummy columns for `MONTH` and `DAY_OF_WEEK`
X_train[['MONTH', 'DAY_OF_WEEK']] = X_train[['MONTH', 'DAY_OF_WEEK']].astype(str)
X_test[['MONTH', 'DAY_OF_WEEK']] = X_test[['MONTH', 'DAY_OF_WEEK']].astype(str)


# In[63]:


############ THE DATA BASE IS TOOOOOOOOOOOOOOOOOOOOOO BIGGGGGG I CAN'T RUN IT WOULD HAVE 3.5 MIL ROW WITH 1.2K COL =O
X_train_small = X_train.head(50000)
X_test_small = X_test.head(50000)
y_train_small = y_train[:50000]
y_test_small = y_test[:50000]


# In[64]:


# Scale the distance column with a min max scaler 
scaler = MinMaxScaler()
X_train_small[['DISTANCE']] = scaler.fit_transform(X_train_small[['DISTANCE']])
X_test_small[['DISTANCE']] = scaler.transform(X_test_small[['DISTANCE']])


# In[65]:


# Get dummies columns for categorical columns 
X_train_temp = pd.get_dummies(X_train_small, prefix_sep='_', drop_first=True)
X_test_temp = pd.get_dummies(X_test_small, prefix_sep='_', drop_first=True)


# In[66]:


# HEAD 1278 COLUMNS 
X_test_temp.head()


# In[ ]:


# SHOULD RETURN all the X_train, test y_train, test AND the original X_train without scaling/dummy variable 
# as the EDA dataset so data exploration will be easier. 
X_train_temp.to_csv("data/X_train_temp.csv")
X_test_temp.to_csv("data/X_test_temp.csv")
y_train_small.to_csv("data/y_train.csv")
y_test_small.to_csv("data/y_test.csv")

X_train_small.to_csv("data/eda_X_train.csv")
