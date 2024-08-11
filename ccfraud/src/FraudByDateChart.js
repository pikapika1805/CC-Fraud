import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer, Label } from 'recharts';
import axios from 'axios';

const FraudByDateChart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/fraud_by_date')
      .then(response => {
        const sortedData = response.data.sort((a, b) => b.transaction_count - a.transaction_count);
        const top10Data = sortedData.slice(0, 10); // Select top 10 records
        setData(top10Data);
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis 
          dataKey="extracted_date" 
          tickFormatter={(date) => new Date(date).toLocaleDateString()}
        >
          <Label value="Date" offset={0} position="insideBottom" />
        </XAxis>
        <YAxis 
          yAxisId="left" 
          domain={[5000, 10000]} // Set domain for Amount
        >
          <Label value="Amount" angle={-90} position="insideLeft" />
        </YAxis>
        <YAxis 
          yAxisId="right" 
          orientation="right"
          domain={['auto', 'auto']} // Auto range for Transaction Count
        >
          <Label value="Transaction Count" angle={-90} position="insideRight" />
        </YAxis>
        <Tooltip />
        <Line 
          type="monotone" 
          dataKey="transaction_count" 
          stroke="#8884d8" 
          name="Transaction Count"
          yAxisId="right"
        />
        <Line 
          type="monotone" 
          dataKey="amount" 
          stroke="#82ca9d" 
          name="Amount" 
          yAxisId="left"
        />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default FraudByDateChart;
