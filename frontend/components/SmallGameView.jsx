import Link from "next/link";

const SmallGameView = ({away_team, box_score_url, game_id, home_team, season, week})=> {

    return (
        
      <Link href={`/game/${game_id}`}>
        <div className="bg-gray-100 rounded-lg p-4 m-2 shadow-md hover:shadow-lg transition-transform transform hover:-translate-y-1">
          <div className="flex justify-between items-center mb-4">
            <div className="flex items-center">
              <img src={`/images/team-logos/${away_team}.png`} alt={`${away_team} Logo`} className="w-8 h-8 mr-2" />
              <p className="text-lg font-semibold">{away_team} vs {home_team}</p>
              <img src={`/images/team-logos/${home_team}.png`} alt={`${home_team} Logo`} className="w-8 h-8 ml-2" />
            </div>
            <div>
              <p className="text-lg font-semibold">Week {week}</p>
            </div>
          </div>
        </div>  
      </Link>
          
          

    );


} 

export default SmallGameView;