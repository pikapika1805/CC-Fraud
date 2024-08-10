from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import sqlite3
from decimal import Decimal

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load Parquet file into a Pandas DataFrame
file_path = 'api_dataset/cc_transactions_detail.parquet'
df = pd.read_parquet(file_path)

# Convert Decimal columns to floats
def convert_decimals_to_floats(df):
    for col in df.select_dtypes(include=[object]).columns:
        if df[col].apply(lambda x: isinstance(x, Decimal)).any():
            df[col] = df[col].apply(lambda x: float(x) if isinstance(x, Decimal) else x)
    return df

df = convert_decimals_to_floats(df)
df = df.replace({np.nan: None})

# Create an SQLite in-memory database and load DataFrame into it
def get_sqlite_connection():
    conn = sqlite3.connect(':memory:')
    df.to_sql('df', conn, index=False, if_exists='replace')
    return conn

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(df.to_dict(orient="records"))

@app.route('/fraud_by_date', methods=['GET'])
def get_fraud_by_date():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT
    DATE(trans_date_trans_time) AS extracted_date,
    COUNT(trans_num) AS transaction_count,
    SUM(amt) AS amount
    FROM df
    WHERE is_fraud = 'fraud'
    GROUP BY extracted_date
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/cat_fraud_only', methods=['GET'])
def get_cat_fraud_only():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT category, count(*) as count, sum(amt) 
    FROM df 
    WHERE is_fraud = 'fraud' 
    GROUP BY 1
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/cat_all', methods=['GET'])
def get_cat_all():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT category, count(*) as count, sum(amt) 
    FROM df 
    WHERE is_fraud = 'fraud' 
    GROUP BY 1
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))
    
@app.route('/merchant_geo_fraud', methods=['GET'])
def get_merchant_geo_fraud():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT merch_lat, 
           merch_long, 
           COUNT(*) as count, 
           SUM(amt) as amount
    FROM df
    WHERE is_fraud = 'fraud' 
    GROUP BY merch_lat, merch_long
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/fraud_stats', methods=['GET'])
def get_fraud_stats():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT is_fraud as fraudulent_status, 
           COUNT(*) as count, 
           SUM(amt) as amount
    FROM df
    WHERE is_fraud = 'fraud' 
    GROUP BY 1
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/not_fraud_stats', methods=['GET'])
def get_not_fraud_stats():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT is_fraud as fraudulent_status, 
           COUNT(*) as count, 
           SUM(amt) as amount
    FROM df
    WHERE is_fraud != 'fraud' 
    GROUP BY 1
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/both_fraud_stats', methods=['GET'])
def get_both_fraud_stats():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT is_fraud as fraudulent_status, 
           COUNT(*) as count, 
           SUM(amt) as amount
    FROM df
    GROUP BY 1
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/geo_cardholder_fraud', methods=['GET'])
def get_geo_cardholder_fraud():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT lat, long, count(*) as count, SUM(amt) as amount
    FROM df 
    WHERE is_fraud = 'fraud' 
    GROUP BY 1,2
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/geo_cardholder_both', methods=['GET'])
def get_geo_cardholder_both():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT lat, long, is_fraud, count(*) as count, SUM(amt) as amount
    FROM df 
    GROUP BY 1,2,3
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/job_cardholder_fraud', methods=['GET'])
def get_job_cardholder_fraud():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT job, count(*) as count, SUM(amt) as amount
    FROM df 
    WHERE is_fraud = 'fraud' 
    GROUP BY 1
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/job_cardholder_both', methods=['GET'])
def get_job_cardholder_both():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT job, is_fraud, count(*) as count, SUM(amt) as amount
    FROM df 
    GROUP BY 1,2
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))
    

@app.route('/cardholder_city_fraud', methods=['GET'])
def get_cardholder_city_fraud():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT
        city || ',' || state AS city,
        COUNT(*) AS count,
        SUM(amt) AS amt
    FROM df
    WHERE is_fraud = 'fraud'
    GROUP BY 1
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/cardholder_city_both', methods=['GET'])
def get_cardholder_city_both():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT
        city || ',' || state AS city,
        is_fraud,
        COUNT(*) AS count,
        SUM(amt) AS amt
    FROM df
    GROUP BY 1,2
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/age_cardholder_fraud', methods=['GET'])
def get_age_cardholder_fraud():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT
        (2024 - SUBSTR(dob, 1, 4)) AS age, 
        COUNT(*) AS count,
        SUM(amt) AS amt
    FROM df
    WHERE is_fraud = 'fraud'
    GROUP BY 1
    ORDER BY 1 DESC
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/age_cardholder_both', methods=['GET'])
def get_age_cardholder_both():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT
        (2024 - SUBSTR(dob, 1, 4)) AS age, is_fraud,
        COUNT(*) AS count,
        SUM(amt) AS amt
    FROM df
    -- WHERE is_fraud = 'fraud'
    GROUP BY 1,2
    ORDER BY 1 DESC
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/conso_metrics', methods=['GET'])
def get_conso_metrics():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
         SELECT
            CASE WHEN is_fraud IS NOT NULL THEN "Transaction Count" END as metrics,
            COUNT(*) AS overall_count,
            SUM(CASE WHEN is_fraud = 'fraud' THEN 1 ELSE 0 END) AS fraud_count,
            (SUM(CASE WHEN is_fraud = 'fraud' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS fraud_percentage
        FROM df
        GROUP BY 1
        
        UNION 
        
        SELECT
            'Merchant' AS metrics,
            (SELECT COUNT(DISTINCT merchant) FROM df) AS overall_count,
            (SELECT COUNT(DISTINCT merchant) FROM df WHERE is_fraud = 'fraud') AS fraud_count,
            (SELECT COUNT(DISTINCT merchant) FROM df WHERE is_fraud = 'fraud') * 100.0 / (SELECT COUNT(DISTINCT merchant) FROM df) AS fraud_percentage
        FROM df
        
        UNION 
        
        SELECT
            'city' AS metrics,
            (SELECT COUNT(DISTINCT city) FROM df) AS overall_count,
            (SELECT COUNT(DISTINCT city) FROM df WHERE is_fraud = 'fraud') AS fraud_count,
            (SELECT COUNT(DISTINCT city) FROM df WHERE is_fraud = 'fraud') * 100.0 / (SELECT COUNT(DISTINCT city) FROM df) AS fraud_percentage
        FROM df
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))



# @app.route('/query', methods=['GET'])
# def query_data():
#     column = request.args.get('column')
#     value = request.args.get('value')
    
#     if column and value:
#         filtered_df = df[df[column] == value]
#         filtered_df = filtered_df.replace({np.nan: None})
#         return jsonify(filtered_df.to_dict(orient="records"))
#     else:
#         return jsonify({"error": "Please provide both 'column' and 'value' parameters"}), 400

if __name__ == '__main__':
    app.run(debug=True)
