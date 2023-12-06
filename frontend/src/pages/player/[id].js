import React, { useState, useEffect } from 'react';
import { useRouter } from "next/router";
import { getPlayerByID } from '../api/api';
import PlayerBio from '../../../components/PlayerBio';
import PasserLogsView from '../../../components/PasserLogsView';
import ReceiverLogsView from '../../../components/ReceiverLogsView';
import RusherLogsView from '../../../components/RusherLogsView';

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
          {data ? (
            <div>              
              {data.position === 'QB' && <PasserLogsView id={data.player_id} />}
              {(data.position === 'WR' || data.position === 'TE')  && <ReceiverLogsView id={data.player_id} />}
              {data.position === 'RB' && <RusherLogsView id={data.player_id} />}
              {!(data.position === 'RB' || data.position === 'WR'|| data.position === 'QB' || data.position === 'TE') && <p>No game logs available for this position</p>}
            </div>
          ) : (
            <p>Loading...</p>
          )}
          
          {/* <div>
            <PasserLogsView
             passing_log_id={1}
             game_id={1}
             player_id={1}
             completions={69}
             attempts={69}
             yards={69}
             touchdowns={69}
             interceptions={69}
             fantasy_points={69}/>
          </div> */}
        </div>
        
      );

    
};

export default PlayerDetails;