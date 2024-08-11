import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Card, CardContent, Typography, Grid } from '@mui/material';

const pastelColors = {
  totalTransactions: '#fce4ec', // Light pink
  fraudCount: '#b3e5fc', // Light purple
  fraudAmount: '#b2dfdb', // Light teal
  fraudPercentage: '#ffe0b2', // Light orange
};

const MetricsCards = () => {
  const [metrics, setMetrics] = useState({
    fraudAmount: 0,
    fraudCount: 0,
    fraudPercentage: 0,
    totalTransactions: 0
  });

  useEffect(() => {
    axios.get('http://localhost:5000/stats_conso_card')
      .then(response => {
        const data = response.data;
        const metrics = {
          fraudAmount: data.find(item => item.metrics === 'Fraud Amount')?.value || 0,
          fraudCount: data.find(item => item.metrics === 'Fraud Count')?.value || 0,
          fraudPercentage: data.find(item => item.metrics === 'Fraud Percentage')?.value || 0,
          totalTransactions: data.find(item => item.metrics === 'Transaction Count')?.value || 0
        };
        setMetrics(metrics);
      })
      .catch(error => console.error('Error fetching metrics:', error));
  }, []);

  return (
    <Grid container spacing={3}>
      <Grid item xs={12} sm={3}>
        <Card style={{ backgroundColor: pastelColors.totalTransactions }}>
          <CardContent>
            <Typography variant="h6">TOTAL TRANSACTIONS</Typography>
            <Typography variant="h3">{Math.round(metrics.totalTransactions)}</Typography>
          </CardContent>
        </Card>
      </Grid>
      <Grid item xs={12} sm={3}>
        <Card style={{ backgroundColor: pastelColors.fraudCount }}>
          <CardContent>
            <Typography variant="h6">FRAUD COUNT</Typography>
            <Typography variant="h3">{Math.round(metrics.fraudCount)}</Typography>
          </CardContent>
        </Card>
      </Grid>
      <Grid item xs={12} sm={3}>
        <Card style={{ backgroundColor: pastelColors.fraudAmount }}>
          <CardContent>
            <Typography variant="h6">FRAUD AMOUNT</Typography>
            <Typography variant="h3">${metrics.fraudAmount.toLocaleString()}</Typography>
          </CardContent>
        </Card>
      </Grid>
      <Grid item xs={12} sm={3}>
        <Card style={{ backgroundColor: pastelColors.fraudPercentage }}>
          <CardContent>
            <Typography variant="h6">FRAUD PERCENTAGE</Typography>
            <Typography variant="h3">{metrics.fraudPercentage.toFixed(2)}%</Typography>
          </CardContent>
        </Card>
      </Grid>
    </Grid>
  );
};

export default MetricsCards;
