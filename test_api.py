import pytest
import requests

BASE_URL = 'http://localhost:5000'  # Adjust if your server runs on a different URL

# Test the dataset for readibilty, whether it return any value
def test_get_data():
    """Test the /data endpoint."""
    response = requests.get(f'{BASE_URL}/data')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)  # Assuming the endpoint returns a list of records
    if data:
        assert isinstance(data[0], dict)  # Each record should be a dictionary

#===== Test record sample for each api ======#
def test_get_fraud_by_date():
    """Test the /fraud_by_date endpoint."""
    response = requests.get(f'{BASE_URL}/fraud_by_date')
    assert response.status_code == 200
    data = response.json()

    # Verify that the response is a list of records
    assert isinstance(data, list)

    # Define the expected record
    expected_record = {
        "amount": 3874.2100000000005,
        "extracted_date": "2020-11-20",
        "transaction_count": 7
    }

    # Check if the expected record is in the response data
    assert any(
        record == expected_record for record in data
    ), "Expected record not found in response data"


def test_get_stats_conso_card():
    """Test the /stats_conso_card endpoint."""
    response = requests.get(f'{BASE_URL}/stats_conso_card')
    assert response.status_code == 200
    data = response.json()

    # Define the expected metric
    expected_metric = {
        "metrics": "Fraud Amount",
        "value": 923192.6499999997
    }

    # Check if the expected metric is in the response data
    assert any(
        metric == expected_metric for metric in data
    ), "Expected metric not found in response data"


def test_get_conso_metrics():
    """Test the /conso_metrics endpoint."""
    response = requests.get(f'{BASE_URL}/conso_metrics')
    assert response.status_code == 200
    data = response.json()

    # Define the expected metrics
    expected_metrics = {
        "fraud_count": 1782,
        "fraud_percentage": 12.389626642564139,
        "metrics": "Transaction Count",
        "overall_count": 14383
    }

    # Ensure the response is a list
    assert isinstance(data, list), "Response data should be a list"

    # Check if the expected metrics are in the list of records
    assert any(
        all(
            item.get(key) == value for key, value in expected_metrics.items()
        ) for item in data
    ), "Expected metrics not found or do not match in response data"

def test_get_cardholder_job_fraud():
    """Test the /cardholder_city_fraud endpoint."""
    response = requests.get(f'{BASE_URL}/job_cardholder_fraud')
    assert response.status_code == 200
    data = response.json()

    # Define the expected metrics
    expected_metrics = {   
        "amount": 2922.38,
        "count": 8,
        "job": "Tourist information centre manager"
    }

    # Ensure the response is a list
    assert isinstance(data, list), "Response data should be a list"

    # Check if the expected metrics are in the list of records
    assert any(
        all(
            item.get(key) == value for key, value in expected_metrics.items()
        ) for item in data
    ), "Expected metrics not found or do not match in response data"

def test_get_cardholder_city_fraud():
    """Test the /cardholder_city_fraud endpoint."""
    response = requests.get(f'{BASE_URL}/cardholder_city_fraud')
    assert response.status_code == 200
    data = response.json()

    # Define the expected metrics
    expected_metrics = {   
        "amt": 6191.29,
        "city": "Wales,AK",
        "count": 15
    }

    # Ensure the response is a list
    assert isinstance(data, list), "Response data should be a list"

    # Check if the expected metrics are in the list of records
    assert any(
        all(
            item.get(key) == value for key, value in expected_metrics.items()
        ) for item in data
    ), "Expected metrics not found or do not match in response data"

def test_get_age_cardholder_fraud():
    """Test the /age_cardholder_fraud endpoint."""
    response = requests.get(f'{BASE_URL}/age_cardholder_fraud')
    assert response.status_code == 200
    data = response.json()

    # Define the expected metrics
    expected_metrics = {   
        "age": 34,
        "amt": 5242.2,
        "count": 14
    }

    # Ensure the response is a list
    assert isinstance(data, list), "Response data should be a list"

    # Check if the expected metrics are in the list of records
    assert any(
        all(
            item.get(key) == value for key, value in expected_metrics.items()
        ) for item in data
    ), "Expected metrics not found or do not match in response data"

def test_get_geo_cardholder_fraud():
    """Test the /geo_cardholder_fraud."""
    response = requests.get(f'{BASE_URL}/geo_cardholder_fraud')
    assert response.status_code == 200
    data = response.json()

    # Define the expected metrics
    expected_metrics = {   
        "amount": 7807.28,
        "count": 12,
        "lat": 66.6933,
        "long": -153.994
    }

    # Ensure the response is a list
    assert isinstance(data, list), "Response data should be a list"

    # Check if the expected metrics are in the list of records
    assert any(
        all(
            item.get(key) == value for key, value in expected_metrics.items()
        ) for item in data
    ), "Expected metrics not found or do not match in response data"

#===== Test record sample for each api ======#

#===== Test logic aunthentication =======#
# Test successful login with valid credentials
def test_login_success():
    login_data = {
        'username': 'afikah_syafika',
        'password': 'we$urvived'
    }
    response = requests.post(f'{BASE_URL}/login', json=login_data)
    assert response.status_code == 200
    response_json = response.json()
    assert 'token' in response_json
    assert isinstance(response_json['token'], str)
    
# Test login with missing username or password
def test_login_missing_username():
    login_data = {
        'password': 'we$urvived'
    }
    response = requests.post(f'{BASE_URL}/login', json=login_data)
    assert response.status_code == 400
    response_json = response.json()
    assert response_json['message'] == 'Username and password are required!'

def test_login_missing_password():
    login_data = {
        'username': 'afikah_syafika'
    }
    response = requests.post(f'{BASE_URL}/login', json=login_data)
    assert response.status_code == 400
    response_json = response.json()
    assert response_json['message'] == 'Username and password are required!'

# Test login with invalid credentials
def test_login_invalid_credentials():
    login_data = {
        'username': 'invalid_user',
        'password': 'invalid_password'
    }
    response = requests.post(f'{BASE_URL}/login', json=login_data)
    assert response.status_code == 401
    response_json = response.json()
    assert response_json['message'] == 'Invalid credentials!'
