import { useState, useEffect } from "react";
import { useRouter } from "next/router";
import { getGameById } from "../api/api";
import 'chart.js/auto';
import { Pie } from "react-chartjs-2";

const GameDetails = () => {
    const router = useRouter();
    const { game_id } = router.query;
  
    const [data, setData] = useState(null);
    const [homeRushingData, setHomeRushingData] = useState(null);
    const [homeReceivingData, setHomeReceivingData] = useState(null);
    const [homePassingData, setHomePassingData] = useState(null);
    const [awayRushingData, setAwayRushingData] = useState(null);
    const [awayReceivingData, setAwayReceivingData] = useState(null);
    const [awayPassingData, setAwayPassingData] = useState(null);

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

    useEffect(() => {

      if (data) {

        const homeTeamColors = [data.home_team_details.team_primary_color, data.home_team_details.team_secondary_color];
        if (data.home_team_details.team_tertiary_color !== null) {
          homeTeamColors.push(data.home_team_details.team_tertiary_color);
        }

        const awayTeamColors = [data.away_team_details.team_primary_color, data.away_team_details.team_secondary_color];
        if (data.away_team_details.team_tertiary_color !== null) {
          awayTeamColors.push(data.away_team_details.team_tertiary_color);
        }

        // filter data by team and position
        const homeRushingData = {
          // labels: ['Red', 'Blue', 'Yellow'],
          labels: data.home_rushing.map((entry) => entry.player_name),
          datasets: [{
            data: data.home_rushing.map((entry) => entry.carries),
            backgroundColor: homeTeamColors,
          }],
        };
        setHomeRushingData(homeRushingData);

        const homeReceivingData ={
          labels: data.home_receiving.map((entry) => entry.player_name),
          datasets: [{
            data: data.home_receiving.map((entry) => entry.receptions),
            backgroundColor: homeTeamColors,
          }],
        };
        setHomeReceivingData(homeReceivingData);

        const homePassingData = {
          labels: data.home_passing.map((entry) => entry.player_name),
          datasets: [{
            data: data.home_passing.map((entry) => entry.yards),
            backgroundColor: homeTeamColors,
          }],
        };
        setHomePassingData(homePassingData);

        const awayRushingData = {
          // labels: ['Red', 'Blue', 'Yellow'],
          labels: data.away_rushing.map((entry) => entry.player_name),
          datasets: [{
            data: data.away_rushing.map((entry) => entry.carries),
            backgroundColor: awayTeamColors,
          }],
        };
        setAwayRushingData(awayRushingData);

        const awayReceivingData ={
          labels: data.away_receiving.map((entry) => entry.player_name),
          datasets: [{
            data: data.away_receiving.map((entry) => entry.receptions),
            backgroundColor: awayTeamColors,
          }],
        };
        setAwayReceivingData(awayReceivingData);

        const awayPassingData = {
          labels: data.away_passing.map((entry) => entry.player_name),
          datasets: [{
            data: data.away_passing.map((entry) => entry.yards),
            backgroundColor: awayTeamColors,
          }],
        };
        setAwayPassingData(awayPassingData);

      }

    }, [data]);

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

    const pieData = {
      labels: ['Red', 'Blue', 'Yellow'],
      datasets: [{
        data: [10, 20, 30],
        backgroundColor: ['red', 'blue', 'yellow'],
      }],
    };

    // const homeRushingData = {
    //   // labels: ['Red', 'Blue', 'Yellow'],
    //   labels: ,
    //   datasets: [{
    //     data: [10, 20, 30],
    //     backgroundColor: ['red', 'blue', 'yellow'],
    //   }],
    // };
  
    return (
<div>

      {data && (
        <div className="flex">

        {/* Home team */}
        <div className="flex flex-col h-full w-full space-y-16">

          {/* Team info */}
          <div className="flex flex-col w-full justify-center items-center">
            <img
              src={`/images/team-logos/${data.home_team_details.team_abbreviation}.png`}
              height="30px"
              width="30px"
            />
            <p>{data.home_team_details.team_full_name}</p>
          </div>

          <div className="flex flex-col items-center justify-center w-full h-96">
            <h2>Passing</h2>
            {homePassingData && 
            <Pie data={homePassingData} 
            options={{
              plugins: {
                legend: {
                  display: false
                }
              }
            }}
            />}
          </div>
          <div className="flex flex-col items-center justify-center w-full h-96">
          <h2>Rushing</h2>
            {homeRushingData && 
            <Pie data={homeRushingData} 
            options={{
              plugins: {
                legend: {
                  display: false
                }
              }
            }}
            />}
          </div>
          <div className="flex flex-col items-center justify-center w-full h-96">
          <h2>Receiving</h2>
            {homeReceivingData && 
            <Pie data={homeReceivingData} 
            options={{
              plugins: {
                legend: {
                  display: false
                }
              }
            }}
            />}
          </div>
        </div>

        <div className="flex h-full w-full">

        {/* Away team */}
        <div className="flex flex-col h-full w-full space-y-16">

          {/* Team info */}
          <div className="flex flex-col w-full justify-center items-center">
            <img
              src={`/images/team-logos/${data.away_team_details.team_abbreviation}.png`}
              height="30px"
              width="30px"
            />
            <p>{data.away_team_details.team_full_name}</p>
          </div>

              <div className="flex flex-col items-center justify-center w-full h-96">
                <h2>Passing</h2>
                {awayPassingData && 
                <Pie data={awayPassingData}
                options={{
                  plugins: {
                    legend: {
                      display: false
                    }
                  }
                }} 
                />}
              </div>
              <div className="flex flex-col items-center justify-center w-full h-96">
                <h2>Rushing</h2>
                {awayReceivingData && 
                <Pie data={awayRushingData}
                options={{
                  plugins: {
                    legend: {
                      display: false
                    }
                  }
                }} 
                />}
              </div>
              <div className="flex flex-col items-center justify-center w-full h-96">
                <h2>Receiving</h2>
                {awayReceivingData && <Pie data={awayReceivingData} 
                options={{
                  plugins: {
                    legend: {
                      display: false
                    }
                  }
                }}
                />}
              </div>
              </div>

        </div>

      </div>
      )}
      

      </div>
    );
    
};

export default GameDetails;