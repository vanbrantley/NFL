import { useState, useEffect } from "react";
import { useRouter } from "next/router";
import { getGameById } from "../api/api";



const GameDetails = () => {
    const router = useRouter();
    const { game_id } = router.query;
  
    const [data, setData] = useState(null);
  
    useEffect(() => {
      if (game_id) {
        console.log(game_id);
        const fetchData = async () => {
          try {
            const response = await getGameById(game_id);
            console.log(response);
            setData(response);
          } catch (error) {
            console.error("Error fetching game data:", error);
          }
        };
  
        fetchData();
      }
    }, [game_id]);  

    const categorizeLogsByTeam = (logs) => {
      const categorizedLogs = {};
      logs.forEach((log) => {
        const teamId = log.team_id;
        if (!categorizedLogs[teamId]) {
          categorizedLogs[teamId] = [];
        }
        categorizedLogs[teamId].push(log);
      });
      return categorizedLogs;
    };

    return (
        <div>
            {data ? (

              <div>
                {/* const passingLogsByTeam = categorizeLogsByTeam(data.passing);
                const categorizeLogsByTeam(data.receiving) = categorizeLogsByTeam(data.receiving);
                const categorizeLogsByTeam(data.rushing) = categorizeLogsByTeam(data.rushing); */}
      
                {/* Display passing logs by team */}
                <h2>Passing Logs:</h2>
                {Object.keys(categorizeLogsByTeam(data.passing)).map((teamId) => (
                  <div key={teamId}>
                    <h3>Team ID: {teamId}</h3>
                    {categorizeLogsByTeam(data.passing)[teamId].map((passingLog, index) => (
                      <div key={index}>
                        <p>{passingLog.player_name}</p>
                        {/* Display other passing log details */}
                      </div>
                    ))}
                  </div>
                ))}
      
                {/* Display receiving logs by team */}
                <br></br>
                <h2>Receiving Logs:</h2>
                {Object.keys(categorizeLogsByTeam(data.receiving)).map((teamId) => (
                  <div key={teamId}>
                    <h3>Team ID: {teamId}</h3>
                    {categorizeLogsByTeam(data.receiving)[teamId].map((receivingLog, index) => (
                      <div key={index}>
                        <p>{receivingLog.player_name}</p>
                        {/* Display other receiving log details */}
                      </div>
                    ))}
                  </div>
                ))}
      
                {/* Display rushing logs by team */}
                <br></br>
                <h2>Rushing Logs:</h2>
                {Object.keys(categorizeLogsByTeam(data.rushing)).map((teamId) => (
                  <div key={teamId} className="bg-gray-100 rounded-lg p-4 m-2 shadow-md hover:shadow-lg transition-transform transform hover:-translate-y-1">
                    <h3>Team ID: {teamId}</h3>
                    {categorizeLogsByTeam(data.rushing)[teamId].map((rushingLog, index) => (
                      <div key={index}>
                        <p>{rushingLog.player_name}: {rushingLog.carries} carries, {rushingLog.yards} yards </p>

                        {/* Display other rushing log details */}
                      </div>
                    ))}
                  </div>
                ))}
            </div>  
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default GameDetails;