const PlayerBio = ({ id, name, position, number, college, experience, height, image_url, weight, team }) => {
    return (
        <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md transition-transform transform">
            <div className="flex flex-col items-center">
                <img
                    src={`${image_url}`}
                    alt="Player Icon"
                    className="w-50 h-50 mb-2"
                />
                <p className="text-xl font-semibold text-black">{name}</p>
                <p className="text-lg text-gray-600">#{number}</p>
                <p className="text-lg text-gray-600">{position}</p>
                <p className="text-lg text-gray-600">{team}</p>
                {/* <p className="text-lg text-gray-600">College: {college}</p>
                <p className="text-lg text-gray-600">Experience: {experience}</p>
                <p className="text-lg text-gray-600">Height: {height} in</p>
                <p className="text-lg text-gray-600">Weight: {weight} lbs</p> */}
            </div>
        </div>
    );
}

export default PlayerBio;