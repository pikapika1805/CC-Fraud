from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("APIExample") \
    .getOrCreate()

# Initialize Flask app
app = Flask(__name__)

# Load your DataFrame from the path
file_path = 'api_dataset'
df = spark.read.option("header", "true") \
    .option("delimiter", ",") \
    .option("quote", "\"") \
    .option("escape", "\"") \
    .csv(file_path)

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
    filtered_df = df.filter(col(column) == value)

    # Check if there are any results
    if filtered_df.count() == 0:
        return jsonify({'message': 'No records found'}), 404

    # Convert to Pandas DataFrame for easy JSON conversion
    result_df = filtered_df.toPandas()

    # Convert to JSON format
    result_json = result_df.to_json(orient='records')

    return jsonify(result_json)

# Create a route to get all data (optional)
@app.route('/data', methods=['GET'])
def get_data():
    # Convert the entire DataFrame to Pandas DataFrame for easy JSON conversion
    result_df = df.toPandas()
    result_json = result_df.to_json(orient='records')
    return jsonify(result_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
