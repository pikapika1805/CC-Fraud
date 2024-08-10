from flask import Flask, request, jsonify
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load Parquet file into a Pandas DataFrame
file_path = 'api_dataset/cc_transactions_detail.parquet'
df = pd.read_parquet(file_path)

# Display first few rows
print(df.head())

# Create a route to query the DataFrame
@app.route('/query', methods=['GET'])
def query_data():
    column = request.args.get('column')
    value = request.args.get('value')
    
    if not column or not value:
        return jsonify({'error': 'Missing column or value'}), 400

    # Check if the column exists in the DataFrame
    if column not in df.columns:
        return jsonify({'error': f'Column {column} does not exist'}), 400

    # Filter the DataFrame based on query parameters
    filtered_df = df[df[column] == value]

    # Check if there are any results
    if filtered_df.empty:
        return jsonify({'message': 'No records found'}), 404

    # Convert to JSON format
    result_json = filtered_df.to_json(orient='records')

    return jsonify(result_json)

# Create a route to get all data (optional)
@app.route('/data', methods=['GET'])
def get_data():
    # Convert the entire DataFrame to JSON format
    result_json = df.to_json(orient='records')
    return jsonify(result_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
