import React, { useEffect, useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer, Label } from 'recharts';
import axios from 'axios';

const AgeFraudChart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/age_cardholder_both')
      .then(response => {
        // Process data: sort and limit to top 10 entries by count
        const sortedData = response.data
          .sort((a, b) => b.count - a.count) // Sort by count descending
          .slice(0, 10); // Take top 10 entries
        setData(sortedData);
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <ResponsiveContainer width="100%" height={400}>
      <BarChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="age">
          <Label value="Age Group" offset={0} position="insideBottom" />
        </XAxis>
        <YAxis>
          <Label value="Count" angle={-90} position="insideLeft" />
        </YAxis>
        <Tooltip />
        {/* Bar Chart for Count */}
        <Bar dataKey="count" fill="#82ca9d" />
      </BarChart>
    </ResponsiveContainer>
  );
};

export default AgeFraudChart;
