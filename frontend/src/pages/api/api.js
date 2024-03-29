import axios from 'axios';

const api = axios.create({
  headers: 'Access-Control-Allow-Origin',
  baseURL: 'http://127.0.0.1:5000',
});

export const getTeamDetails = async (abbreviation) => {
  try {
    const requestUrl = `/api/team/details/${abbreviation}`
    const response = await api.get(requestUrl);
    //   console.log(response);
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export const getTeamRoster = async (abbreviation) => {
  try {
    const requestUrl = `/api/team/roster/${abbreviation}`
    const response = await api.get(requestUrl);
    //   console.log(response);
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export const getPlayerByID = async (id) => {
  try {
    const requestUrl = `api/player/${id}`
    const response = await api.get(requestUrl);
    //console.log(response);
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }

};

export const getGamesByWeek = async (week) => {
  try {
    const requestUrl = `api/games/week/${week}`;
    const response = await api.get(requestUrl);
    // console.log(response);
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }

};

export const getGameById = async (game_id) => {
  try{
    // const requestUrl = `api/games/game/logs/${game_id}`;
    const requestUrl = `api/games/game/logs/${game_id}`;
    const response = await api.get(requestUrl);
    console.log(response);
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
}


export const getGameLogsForPlayer = async (id) => {
  try {
    const requestUrl = `api/player/logs/${id}`
    const response = await api.get(requestUrl);
    //console.log(response);
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }

};


export const getFilteredLogs = async (position, start_week, end_week, sort_by, ascending) => {
  try {
    const order = ascending ? "ascending" : "descending";
    const requestUrl = `api/player/logs/filter?position=${position}&start_week=${start_week}&end_week=${end_week}&sort_by=${sort_by}&order=${order}`;
    // console.log(requestUrl);
    const response = await api.get(requestUrl);
    //console.log(response);
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }

}
