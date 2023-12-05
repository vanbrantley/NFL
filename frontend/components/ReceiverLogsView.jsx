const ReceiverLogsView = ({receiving_log_id, game_id, player_id, targets, receptions, yards, touchdowns, fantasy_points}) => {
    return(
        <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md hover:shadow-lg transition-transform transform hover:-translate-y-1">
        <h2 className="text-lg font-semibold mb-4">Receiver Log</h2>
        <p>Passing Log ID: {receiving_log_id}</p>
        <p>Game ID: {game_id}</p>
        <p>Player ID: {player_id}</p>
        <div className="grid grid-cols-2 gap-4">
            <div>
            <p>Completions: {targets}</p>
            <p>Attempts: {receptions}</p>
            <p>Yards: {yards}</p>
            </div>
            <div>
            <p>Touchdowns: {touchdowns}</p>
            <p>Fantasy Points: {fantasy_points}</p>
            </div>
        </div>
        </div>

    );
}

export default ReceiverLogsView;