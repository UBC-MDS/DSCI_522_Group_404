import pandas as pd


df1 = pd.read_csv('https://www.dropbox.com/s/5o9gmtpq2q8cshp/flights.csv?dl=0')

df1.to_csv('data/flights.csv')