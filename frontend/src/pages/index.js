
import { Inter } from 'next/font/google'
import Navbar from '../../components/Navbar'
import FilteredLogsManipulator from '../../components/FilteredLogsManipulator';

const inter = Inter({ subsets: ['latin'] })

const Home = () => {
  return (
    <div>
      <h1>Fantasy Finesser</h1>
      <FilteredLogsManipulator />

    </div>
  );
};

export default Home;


