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
  `pip install pandas flask` and `pip install pytest requests`

# Run API 
1. Execute API for Main Dataset
`python api1.py`
2. Call API to Retrieve Entire Dataset
`curl "http://localhost:5000/data"`
3. To Call API to Query Dataset
 `curl "http://localhost:5000/query?column=<column_name>&value=<value_name>"`

# QA API Testing
1. Execute API for Main Dataset
`pytest test_api.py`

 # How to Start the Web-based Dashboard
1. Navigate to Frontend Directory
 `cd ccfraud`
2. Install Dependencies
 `npm install`
3. Start React App
 `npm start`

# Dashboard Credentials
<br>For testing, please login through this credentials:
<br> Username: `afikah_syafika`
<br> Password: `we$urvived`
