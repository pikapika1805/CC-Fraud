import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Typography, Paper, Container, Box } from '@mui/material';

const Login = ({ setToken }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/login', {
        username,
        password,
      });
      
      const token = response.data.token;
      setToken(token);
      localStorage.setItem('token', token);
    } catch (err) {
      console.error('Login failed:', err);
      setError('Invalid username or password');
    }
  };

  return (
    <Container maxWidth="sm"> {/* Increased the maxWidth to 'sm' */}
      <Paper elevation={3} style={{ padding: '40px', marginTop: '80px' }}> {/* Increased padding and marginTop */}
        <Typography variant="h3" align="center" gutterBottom> {/* Increased the variant size */}
          Login
        </Typography>
        <form onSubmit={handleSubmit}>
          <TextField
            label="Username"
            variant="outlined"
            fullWidth
            margin="normal"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            InputProps={{ style: { fontSize: 20 } }} // Increase input text size
            InputLabelProps={{ style: { fontSize: 18 } }} // Increase label text size
          />
          <TextField
            label="Password"
            type="password"
            variant="outlined"
            fullWidth
            margin="normal"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            InputProps={{ style: { fontSize: 20 } }} // Increase input text size
            InputLabelProps={{ style: { fontSize: 18 } }} // Increase label text size
          />
          {error && (
            <Typography color="error" align="center" style={{ marginTop: '20px', fontSize: '16px' }}>
              {error}
            </Typography>
          )}
          <Box display="flex" justifyContent="center" mt={4}> {/* Increased marginTop */}
            <Button type="submit" variant="contained" color="primary" size="large" style={{ padding: '15px 30px', fontSize: '18px' }}>
              Login
            </Button>
          </Box>
        </form>
      </Paper>
    </Container>
  );
};

export default Login;
