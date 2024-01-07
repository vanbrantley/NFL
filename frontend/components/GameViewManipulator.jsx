import { getGamesByWeek } from "@/pages/api/api";
import { useState, useEffect } from "react";
import SmallGameView from "./SmallGameView";
import Select from 'react-select';
import Link from "next/link";


const GameViewManipulator = () => {

    const [week, setWeek] = useState(1);
    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await getGamesByWeek(week);
            console.log(response);
            setData(response);
          } catch (error) {
            // Handle the error, e.g., display an error message
          }
        };
    
        fetchData();
      }, [week]);

      const weekOptions = [
        { value: 1, label: '1' },
        { value: 2, label: '2' },
        { value: 3, label: '3' },
        { value: 4, label: '4' },
        { value: 5, label: '5' },
        { value: 6, label: '6' },
        { value: 7, label: '7' },
        { value: 8, label: '8' },
        { value: 9, label: '9' },
        { value: 10, label: '10' },
        { value: 11, label: '11' },
        { value: 12, label: '12' },
        { value: 13, label: '13' },
        { value: 14, label: '14' },
        { value: 15, label: '15' },
      ];

      const handleWeekSelect = (e) => {
        setWeek(e.value);
      };

      return(
        <div>
            <div className="flex flex-grow items-center justify-center space-x-4">
                <p>Week: </p>
                <Select options={weekOptions} value={weekOptions.find(option => option.value === week)} onChange={handleWeekSelect} />
            </div>

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

export default GameViewManipulator;
