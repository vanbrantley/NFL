const ReceivingFilteredLogsResults = ({data}) => {
    return(
        <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md transition-transform transform">
            <div className="flex flex-col items-center">
                 <img
                    src={`${image_url}`}
                    alt="Player Icon"
                    className="w-50 h-50 mb-2"
                />
                <p className="text-lg text-gray-600">Team: {team}</p>
            </div>
        </div>
    );
}

export default ReceivingFilteredLogsResults;