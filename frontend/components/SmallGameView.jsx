import Link from "next/link";

const SmallGameView = ({away_team, box_score_url, game_id, home_team, season, week})=> {

    return (
        // <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md hover:shadow-lg transition-transform transform hover:-translate-y-1">
        //             <div className="flex items-center">
        //                 {/* <img
        //                     src={`${image_url}`} // Replace with your image URL
        //                     alt="Home Team icon"
        //                     className="w-16 h-16 mb-2"
        //                 /> */}
        //                 <div className="ml-4 flex flex-col">
        //                     <Link href={`/`}>
        //                         <p className="text-xl font-semibold text-black hover:text-rose-700">{game_id}</p>
        //                         <p className="text-lg text-gray-600">{season}</p>
        //                         <p className="text-lg text-gray-600"># {week}</p>
        //                     </Link>
        //                 </div>

        //                 <div className="ml-4 flex flex-col">
        //                     <Link href={`/`}>
        //                         <p className="text-xl font-semibold text-black hover:text-rose-700">{away_team}</p>
        //                     </Link>
        //                 </div>

        //                 <div className="ml-4 flex flex-col">
        //                     <Link href={`/`}>
        //                         <p className="text-xl font-semibold text-black hover:text-rose-700">VS</p>
        //                     </Link>
        //                 </div>

        //                 <div className="ml-4 flex flex-col">
        //                     <Link href={`/`}>
        //                         <p className="text-xl font-semibold text-black hover:text-rose-700">{home_team}</p>
        //                     </Link>
        //                 </div>

        //                 <div className="ml-4 flex flex-col">
        //                     <Link href={box_score_url}>
        //                         <p className="text-xl font-semibold text-black hover:text-rose-700">Box Score:</p>
        //                     </Link>
        //                 </div> 
        //             </div>
        //         </div>

        // <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md hover:shadow-lg transition-transform transform hover:-translate-y-1">
        //     <div>
        //         <p>ID: {game_id}</p>
        //         <p>Season: {season}</p>
        //         <p>Week: {week}</p>
        //     </div>
        //     <p>Away Team: {away_team}</p>
        //     <p>Box Score URL: {box_score_url}</p>
        //     <p>ID: {game_id}</p>
        //     <p>Home Team: {home_team}</p>
            
        // </div>

        
        <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md hover:shadow-lg transition-transform transform hover:-translate-y-1">
              <div className="flex justify-between items-center mb-4">
                <div className="flex items-center">
                  <img src={`/png-images/${away_team}.png`} alt={`${away_team} Logo`} className="w-8 h-8 mr-2" />
                  <p className="text-lg font-semibold">{away_team} vs {home_team}</p>
                  <img src={`/png-images/${home_team}.png`} alt={`${home_team} Logo`} className="w-8 h-8 ml-2" />
                </div>
                <div>
                  <p className="text-lg font-semibold">Week {week}</p>
                  <p className="text-sm text-gray-500">Season: {season}</p>
                </div>
                
              </div>
              <div className="mb-4">
                <p className="text-sm text-gray-500">Box Score URL: <a href={box_score_url} target="_blank" rel="noopener noreferrer" className="text-blue-500">{box_score_url}</a></p>
                
              </div>
              <div className="flex justify-between items-center">
                <p className="text-sm text-gray-500">Away: {away_team}, Home: {home_team}</p>
                <p className="text-sm text-gray-500">Game ID: {game_id}</p>
              </div>
            </div>    
          

    );


} 

export default SmallGameView;