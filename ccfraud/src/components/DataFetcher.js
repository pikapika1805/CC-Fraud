import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DataFetcher = () => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://localhost:5000/query'); // Update with the correct API endpoint
                setData(response.data);
                setLoading(false);
            } catch (err) {
                setError(err);
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading data: {error.message}</p>;

    return (
        <div>
            <h1>Merchant Data</h1>
            <table>
                <thead>
                    <tr>
                        <th>Merchant</th>
                        <th>Latitude</th>
                        <th>Longitude</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((item, index) => (
                        <tr key={index}>
                            <td>{item.merchant}</td>
                            <td>{item.merch_lat}</td>
                            <td>{item.merch_long}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default DataFetcher;
