## Predicting US domestic flight delays using flight details

Group 404: Mike Chen, Lori Fang, Jarome Leslie

### Summary

In this project we aim to develop a classifier which predicts whether a US domestic flight will be delayed based on its characteristics. We compare Support Vector Machines ("SVM") and Logistic Regression classifiers which both resulted in a 72.6% accuracy rate on unseen validation data. Taking a closer look at the data, we observed that the status of a flight as delayed or not delayed is imbalanced with 27.4% of observations representing a delayed flight and 72.6% representing the proportion of flights that were on time. It appears that neither model does a good job of classifying delayed flights, even after parameter optimization. A second look at the features and the consideration of different classifiers may therefore be required.


```python
import pandas as pd
import numpy as np
from IPython.display import IFrame
```

## Introduction

On any given day there are approximately 87,000 flights in the skies of the United States (US National Oceanic and Atmospheric Administration). For business travellers trying to fit productivity into every hour of the day, knowing whether a flight will be delayed would help them avoid setting unrealistic meeting times. Here we endeavour to test whether a machine learning model can answer the question of whether a flight will be delayed. 

## Methods

### Data

For this project, we selected US Deparment of Transportation's dataset on [2015 Flight Delays and Cancellations](https://www.kaggle.com/usdot/flight-delays#flights.csv.). This data is shared on Kaggle under a CC0: Public Domain license.   This dataset contains data for approximately 6 million domestic flights in the 2015 calender year with datetime-, airline- and flight-related features. Some datetime-related features include `YEAR`, `MONTH`, `DAY`, `DAY_OF_THE_WEEK`, `SCHEDULED_DEPARTURE`, `DEPARTURE_TIME`, `DEPARTURE_DELAY`, and  `ARRIVAL_TIME`. Some examples of the airline-related features are `AIRLINE`, `FLIGHT_NUMBER`, and `TAIL_NUMBER`. Lastly,  the flight-related features include features such as `ORIGIN_AIRPORT`, `DESTINATION_AIRPORT`, `DISTANCE`, `SCHEDULED_TIME`, `ELAPSED_TIME`,  and `AIR_TIME`.

Taking a preliminary look at the data, we observe average departure delay for different US domestic carriers. Here we observe that Spirit Airways and United Airways experiences the largest average departure delays in 2015. Similarly, Alaska Airlines and Hawaiian Airlines recorded the lowest average departure delay times in the country for the same year. Our analysis will explore whether this feature has any predictive power.

**Figure 1. Average departure delay for each airline**


        <iframe
            width="1000"
            height="400"
            src="../results/chart1.html"
            frameborder="0"
            allowfullscreen
        ></iframe>
        

### Analysis

To compare the SVM and Logistic regression we sought out to perform hyperparameter optimization for the following values of C, and gamma. From performing `GridSearchCV` over this set, we identified the optimal parameters for the SVM classifier as &quot;{&#39;C&#39;: 0.001, &#39;gamma&#39;: 0.0001}&quot; and the optimal parameters for the logistic regression classifier as &quot;{&#39;C&#39;: 0.001}&quot;.

**Figure 2. Hyperparameters tested for optimization**

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>gamma</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.001</td>
      <td>0.0001</td>
    </tr>
    <tr>
      <td>1</td>
      <td>0.010</td>
      <td>0.0010</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0.100</td>
      <td>0.0100</td>
    </tr>
    <tr>
      <td>3</td>
      <td>1.000</td>
      <td>0.1000</td>
    </tr>
    <tr>
      <td>4</td>
      <td>10.000</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <td>5</td>
      <td>100.000</td>
      <td>10.0000</td>
    </tr>
    <tr>
      <td>6</td>
      <td>1000.000</td>
      <td>100.0000</td>
    </tr>
  </tbody>
</table>
</div>

In addition, to minimize the bias of not taking into account all of the training data, we implemented 5-fold cross validation. As we embarked on this journey it became that our original 500,000 observation slice of full dataset was too large to process in this manner. Accordingly we pared down our analysis to a subset containing 8,000 training examples and 2,000 validation examples.  The R and Python programming languages (R Core Team 2019; Van Rossum and Drake 2009) and the following R and Python packages were used to perform the analysis:  docopt (de Jonge 2018), tidyverse (Wickham 2017), docopt (Keleshev 2014), RCurl (Lang 2020), testthat (Wickam 2011), Pandas (McKinney 2010), NumPy (Oliphant 2006). The code for this analysis may be found [here](https://github.com/UBC-MDS/DSCI_522_Group_404).



## Results & Discussion

Using sklearn's classification report, we observe that the SVM and logistic regression models yield identical results. More specifically we observe that neither captures predictions for delayed flights as seen from the f1 score for the delayed group being zero.


**Figure 3. Classification report for the SVM classifier**

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>0</th>
      <th>1</th>
      <th>accuracy</th>
      <th>macro avg</th>
      <th>weighted avg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>precision</td>
      <td>0.726375</td>
      <td>0.0</td>
      <td>0.726375</td>
      <td>0.363187</td>
      <td>0.527621</td>
    </tr>
    <tr>
      <td>1</td>
      <td>recall</td>
      <td>1.000000</td>
      <td>0.0</td>
      <td>0.726375</td>
      <td>0.500000</td>
      <td>0.726375</td>
    </tr>
    <tr>
      <td>2</td>
      <td>f1-score</td>
      <td>0.841503</td>
      <td>0.0</td>
      <td>0.726375</td>
      <td>0.420752</td>
      <td>0.611247</td>
    </tr>
    <tr>
      <td>3</td>
      <td>support</td>
      <td>5811.000000</td>
      <td>2189.0</td>
      <td>0.726375</td>
      <td>8000.000000</td>
      <td>8000.000000</td>
    </tr>
  </tbody>
</table>
</div>

**Figure 4. Classification report for the logistic regression classifier**

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>0</th>
      <th>1</th>
      <th>accuracy</th>
      <th>macro avg</th>
      <th>weighted avg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>precision</td>
      <td>0.726375</td>
      <td>0.0</td>
      <td>0.726375</td>
      <td>0.363187</td>
      <td>0.527621</td>
    </tr>
    <tr>
      <td>1</td>
      <td>recall</td>
      <td>1.000000</td>
      <td>0.0</td>
      <td>0.726375</td>
      <td>0.500000</td>
      <td>0.726375</td>
    </tr>
    <tr>
      <td>2</td>
      <td>f1-score</td>
      <td>0.841503</td>
      <td>0.0</td>
      <td>0.726375</td>
      <td>0.420752</td>
      <td>0.611247</td>
    </tr>
    <tr>
      <td>3</td>
      <td>support</td>
      <td>5811.000000</td>
      <td>2189.0</td>
      <td>0.726375</td>
      <td>8000.000000</td>
      <td>8000.000000</td>
    </tr>
  </tbody>
</table>
</div>






## References

"Air Traffic." National Oceanic and Atmospheric Administration. Accessed January 25, 2020. <https://sos.noaa.gov/datasets/air-traffic/>

Lang, D. (2020). RCurl: General Network (HTTP/FTP/...) Client Interface for R. R
  package version 1.98-1.1. <https://CRAN.R-project.org/package=RCurl>

de Jonge, E.  (2018). docopt: Command-Line Interface Specification Language. R package
  version 0.6.1. <https://CRAN.R-project.org/package=docopt>

McKinney, W., & others. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51–56).

Pedregosa, F., Varoquaux, Ga"el, Gramfort, A., Michel, V., Thirion, B., Grisel, O., … others. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12(Oct), 2825–2830.

R Core Team. 2019. R: A Language and Environment for Statistical Computing. Vienna, Austria: R Foundation for Statistical Computing. https://www.R-project.org/.

Oliphant, T. A guide to NumPy, USA: Trelgol Publishing, (2006).

"US Department of Transportation - 2015 Flight Delays and Cancellations." Kaggle Inc. Accessed January 15, 2020. <https://www.kaggle.com/usdot/flight-delays#flights.csv>

Van Rossum, G., and Drake, F. 2009. Python 3 Reference Manual. Scotts Valley, CA: CreateSpace.

Wickham, H. 2017. Tidyverse: Easily Install and Load the ’Tidyverse’. https://CRAN.R-project.org/package=tidyverse.

Wickham, H., Hester, J., and Francois, R. (2018). readr: Read Rectangular Text Data. R
  package version 1.3.1. https://CRAN.R-project.org/package=readr
  
Wickham, H. testthat: Get Started with Testing. The R Journal, vol. 3, no. 1, pp. 5--10,
  2011



## Appendix


```python
#variables for report
Test_acc = round(np.max(pd.read_csv('../results/accuracy.csv')['test_accuracy']),3)*100
y_original = pd.read_csv('../data/y_test.csv')['Target']
late_dep = round(np.sum(pd.read_csv('../data/y_test.csv')['Target'])/len(pd.read_csv('../data/y_test.csv')['Target'])*100,1)
```
