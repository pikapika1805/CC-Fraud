import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import { styled } from '@mui/material/styles';

// Styled components for larger font size
const StyledTableCell = styled(TableCell)(({ theme }) => ({
  fontSize: '1.5rem',
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  '&:nth-of-type(odd)': {
    backgroundColor: theme.palette.action.hover,
  },
}));

const MetricsTable = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/conso_metrics')
      .then(response => setData(response.data))
      .catch(error => console.error('Error fetching metrics:', error));
  }, []);

  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <StyledTableCell>Metrics</StyledTableCell>
            <StyledTableCell>Overall Count</StyledTableCell>
            <StyledTableCell>Fraud Count</StyledTableCell>
            <StyledTableCell>Fraud Percentage (%)</StyledTableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((row, index) => (
            <StyledTableRow key={index}>
              <StyledTableCell>{row.metrics}</StyledTableCell>
              <StyledTableCell>{row.overall_count}</StyledTableCell>
              <StyledTableCell>{row.fraud_count}</StyledTableCell>
              <StyledTableCell>{row.fraud_percentage.toFixed(2)}</StyledTableCell>
            </StyledTableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default MetricsTable;
