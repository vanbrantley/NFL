import '@/styles/globals.css'
import Navbar from '../../components/Navbar';
import Head from 'next/head';


function MyApp({ Component, pageProps }) {
  return (
    <>
      <Head>
        <title>NFL Finesser</title>
      </Head>
      <Navbar />
      <Component {...pageProps} />
    </>
  );
}

export default MyApp;

