import React, { useState, useEffect } from 'react';
import { useRouter } from "next/router";
import { getPlayerByID } from '../api/api';
import PlayerBio from '../../../components/PlayerBio';

const PlayerDetails = () => {

    const router = useRouter();
    const { id } = router.query;

    const [data, setData] = useState(null);

    useEffect(() => {
        // Check if team is defined before making the API request
        if (id) {
          console.log(id);
          const fetchData = async () => {
            try {
              const response = await getPlayerByID(id);
              console.log(response);
              setData(response);
            } catch (error) {
              // Handle the error, e.g., display an error message
            }
          };
    
          fetchData();
        }
      }, [id]); // Add player as a dependency


      return (
        <div>
          {/* <h1>Player Page: ${data.player_name}</h1>
          <h2>ID: {id}</h2> */}
          <h1>Player Profile</h1>
          {data ? (
            <div>              
              <PlayerBio 
              id={data.player_id}
              name={data.player_name}
              position={data.position}
              number={data.jersey_number}
              college={data.college}
              experience={data.experience}
              height={data.height}
              image_url={data.image_url}
              weight={data.weight}
              team={data.team_abbreviation}
              />
            </div>
          ) : (
            <p>Loading...</p>
          )}
          <h1>Game Logs</h1>
        </div>
        
      );

    
};

export default PlayerDetails;