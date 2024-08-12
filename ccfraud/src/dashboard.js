import React, { useState, useEffect } from 'react';
import { Card, CardContent, Typography, IconButton, Button } from '@mui/material';
import DarkModeIcon from '@mui/icons-material/DarkMode';
import LightModeIcon from '@mui/icons-material/LightMode';
import GeoMap from './GeoMap';
import JobFraudChart from './JobFraudChart';
import CityFraudChart from './CityFraudChart';
import AgeFraudChart from './AgeFraudChart';
import FraudByDateChart from './FraudByDateChart';
import MetricsCards from './MetricsCards';
import MetricsTable from './MetricsTable';
import Login from './Login';

const Dashboard = () => {
  const [darkMode, setDarkMode] = useState(false);
  const [token, setToken] = useState(null);

  useEffect(() => {
    const savedToken = localStorage.getItem('token');
    if (savedToken) {
      setToken(savedToken);
    }
  }, []);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  const handleLogout = () => {
    setToken(null);
    localStorage.removeItem('token');
  };

  const themeStyles = {
    backgroundColor: darkMode ? '#2c3e50' : '#f0f0f0',
    color: darkMode ? 'white' : 'black',
    minHeight: '100vh',
    padding: '20px',
  };

  const cardStyles = {
    marginBottom: '20px',
    backgroundColor: darkMode ? '#34495e' : 'white',
    color: darkMode ? 'white' : 'black',
  };

  const contentStyles = {
    paddingBottom: '20px',
  };

  const iconButtonStyles = {
    backgroundColor: darkMode ? '#34495e' : '#f0f0f0',
    color: darkMode ? 'white' : 'black',
    borderRadius: '50%',
    width: '60px',
    height: '60px',
    fontSize: '24px',
  };

  const headerStyles = {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '30px',
  };

  // If the user is not authenticated, show the login form
  if (!token) {
    return <Login setToken={setToken} />;
  }

  return (
    <div style={themeStyles}>
      <div style={headerStyles}>
        <div style={{ flex: 1, display: 'flex', justifyContent: 'flex-start' }}>
          {/* Logout Button */}
          <Button variant="contained" color="secondary" onClick={handleLogout}>
            Logout
          </Button>
        </div>
        <Typography 
          variant="h2" 
          style={{
            fontWeight: 'bold',
            color: darkMode ? '#f39c12' : '#2980b9',
            textAlign: 'center',
            textTransform: 'uppercase',
            letterSpacing: '2px',
            flex: 2,
          }}
        >
          Credit Card Fraud Analysis
        </Typography>
        <div style={{ flex: 1, display: 'flex', justifyContent: 'flex-end' }}>
          {/* Toggle Button for Dark/Light Mode */}
          <IconButton
            onClick={toggleDarkMode}
            style={iconButtonStyles}
          >
            {darkMode ? <LightModeIcon /> : <DarkModeIcon />}
          </IconButton>
        </div>
      </div>

      {/* Metrics Cards */}
      <Card style={cardStyles}>
        <CardContent>
          <Typography variant="h4" style={contentStyles}>Summary Metrics</Typography>
          <MetricsCards />
        </CardContent>
      </Card>

      {/* Charts */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '20px' }}>
        <Card style={cardStyles}>
          <CardContent>
            <Typography variant="h5" style={contentStyles}>Top 10 Fraud Transaction Count & Amount by Transaction Date</Typography>
            <div style={{ height: '400px' }}>
              <FraudByDateChart />
            </div>
          </CardContent>
        </Card>
        <Card style={cardStyles}>
          <CardContent>
            <Typography variant="h5" style={contentStyles}>Detailed Metrics</Typography>
            <div style={{ height: '400px' }}>
              <MetricsTable />
            </div>
          </CardContent>
        </Card>
        <Card style={cardStyles}>
          <CardContent>
            <Typography variant="h5" style={contentStyles}>Top 10 Fraud Transaction Count & Amount by Cardholder Job</Typography>
            <div style={{ height: '400px' }}>
              <JobFraudChart />
            </div>
          </CardContent>
        </Card>
        <Card style={cardStyles}>
          <CardContent>
            <Typography variant="h5" style={contentStyles}>Top 10 Fraud Transaction Amount by Cardholder City</Typography>
            <div style={{ height: '400px' }}>
              <CityFraudChart />
            </div>
          </CardContent>
        </Card>
        <Card style={cardStyles}>
          <CardContent>
            <Typography variant="h5" style={contentStyles}>Geo Mapping of Cardholder Fraud</Typography>
            <div style={{ height: '400px' }}>
              <GeoMap />
            </div>
          </CardContent>
        </Card>
        <Card style={cardStyles}>
          <CardContent>
            <Typography variant="h5" style={contentStyles}>Top 10 Fraud Transaction Count by Cardholder Age</Typography>
            <div style={{ height: '400px' }}>
              <AgeFraudChart />
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default Dashboard;
