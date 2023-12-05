import { getGameLogsForPlayer } from "@/pages/api/api";
import { useState, useEffect } from "react";


const PasserLogsView = ({id}) => {


    const [data, setData] = useState(null);

    useEffect(() => {
        // Check if team is defined before making the API request
        if (id) {
          console.log(id);
          const fetchData = async () => {
            try {
              const response = await getGameLogsForPlayer(id);
              console.log(response);
              setData(response);
            } catch (error) {
              // Handle the error, e.g., display an error message
            }
          };
    
          fetchData();
        }
      }, [id]); // Add player as a dependency


    return(
        <div>

         {data ? (
            <div>
                <h2 className="text-lg font-semibold mb-4">Quarterback Log</h2>

                {data.map((log, i) => (

                <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md hover:shadow-lg transition-transform transform hover:-translate-y-1">
                <p>Passing Log ID: {log.passing_log_id}</p>
                <p>Game ID: {log.game_id}</p>
                <p>Player ID: {log.player_id}</p>
                <div className="grid grid-cols-2 gap-4">
                    <div>
                    <p>Completions: {log.completions}</p>
                    <p>Attempts: {log.attempts}</p>
                    <p>Yards: {log.yards}</p>
                    </div>
                    <div>
                    <p>Touchdowns: {log.touchdowns}</p>
                    <p>Interceptions: {log.interceptions}</p>
                    <p>Fantasy Points: {log.fantasy_points}</p>
                    </div>
                </div>
                </div>

))}

            </div>
          ) : (
            <p>Loading...</p>
          )} 
        </div>
        // <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md hover:shadow-lg transition-transform transform hover:-translate-y-1">
        // <h2 className="text-lg font-semibold mb-4">Quarterback Log</h2>
        // <p>Passing Log ID: {passing_log_id}</p>
        // <p>Game ID: {game_id}</p>
        // <p>Player ID: {player_id}</p>
        // <div className="grid grid-cols-2 gap-4">
        //     <div>
        //     <p>Completions: {completions}</p>
        //     <p>Attempts: {attempts}</p>
        //     <p>Yards: {yards}</p>
        //     </div>
        //     <div>
        //     <p>Touchdowns: {touchdowns}</p>
        //     <p>Interceptions: {interceptions}</p>
        //     <p>Fantasy Points: {fantasy_points}</p>
        //     </div>
        // </div>
        // </div>

    );
}

export default PasserLogsView;