import React, { useState, useEffect } from 'react';
import { useRouter } from "next/router";
import { getTeamDetails, getTeamRoster } from './../api/api';
import RosterTab from '../../../components/RosterTab';

const TeamDetails = () => {

  const router = useRouter();
  const { team } = router.query;

  const [teamDetails, setTeamDetails] = useState(null);
  const [roster, setRoster] = useState(null);

  useEffect(() => {
    // Check if team is defined before making the API request
    if (team) {

      const fetchTeamDetails = async () => {
        try {
          const teamDetailsResponse = await getTeamDetails(team);
          console.log(teamDetailsResponse);
          setTeamDetails(teamDetailsResponse);
        } catch (error) {
          // Handle the error, e.g., display an error message
        }
      };

      const fetchRoster = async () => {
        try {
          const rosterResponse = await getTeamRoster(team);
          //   console.log(rosterResponse);
          setRoster(rosterResponse);
        } catch (error) {
          // Handle the error, e.g., display an error message
        }
      };

      fetchTeamDetails();
      fetchRoster();

    }
  }, [team]); // Add team as a dependency


  return (

    <div>

      {teamDetails && (
        <div className="flex items-center justify-center" style={{ backgroundColor: teamDetails.primary_color }}>
          <div className="flex flex-col items-center justify-center">
            <img
              src={`/images/team-logos/${team}.png`}
              height="100px"
              width="100px"
            />
            <p style={{ color: teamDetails.secondary_color, fontSize: "24px" }}>{teamDetails.full_name}</p>
          </div>
        </div>
      )}

      <RosterTab data={roster} />
    </div>
  );
};

export default TeamDetails;