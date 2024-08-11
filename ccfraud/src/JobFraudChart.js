import React, { useEffect, useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from 'recharts';
import axios from 'axios';

const JobFraudChart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/job_cardholder_both')
      .then(response => {
        const sortedData = response.data
          .sort((a, b) => b.amount - a.amount)
          .slice(0, 10);
        setData(sortedData);
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <ResponsiveContainer width="100%" height={400}>
      <BarChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="job" />
        <YAxis yAxisId="left" orientation="left" label={{ value: 'Amount', angle: -90, position: 'insideLeft' }} />
        <YAxis yAxisId="right" orientation="right" label={{ value: 'Count', angle: 90, position: 'insideRight' }} />
        <Tooltip />
        {/* Bar Chart for Amount */}
        <Bar yAxisId="left" dataKey="amount" fill="#8884d8" name="Amount" />
        {/* Vertical Bar Chart for Count */}
        <Bar yAxisId="right" dataKey="count" fill="#82ca9d" name="Count" barSize={20} />
      </BarChart>
    </ResponsiveContainer>
  );
};

export default JobFraudChart;
