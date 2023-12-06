import Link from 'next/link';
const Player = ({id, name, position, number, image_url}) => {

    console.log(image_url);

    return(
        <Link href={`/player/${id}`}>
            <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md hover:shadow-lg transition-transform transform hover:-translate-y-1">
                
                <div className="flex items-center">
                    {image_url ? (
                        <img
                        src={`${image_url}`} // Replace with your image URL
                        alt="Player Icon"
                        className="w-16 h-16 mb-2"
                    />
                    ) : (
                    
                    <div className="w-16 h-16 mb-2"></div>
                    )}
                    <div className="ml-4 flex flex-col">
                        
                            <p className="text-xl font-semibold text-black hover:text-rose-700">{name}</p>
                            <p className="text-lg text-gray-600">{position}</p>
                            {number && <p className="text-lg text-gray-600"># {number}</p>}
                        
                    </div>
                </div>
            </div>
        </Link>

    );

}

export default Player;