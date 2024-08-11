import React, { useEffect } from 'react';
import { geoMercator, geoPath } from 'd3-geo';
import { select } from 'd3-selection';

const MapChart = ({ data }) => {
  const mapContainerStyle = {
    width: "100%",
    height: "400px",
    border: "1px solid #ccc",
    margin: "0 auto",
  };

  const projection = geoMercator()
    .center([0, 20])
    .scale(100)
    .translate([200, 200]);

  const pathGenerator = geoPath().projection(projection);

  useEffect(() => {
    const svg = select('#map');
    svg.selectAll('path')
      .data(data.features)
      .enter()
      .append('path')
      .attr('d', pathGenerator)
      .attr('fill', 'blue')
      .attr('stroke', 'black');
  }, [data]);

  return (
    <div style={mapContainerStyle}>
      <svg id="map" width={400} height={400}></svg>
    </div>
  );
};

export default MapChart;
