import React, { useState, useEffect } from 'react';
import { useRouter } from "next/router";
import { getTeamRoster } from './../api/api';
import Player from '../../../components/Player';
import RosterTab from '../../../components/RosterTab';

const TeamDetails = () => {

    const router = useRouter();
    const { team } = router.query;

    const [data, setData] = useState(null);

    useEffect(() => {
        // Check if team is defined before making the API request
        if (team) {
          const fetchData = async () => {
            try {
              const response = await getTeamRoster(team);
            //   console.log(response);
              setData(response);
            } catch (error) {
              // Handle the error, e.g., display an error message
            }
          };
    
          fetchData();
        }
      }, [team]); // Add team as a dependency


    return (
        // <div>
        //     <h1 className="text-xl font-semibold text-black">Team: {team}</h1>
        //     <br></br>
        //     <h1 className='text-xl font-semibold text-black'>Roster:</h1>
        //     {data ? (
        //     <div>
        //       {/* <h2>API Data:</h2>
        //       <pre>{JSON.stringify(data, null, 2)}</pre> */}
        //       {data.map((player, i) => {
        //         return(
        //             <Player key={i} id={player.player_id} name={player.player_name} position={player.position} number={player.jersey_number} image_url={player.image_url} />
        //         );
        //       })}

        //     </div>
        //   ) : (
        //     <p>Loading...</p>
        //   )}
        // </div>
        <div>
          <RosterTab data={data}></RosterTab>
        </div>
    );
};

export default TeamDetails;