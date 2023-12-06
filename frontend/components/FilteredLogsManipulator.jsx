import { getFilteredLogs } from "@/pages/api/api";
import { useState, useEffect } from "react";
import PassingFilteredLogsResult from "./PassingFilteredLogsResult";
import RushingFilteredLogsResult from "./RushingFilteredLogsResult";
import ReceivingFilteredLogsResult from "./ReceivingFilteredLogsResult";

const FilteredLogsManipulator = () => {

    const [data, setData] = useState(null);
    const [position, setPosition] = useState("WR");
    const [startWeek, setStartWeek] = useState(1);
    const [endWeek, setEndWeek] = useState(2);

    useEffect(() => {
          const fetchData = async () => {
            try {
              const response = await getFilteredLogs(position, startWeek, endWeek);
              console.log(response);
              setData(response);
            } catch (error) {
              // Handle the error, e.g., display an error message
            }
          };
    
          fetchData();
      }, [position, startWeek, endWeek]);

    return (
      <div>
        <h1>Filtered Logs Manipulator Page</h1>
        {data ? (
        <div>
          {data.map((player, i) => (
            <div>

            {(position == "QB") && <PassingFilteredLogsResult />}
            {(position == "RB") && <RushingFilteredLogsResult />}
            {(position == "WR" || position == "TE") && <PassingFilteredLogsResult />}
            {!(position == "WR" || position == "TE" || position == "RB" || position == "QB") && <p>No game logs available for this position</p>}

            {/* <Player
              key={i}
              id={player.player_id}
              name={player.player_name}
              position={player.position}
              number={player.jersey_number}
              image_url={player.image_url}
            /> */}
            </div>
          ))}
        </div>
      ) : (
        <p>Loading...</p>
      )}
      </div>
    );
  };
  
  export default FilteredLogsManipulator;