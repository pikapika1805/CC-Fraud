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

@app.route('/merchant_data', methods=['GET'])
def get_merchant_data():
    conn = get_sqlite_connection()
    
    # SQL query for aggregation
    query = """
    SELECT merchant, 
           merch_lat, 
           merch_long, 
           category, 
           is_fraud, 
           COUNT(*) as count, 
           SUM(amt) as total_amount
    FROM df
    GROUP BY merchant, merch_lat, merch_long, category, is_fraud
    """
    
    # Execute query and load results into DataFrame
    result_df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    # Convert DataFrame to dictionary
    return jsonify(result_df.to_dict(orient="records"))

@app.route('/query', methods=['GET'])
def query_data():
    column = request.args.get('column')
    value = request.args.get('value')
    
    if column and value:
        filtered_df = df[df[column] == value]
        filtered_df = filtered_df.replace({np.nan: None})
        return jsonify(filtered_df.to_dict(orient="records"))
    else:
        return jsonify({"error": "Please provide both 'column' and 'value' parameters"}), 400

if __name__ == '__main__':
    app.run(debug=True)
