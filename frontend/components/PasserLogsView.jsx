import { getGameLogsForPlayer } from "@/pages/api/api";
import { useState, useEffect } from "react";

const PasserLogsView = ({ id }) => {

  const [data, setData] = useState(null);

  useEffect(() => {
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
  }, [id]);

  return (
    <div>

      {data ? (
        <div>
          <h2 className="text-lg font-semibold mb-4">Passing Logs</h2>

          <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md transition-transform transform">
            <div className="grid grid-cols-8 gap-4">

              <div className="flex justify-center">
                <p style={{ fontWeight: "bold" }}>Week</p>
              </div>
              <div className="flex justify-center">
                <p style={{ fontWeight: "bold" }}>Opponent</p>
              </div>
              <div className="flex justify-center">
                <p style={{ fontWeight: "bold" }}>Completions</p>
              </div>
              <div className="flex justify-center">
                <p style={{ fontWeight: "bold" }}>Attempts</p>
              </div>
              <div className="flex justify-center">
                <p style={{ fontWeight: "bold" }}>Yards</p>
              </div>
              <div className="flex justify-center">
                <p style={{ fontWeight: "bold" }}>Touchdowns</p>
              </div>
              <div className="flex justify-center">
                <p style={{ fontWeight: "bold" }}>Interceptions</p>
              </div>
              <div className="flex justify-center">
                <p style={{ fontWeight: "bold" }}>Fantasy Points</p>
              </div>

              {data.map((log, i) => {

                const { passing_log_id, game_id, week, opponent, player_id, completions, attempts, yards, touchdowns, interceptions, fantasy_points } = log;

                return (
                  <>

                    <div className="flex justify-center">
                      <p>{week}</p>
                    </div>
                    <div className="flex justify-center items-center">
                      <p>{opponent}</p>
                      <img
                        src={`/images/team-logos/${opponent}.png`}
                        height="30px"
                        width="30px"
                      />
                    </div>
                    <div className="flex justify-center">
                      <p>{completions}</p>
                    </div>
                    <div className="flex justify-center">
                      <p>{attempts}</p>
                    </div>
                    <div className="flex justify-center">
                      <p>{yards}</p>
                    </div>
                    <div className="flex justify-center">
                      <p>{touchdowns}</p>
                    </div>
                    <div className="flex justify-center">
                      <p>{interceptions}</p>
                    </div>
                    <div className="flex justify-center">
                      <p>{fantasy_points}</p>
                    </div>

                  </>

                );

              })}

            </div>
          </div>

        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>

  );
}

export default PasserLogsView;