# DSCI 522: Group 404

Authors: Mike Chen, Lori Fang, Jarome Leslie

Data analysis project for DSCI 522 - Data Science Workflows.

## About

In this project we develop a classification mode to predict which domestic US flights are most likely to be delayed. In this analysis we compare the predictive power of Logistic Regression and Support Vector Machine ("SVM") classifiers, while accounting for hyperparameter tuning. Unfortunately it appears that neither of these models do a good job at predicting delayed flights.

For this project, we selected US Deparment of Transportation's dataset on 2015 Flight Delays and Cancellations. This data is shared on Kaggle under a CC0: Public Domain license. This dataset contains data for approximately 6 million domestic flights in the 2015 calender year with datetime-, airline- and flight-related features. Some datetime-related features include YEAR, MONTH, DAY, DAY_OF_THE_WEEK, SCHEDULED_DEPARTURE, DEPARTURE_TIME, DEPARTURE_DELAY, and ARRIVAL_TIME. Some examples of the airline-related features are AIRLINE, FLIGHT_NUMBER, and TAIL_NUMBER. Lastly, the flight-related features include features such as ORIGIN_AIRPORT, DESTINATION_AIRPORT, DISTANCE, SCHEDULED_TIME, ELAPSED_TIME, and AIR_TIME.


## Report

The final report for our analysis may be found [here](https://ubc-mds.github.io/DSCI_522_Group_404/doc/flight_delays_report.html).

## Usage

To replicate the analysis, clone this GitHub repository, install the dependencies listed below, and run the following command at the command line/terminal from the root directory of this project:

```
make all
```

To reset the repo to a clean state, with no intermediate or results files, run the following command at the command line/terminal from the root directory of this project:

```
make clean
```

## Links

The v0.1 release for this project may be found here: [Pre-release version 0.1](https://github.com/UBC-MDS/DSCI_522_Group_404/releases/tag/0.1)

The EDA for this project may be found here: [Group 404 EDA](https://github.com/jsleslie/DSCI_522_Group_404/blob/3df0489caddf20d321e108be90ee03165937719f/src/Preliminary_EDA.ipynb)


## Dependencies
- Python 3.7.3 and Python packages:
  - docopt==0.6.2
  - requests==2.22.0
  - pandas==0.25.2
  - scikit-learn==0.22.1
  - altair==3.2.0
- R version 3.6.1 and R packages:
  - readr==1.3.1
  - docopt==0.6.1
  - RCurl==1.98.1.1
  - testthat==2.2.1


# References

"US Department of Transportation - 2015 Flight Delays and Cancellations." Kaggle Inc. Accessed January 15, 2020. https://www.kaggle.com/usdot/flight-delays#flights.csv
