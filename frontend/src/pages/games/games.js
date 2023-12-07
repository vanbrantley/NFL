import React, { useState, useEffect } from 'react';
import { getGames } from './../api/api';
import SmallGameView from '../../../components/SmallGameView';

const GamesPage = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getGames();
        console.log(response);
        setData(response);
      } catch (error) {
        // Handle the error, e.g., display an error message
        console.error('Error fetching games:', error);
      }
    };

    fetchData();
  }, []); // No dependencies, fetch once when the component mounts

  return (
    <div>
      <h2 className="text-xl font-semibold text-black">Games</h2>
      {data && data.length > 0 ? (
        <div>
          {data.map((game) => (
            <SmallGameView
              key={game.game_id}
              away_team={game.away_team_abbreviation}
              box_score_url={game.box_score_url}
              game_id={game.game_id}
              home_team={game.home_team_abbreviation}
              season={game.season}
              week={game.week}
            />
          ))}
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default GamesPage;
