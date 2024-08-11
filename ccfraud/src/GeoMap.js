import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import axios from 'axios';
import L from 'leaflet';

// Create a custom icon
const customIcon = new L.Icon({
  iconUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png',
  shadowSize: [41, 41]
});

const GeoMap = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/geo_cardholder_fraud')
      .then(response => {
        const mappedData = response.data.map(location => ({
          lat: location.lat,
          lng: location.long, // Map `long` to `lng`
          amount: location.amount,
          count: location.count
        }));
        setData(mappedData);
      })
      .catch(error => console.error('Error fetching geo data:', error));
  }, []);

  return (
    <MapContainer center={[20.0271, -155.3697]} zoom={13} style={{ height: '100%', width: '100%' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='© OpenStreetMap contributors'
      />
      {data.map((location, index) => (
        <Marker key={index} position={[location.lat, location.lng]} icon={customIcon}>
          <Popup>
            Amount: ${location.amount} <br />
            Count: {location.count}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

export default GeoMap;
