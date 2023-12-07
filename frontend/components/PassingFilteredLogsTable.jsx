import Link from "next/link";

const PassingFilteredLogsTable = ({ data, renderHeader }) => {

    return (

        <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md transition-transform transform">
            <div className="grid grid-cols-8 gap-4">
                {renderHeader('rank', 'Rank')}
                {renderHeader('player', 'Player')}
                {renderHeader('completions', 'Completions')}
                {renderHeader('attempts', 'Attempts')}
                {renderHeader('yards', 'Yards')}
                {renderHeader('touchdowns', 'Touchdowns')}
                {renderHeader('interceptions', 'Interceptions')}
                {renderHeader('fantasy_points', 'Fantasy Points')}
            </div>

            {data.map((result, i) => {

                const { player_id, player_name, image_url, total_attempts, total_completions,
                    total_yards, total_touchdowns, total_interceptions, total_fantasy_points } = result;

                return (
                    <Link href={`/player/${player_id}`}>
                        <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md hover:shadow-lg  transition-transform transform hover:-translate-y-1">

                            <div className="grid grid-cols-8 gap-4">

                                <div className="flex justify-center items-center">
                                    <p>{i + 1}</p>
                                </div>
                                <div className="flex justify-center items-center">
                                    {image_url && <img
                                        src={`${image_url}`}
                                        alt="Player Icon"
                                        className="w-50 h-50 mb-2"
                                    />}
                                    <p>{player_name}</p>
                                </div>
                                <div className="flex justify-center items-center">
                                    <p>{total_completions}</p>
                                </div>
                                <div className="flex justify-center items-center">
                                    <p>{total_attempts}</p>
                                </div>
                                <div className="flex justify-center items-center">
                                    <p>{total_yards}</p>
                                </div>
                                <div className="flex justify-center items-center">
                                    <p>{total_touchdowns}</p>
                                </div>
                                <div className="flex justify-center items-center">
                                    <p>{total_interceptions}</p>
                                </div>
                                <div className="flex justify-center items-center">
                                    <p>{total_fantasy_points}</p>
                                </div>
                            </div>
                        </div>
                    </Link>
                )
            })}

        </div>
    );

}

export default PassingFilteredLogsTable;