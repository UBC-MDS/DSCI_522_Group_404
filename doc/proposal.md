# Project Proposal

### Data

For this project, we selected US Deparment of Transportation's dataset on [2015 Flight Delays and Cancellations](https://www.kaggle.com/usdot/flight-delays#flights.csv.). This data is shared on Kaggle under a CC0: Public Domain license.   This dataset contains data for approximately 6 million domestic flights in the 2015 calender year with datetime-, airline- and flight-related features. Some datetime-related features include `YEAR`, `MONTH`, `DAY`, `DAY_OF_THE_WEEK`, `SCHEDULED_DEPARTURE`, `DEPARTURE_TIME`, `DEPARTURE_DELAY`, and  `ARRIVAL_TIME`. Some examples of the airline-related features are `AIRLINE`, `FLIGHT_NUMBER`, and `TAIL_NUMBER`. Lastly,  the flight-related features include features such as `ORIGIN_AIRPORT`, `DESTINATION_AIRPORT`, `DISTANCE`, `SCHEDULED_TIME`, `ELAPSED_TIME`,  and `AIR_TIME`.


### Research question

Our main research question is the classification problem of predicting which flights are likely to be delayed. The motivation for this study is to help business travel passengers in making plans when they travel on the amount of buffer time they should keep in their schedules when travelling before making meeting commitments. For example, consultants travelling to client sites could reduce the likelihood of missing meetings due to delays in their domestic flights.

### Our plan
Random forest, SVC, and logistic regression are all feasible models for our research question. Since SVC has strong predictive power via kernel trick, and is effective in high dimensional spaces and also relatively memory efficient, logistic regression is easier to implement, interpret and very efficient to train, so we decided to use these two models to fit our data set.

### Exploratory Data Analysis
Before fit the data to any model, we will use scatter plot to see how the data points are distributed and diagnose any association. Then we can fit it into a model.

### Results
We will use the classifier plot and classification report to compare how our models are performing. The conclusion will be discussed below the plot and tables. 



### References

"US Department of Transportation - 2015 Flight Delays and Cancellations." Kaggle Inc. Accessed January 15, 2020. <https://www.kaggle.com/usdot/flight-delays#flights.csv>
