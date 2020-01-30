all : doc/flight_delays_report.html

data/flights.csv :  src/load_data.R
	Rscript src/load_data.R 'https://dl.dropboxusercontent.com/s/5o9gmtpq2q8cshp/flights.csv?dl=0' 'data/flights.csv'
  
data/X_original.csv data/X_test_clean.csv data/X_train_clean data/y_original data/y_test data/y_train : data/flights.csv src/dataprocessing.py 
	python src/dataprocessing.py --path_in="data/flights.csv" --path_out="data/"
	
results/chart1.html : data/flights.csv src/EDA.py 
	python src/EDA.py --path_in="data/flights.csv" --path_out="results/"

results/accuracy.csv results/lgr_classification_report.csv results/csv_classification_report.csv results/hyper_parameters.csv : data/X_original.csv data/X_test_clean.csv data/X_train_clean data/y_original data/y_test data/y_train src/model.py 
	python src/model.py --data_input=data --result_output=results
	
doc/flight_delays_report.html : results/accuracy.csv doc/flight_delays_report.ipynb results/chart1.html results/hyper_parameters.csv results/lgr_classification_report.csv results/csv_classification_report.csv 
	jupyter nbconvert doc/flight_delays_report.ipynb --to html
  
	
clean :
	rm -f data/*
	rm -f results/*.csv results/*.html
	rm -f doc/flight_delays_report.html