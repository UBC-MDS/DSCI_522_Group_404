# Project Proposal

### Data

For this project, we selected US Deparment of Transportation's dataset on [2015 Flight Delays and Cancellations](https://www.kaggle.com/usdot/flight-delays#flights.csv.). This data is shared on Kaggle under a CC0: Public Domain license.   This dataset contains data for approximately 6 million domestic flights in the 2015 calender year with datetime-, airline- and flight-related features. Some datetime-related features include `YEAR`, `MONTH`, `DAY`, `DAY_OF_THE_WEEK`, `SCHEDULED_DEPARTURE`, `DEPARTURE_TIME`, `DEPARTURE_DELAY`, and  `ARRIVAL_TIME`. Some examples of the airline-related features are `AIRLINE`, `FLIGHT_NUMBER`, and `TAIL_NUMBER`. Lastly,  the flight-related features include features such as `ORIGIN_AIRPORT`, `DESTINATION_AIRPORT`, `DISTANCE`, `SCHEDULED_TIME`, `ELAPSED_TIME`,  and `AIR_TIME`.


### Research question

Our main research question is the classification problem of predicting which flights are likely to be delayed. The motivation for this study is to help business travel passengers in making plans when they travel on the amount of buffer time they should keep in their schedules when travelling before making meeting commitments. For example, consultants travelling to client sites could reduce the likelihood of missing meetings due to delays in their domestic flights.

### Our plan
We plan to fit a linear model on the dataset to find if there is signigificant linear relationship between those two variables by conducting a hypothesis test and how is their relationship by contucting a Generalized Linear Model. 

### Exploratory Data Analysis
Before fit the data to any model, we will use scatter plot to see how the data points are distributed and diagnose any association. Then we can fit it into a model.


### Results
The summary of lm() can show some results of the estimates of linear model parameters and predictions of the response. The plot of the Generalized Linear Model will help visualize a relationship.




### References

"US Department of Transportation - 2015 Flight Delays and Cancellations." Kaggle Inc. Accessed January 15, 2020. <https://www.kaggle.com/usdot/flight-delays#flights.csv>
