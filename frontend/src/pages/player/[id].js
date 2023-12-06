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
            team={data.team_full_name}
          />
        </div>
      ) : (
        <p>Loading...</p>
      )}
      {data ? (
        <div>
          {data.position === 'QB' && <PasserLogsView id={data.player_id} />}
          {(data.position === 'WR' || data.position === 'TE') && <ReceiverLogsView id={data.player_id} />}
          {data.position === 'RB' && <RusherLogsView id={data.player_id} />}
          {!(data.position === 'RB' || data.position === 'WR' || data.position === 'QB' || data.position === 'TE') && <p>No game logs available for this position</p>}
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>

  );


};

export default PlayerDetails;