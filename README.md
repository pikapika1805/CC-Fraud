# CC-Fraud
All related documentation. Code-base for Credit Card Dashboard
For more documentation, please visit - https://github.com/pikapika1805/CC-Fraud/wiki

Dataset used - https://www.kaggle.com/datasets/neharoychoudhury/credit-card-fraud-data/data

# Pre-requisites Installation
1. Create Virtual Environment
 run `python -m venv venv`
2. Create Virtual Environment
 venv\Scripts\activate
3. Install Required Packages
 pip install pandas flask

# Run API 
1. Execute API for Main Dataset
`python api1.py`
2. Call API to Retrieve Entire Dataset
`curl "http://localhost:5000/data"`
3. To Call API to Query Dataset
 `curl "http://localhost:5000/query?column=<column_name>&value=<value_name>"`

 # How to Start the Web-based Dashboard
1. Navigate to Frontend Directory
 `cd frontend`
2. Install Dependencies
 `npm install`
3. Start React App
 `npm start`

# API lists:
- Fraud by date - `curl "http://localhost:5000/fraud_by_date"`
- Category count and amount (fraud only) - `curl "http://localhost:5000/cat_fraud_only"`
- Category count and amount (fraud & non fraud) - `curl "http://localhost:5000/cat_all"`
- Merchant geo (fraud only) - `curl "http://localhost:5000/merchant_geo_fraud"`
- Fraud stats - `curl "http://localhost:5000/fraud_stats"`
- Not Fraud stats - `curl "http://localhost:5000/not_fraud_stats"`
- Stats group by is_fraud - `curl "http://localhost:5000/both_fraud_stats"`
- Geo Cardholder (fraud) - ` curl "http://localhost:5000/geo_cardholder_fraud"`
- Geo Cardholder (fraud & non fraud) - ` curl "http://localhost:5000/geo_cardholder_both"`
- Job Cardholder (fraud) - `curl "http://localhost:5000/job_cardholder_fraud"`
- Job Cardholder (fraud & non fraud) - `curl "http://localhost:5000/job_cardholder_both"`
- City Cardholder (fraud) - `curl "http://localhost:5000/cardholder_city_fraud"`
- City Cardholder (fraud & non fraud) - `curl "http://localhost:5000/cardholder_city_both"`
- Age cardholder (fraud) - `curl "http://localhost:5000/age_cardholder_fraud"`
- Age cardholder (fraud & non fraud) - `curl "http://localhost:5000/age_cardholder_both"`
- Consolidated statitical metrics - `curl "http://localhost:5000/conso_metrics"`
- Consolidated Transactions Fraud metrics - `curl "http://localhost:5000/stats_conso_card"`

