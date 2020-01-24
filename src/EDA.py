

import numpy as np
import pandas as pd
import altair as alt
# from pandas_profiling import ProfileReport
from sklearn.model_selection import train_test_split

#alt.data_transformers.enable('json')
#alt.renderers.enable('notebook')


def EDA(input_path, output_path):
    data = pd.read_csv(input_path)



    # split into training/validation and testing set
    train, test = train_test_split(data, test_size=0.45)



    train.head()



    # Basic description of every column present in the dataframe
    pd.DataFrame.describe(train)



    train.shape



    # List all the columns present in the data frame
    list(train.columns.values)



    # Drop columns which aren't interesting/needed for quicker EDA. Store in temp dataframe
    temp_df = train[['AIRLINE', 'DEPARTURE_DELAY', 'DISTANCE']]



    # Full dataset takes wayyy too long for panda profiling to load 
    profiling_df = temp_df.iloc[:500000]



    # Pandas Profiling 
    #profile = ProfileReport(profiling_df, title='Pandas Profiling Report', html={'style':{'full_width':True}})


    #profile


    # > Explore the relationship between `AIRLINE` and `DEPARTURE_DELAY`

    # Group the data by AIRLINE
    dfg = temp_df.groupby(by = 'AIRLINE')



    # Average Departure Time for each AIRLINE
    average_airline_delay = dfg.aggregate('mean').loc[:,'DEPARTURE_DELAY']
    average_airline_delay



    source = pd.DataFrame({
        'AIRLINE' : average_airline_delay.keys(),
        'DEPARTURE_DELAY' : average_airline_delay
    })

    chart_1 = alt.Chart(source).mark_bar().encode(
        alt.X('AIRLINE:N'),
        alt.Y('DEPARTURE_DELAY:Q')
    ).properties(width = 500,title = "Average Departure Delay for Each Airline")



    # Group the data by MONTH
    dfm = train.groupby(by = 'MONTH')
    # Average Departure Time for each MONTH
    average_airline_month_delay = dfm.aggregate('mean').loc[:,'DEPARTURE_DELAY']

    source = pd.DataFrame({
        'MONTH' : average_airline_month_delay.keys(),
        'DEPARTURE_DELAY' : average_airline_month_delay
    })

    chart_2 = alt.Chart(source).mark_bar().encode(
        alt.X('MONTH:N'),
        alt.Y('DEPARTURE_DELAY:Q')
    ).properties(width = 500,title = "Average Departure Delay for Each Month")

    

    # >Explore the relationship between `DISTANCE` and `DEPARTURE_DELAY`

    # Since the training data frame is already shuffled
    # Drop some rows so, my computer won't crash trying to plot every single point
    df_point_plot = temp_df.iloc[:500]

    chart_3 = alt.Chart(df_point_plot).mark_circle().encode(
        alt.X('DISTANCE:Q'),
        alt.Y('DEPARTURE_DELAY:Q')
    ).properties(width = 1000,title = "Average Departure Delay for Each Airline")



    delay_df = train[['DEPARTURE_DELAY']]



    chart_4 = alt.Chart(delay_df).mark_bar().encode(
        alt.X("DEPARTURE_DELAY:Q", bin=alt.Bin(extent=[-50, 400], step=25)),
        y='count()',
    ).properties(width = 1000,title = "Departure Delay in Minutes Histogram")

    chart_1.save(output_path+'chart1.html')
    chart_2.save(output_path+'chart2.html')
    chart_3.save(output_path+'chart3.html')
    chart_4.save(output_path+'chart4.html')



