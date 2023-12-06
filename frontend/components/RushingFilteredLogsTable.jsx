import Link from "next/link";

const RushingFilteredLogsTable = ({ data }) => {

    return (

        <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md transition-transform transform">
            <div className="grid grid-cols-6 gap-4">
                <div className="flex justify-center col-span-1">
                    <p>Rank</p>
                </div>
                <div className="flex justify-center col-span-1">
                    <p>Player</p>
                </div>
                <div className="flex justify-center col-span-1">
                    <p>Carries</p>
                </div>
                <div className="flex justify-center col-span-1">
                    <p>Yards</p>
                </div>
                <div className="flex justify-center col-span-1">
                    <p>Touchdowns</p>
                </div>
                <div className="flex justify-center col-span-1">
                    <p>Fantasy Points</p>
                </div>
            </div>

            {data.map((result, i) => {

                const { player_id, player_name, image_url, total_carries,
                    total_yards, total_touchdowns, total_fantasy_points } = result;

                return (
                    <Link href={`/player/${player_id}`}>
                        <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md hover:shadow-lg  transition-transform transform hover:-translate-y-1">

                            <div className="grid grid-cols-6 gap-4">

                                <div className="flex justify-center items-center">
                                    <p>{i + 1}</p>
                                </div>
                                <div className="flex justify-center items-center">
                                    <img
                                        src={`${image_url}`}
                                        alt="Player Icon"
                                        className="w-50 h-50 mb-2"
                                    />
                                    <p>{player_name}</p>
                                </div>
                                <div className="flex justify-center items-center">
                                    <p>{total_carries}</p>
                                </div>
                                <div className="flex justify-center items-center">
                                    <p>{total_yards}</p>
                                </div>
                                <div className="flex justify-center items-center">
                                    <p>{total_touchdowns}</p>
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

export default RushingFilteredLogsTable;