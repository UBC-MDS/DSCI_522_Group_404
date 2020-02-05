all : doc/flight_delays_report.html

# To download the database from online, written by Jarome 
data/flights.csv :  src/load_data.R
	Rscript src/load_data.R 'https://dl.dropboxusercontent.com/s/5o9gmtpq2q8cshp/flights.csv?dl=0' 'data/flights.csv'
 
# To wrangle and clean the data, written by Mike 
data/X_original.csv data/X_test_clean.csv data/X_train_clean data/y_original data/y_test data/y_train : data/flights.csv src/dataprocessing.py 
	python src/dataprocessing.py --path_in="data/flights.csv" --path_out="data/"

# EDA script to create plots and explore the data, written by Mike	
results/chart1.png : data/flights.csv src/EDA.py 
	python src/EDA.py --path_in="data/flights.csv" --path_out="results/"

# Model script to perform classification analysis, written by Lori
results/accuracy.csv results/lgr_classification_report.csv results/csv_classification_report.csv results/hyper_parameters.csv : data/X_original.csv data/X_test_clean.csv data/X_train_clean data/y_original data/y_test data/y_train src/model.py 
	python src/model.py --data_input=data --result_output=results

# Report script to generate a final report, written by Jarome	
doc/flight_delays_report.html : results/accuracy.csv doc/flight_delays_report.ipynb results/chart1.png results/hyper_parameters.csv results/lgr_classification_report.csv results/csv_classification_report.csv 
	jupyter nbconvert doc/flight_delays_report.ipynb --to html
  
	
clean :
	rm -f data/*
	rm -f results/*.csv results/*.html results/*.png
	rm -f doc/flight_delays_report.html doc/flight_delays_report.pdf