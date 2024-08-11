import React, { useEffect, useState } from 'react';
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer, Legend } from 'recharts';
import axios from 'axios';

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#FF5454', '#7D4C4F', '#C74C5F', '#A7C8E1', '#D4A4B3', '#B8D2C4'];

const CustomLegend = ({ payload }) => {
  return (
    <div style={{ padding: '10px', textAlign: 'left' }}>
      {payload.map((entry, index) => (
        <div key={`item-${index}`} style={{ display: 'flex', alignItems: 'center', marginBottom: '4px' }}>
          <div
            style={{
              width: '12px',
              height: '12px',
              backgroundColor: entry.payload.fill,
              marginRight: '8px'
            }}
          />
          <span>{entry.payload.name}</span>
        </div>
      ))}
    </div>
  );
};

const CityFraudChart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/cardholder_city_both')
      .then(response => {
        // Process data: sort and limit to top 10 cities by amount
        const sortedData = response.data
          .sort((a, b) => b.amt - a.amt) // Sort by amount descending
          .slice(0, 10) // Take top 10 entries
          .map(item => ({
            name: item.city,
            value: item.amt
          })); // Map to PieChart format
        setData(sortedData);
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <ResponsiveContainer width="100%" height={400}>
      <PieChart>
        <Tooltip />
        <Pie
          data={data}
          dataKey="value"
          nameKey="name"
          outerRadius={150}
          fill="#8884d8"
          label
        >
          {data.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
          ))}
        </Pie>
        <Legend
          content={<CustomLegend />}
          layout="vertical"
          align="right"
          verticalAlign="middle"
        />
      </PieChart>
    </ResponsiveContainer>
  );
};

export default CityFraudChart;
