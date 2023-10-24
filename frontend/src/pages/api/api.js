// utils/api.js

import axios from 'axios';

const api = axios.create({
  headers: 'Access-Control-Allow-Origin',  
  baseURL: 'http://127.0.0.1:5000', // Replace with your API endpoint
});

export const getPitData = async () => {
  try {
    const response = await api.get('/api/roster/PIT'); // Replace with your API endpoint
    console.log(response);
    return response.data;
  } catch (error) {
    // Handle errors (e.g., log them or return an error message)
    console.error('Error fetching data:', error);
    throw error;
  }
};
