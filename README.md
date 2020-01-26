# DSCI 522: Group 404

Authors: Mike Chen, Lori Fang, Jarome Leslie

Data analysis project for DSCI 522 - Data Science Workflows.

## About

In this project we develop a classification mode to predict which domestic US flights are most likely to be delayed. In this analysis we compare the predictive power of Logistic Regression and Support Vector Machine ("SVM") classifiers, while accounting for hyperparameter tuning. ADD SENTENCES ABOUT RESULTS.

For this project, we selected US Deparment of Transportation's dataset on 2015 Flight Delays and Cancellations. This data is shared on Kaggle under a CC0: Public Domain license. This dataset contains data for approximately 6 million domestic flights in the 2015 calender year with datetime-, airline- and flight-related features. Some datetime-related features include YEAR, MONTH, DAY, DAY_OF_THE_WEEK, SCHEDULED_DEPARTURE, DEPARTURE_TIME, DEPARTURE_DELAY, and ARRIVAL_TIME. Some examples of the airline-related features are AIRLINE, FLIGHT_NUMBER, and TAIL_NUMBER. Lastly, the flight-related features include features such as ORIGIN_AIRPORT, DESTINATION_AIRPORT, DISTANCE, SCHEDULED_TIME, ELAPSED_TIME, and AIR_TIME.


## Report

The final report for our analysis may be found [here](https://github.com/jsleslie/DSCI_522_Group_404/blob/f3963b2c394ba8f08a51be295f2db0398c6336cb/doc/flight_delays_report.ipynb).

## Usage

To download the flights dataset, run the following code in the command line:

```
Rscript src/load_data.R 'https://dl.dropboxusercontent.com/s/5o9gmtpq2q8cshp/flights.csv?dl=0' 'data/flights.csv'

python src/dataprocessing.py --path_in="data/flights.csv" --path_out="/data"

python src/model2.py data results results


```

## Links

The v0.1 release for this project may be found here: [Pre-release version 0.1](https://github.com/UBC-MDS/DSCI_522_Group_404/releases/tag/0.1)

The EDA for this project may be found here: [Group 404 EDA](https://github.com/jsleslie/DSCI_522_Group_404/blob/3df0489caddf20d321e108be90ee03165937719f/src/Preliminary_EDA.ipynb)



# References

"US Department of Transportation - 2015 Flight Delays and Cancellations." Kaggle Inc. Accessed January 15, 2020. https://www.kaggle.com/usdot/flight-delays#flights.csv
