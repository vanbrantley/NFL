const PlayerBio = ({ id, name, position, number, college, experience, height, image_url, weight, team_abbreviation, team_full_name, team_primary_color }) => {
    return (
        <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md transition-transform transform">
            <div className="flex flex-col items-center">
                <img
                    src={`${image_url}`}
                    alt="Player Icon"
                    className="w-50 h-50 mb-2"
                />
                <p className="text-xl font-semibold text-black">{name}</p>
                <p className="text-lg text-gray-600">{position} {number ? `#${number}` : ''}</p>
                <div className="flex justify-center items-center">
                    <p className="text-lg text-gray-600">{team_full_name}</p>
                    <img
                        src={`/images/team-logos/${team_abbreviation}.png`}
                        height="30px"
                        width="30px"
                    />
                </div>
            </div>
        </div>
    );
}

export default PlayerBio;