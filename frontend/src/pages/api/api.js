// utils/api.js

import axios from 'axios';

const api = axios.create({
  headers: 'Access-Control-Allow-Origin',  
  baseURL: 'http://127.0.0.1:5000', // Replace with your API endpoint
});

export const getTeamRoster = async (abbreviation) => {
    try {
      const requestUrl = `/api/roster/${abbreviation}`
      const response = await api.get(requestUrl); // Replace with your API endpoint
    //   console.log(response);
      return response.data;
    } catch (error) {
      // Handle errors (e.g., log them or return an error message)
      console.error('Error fetching data:', error);
      throw error;
    }
  };

export const getPlayerByID = async (id) => {
    try{
        const requestUrl = `api/player/${id}`
        const response = await api.get(requestUrl);
        console.log(response);
        return response.data;
    }catch (error) {
        console.error('Error fetching data:', error);
      throw error;
    }

};
