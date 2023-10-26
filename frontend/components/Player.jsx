import Link from 'next/link';
const Player = ({id, name, position, number}) => {

    return(
        // <div>
        //     <Link href={`/player/${id}`} className="text-black hover:text-rose-700">
        //         <p>{name}, {position}, {number}</p>
        //         <p>{id}</p>
        //     </Link>
        // </div>
        // <div class="flex flex-col items-left">
        //     <Link href={`/player/${id}`} className="text-black hover:text-rose-700 p-4 border border-gray-300 rounded-lg shadow-md transition-transform transform hover:-translate-y-1 hover:scale-105">
        //         <div>
        //             <p class="text-lg font-semibold">{name}</p>
        //             <p class="text-gray-600">{position}</p>
        //             <p class="text-gray-600">Number: {number}</p>
        //         </div>
        //     </Link>
        // </div>
        <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md hover:shadow-lg transition-transform transform hover:-translate-y-1">
            <div className="flex flex-col items-right">
                {/* <img
                    src="/" // Replace with your jersey icon image URL
                    alt="Player Icon"
                    className="w-16 h-16 mb-2"
                /> */}
                <Link href={`/player/${id}`}>
                    <p className="text-xl font-semibold text-black hover:text-rose-700">{name}</p>
                    <p className="text-lg text-gray-600">{position}</p>
                    <p className="text-lg text-gray-600">Jersey #: {number}</p>
                </Link>
            </div>
        </div>

    );

}

export default Player;