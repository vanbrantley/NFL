import React, { useState, useEffect } from 'react';
import { useRouter } from "next/router";
import { getTeamRoster } from './../api/api';
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

        <div>
          <RosterTab data={data} />
        </div>
    );
};

export default TeamDetails;