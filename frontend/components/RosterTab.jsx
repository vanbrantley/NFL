// components/RosterTab.js
import Player from './Player';

const RosterTab = ({ data }) => {
  return (
    <div>
      <h2 className="text-xl font-semibold text-black">Roster</h2>
      {data ? (
        <div>
          {data.map((player, i) => (
            <Player
              key={i}
              id={player.player_id}
              name={player.player_name}
              position={player.position}
              number={player.jersey_number}
              image_url={player.image_url}
            />
          ))}
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default RosterTab;
