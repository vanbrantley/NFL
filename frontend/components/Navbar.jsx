import Link from 'next/link';

const Navbar = () => {

  const team_abbreviations = [
    "ARI",
    "ATL",
    "BAL",
    "BUF",
    "CAR",
    "CHI",
    "CIN",
    "CLE",
    "DAL",
    "DEN",
    "DET",
    "GB",
    "HOU",
    "IND",
    "JAC",
    "KC",
    "LV",
    "LAC",
    "LAR",
    "MIA",
    "MIN",
    "NE",
    "NO",
    "NYG",
    "NYJ",
    "PHI",
    "PIT",
    "SF",
    "SEA",
    "TB",
    "TEN",
    "WAS",
  ]

  return (
    <nav className="bg-blue-900 py-4 shadow-lg">
      <div className="container mx-auto">
        <ul className="flex justify-center space-x-2">
          <li>
            <Link href="/" className="text-white hover:text-rose-700">Home</Link>
          </li>

          {team_abbreviations.map((abbreviation, i) => {
            return(
              <li>
                <Link href={`/team/${abbreviation}`}>
                    <img
                      src={`/images/${abbreviation}-logo.png`}
                      className="w-10 h-9 cursor-pointer transform transition-transform hover:scale-125" // Set the width and height here
                    />
                </Link>
              </li>
            );
            
          })}

          <li>
            <Link href="/FantasyTeam" className="text-white hover:text-rose-700">Fantasy Team</Link>
          </li>

        </ul>
      </div>
    </nav>
    
  );
};

export default Navbar;