import React, { useState, useEffect } from 'react';
import { getPitData } from './api/api';



// const PIT = () => {
//   const [data, setData] = useState(null);

//   useEffect(() => {
//     const fetchData = async () => {
//       try {
//         const response = await getPitData();
//         setData(response);
//       } catch (error) {
//         // Handle the error, e.g., display an error message
//       }
//     };

//     fetchData();
//   }, []);

//     return (
//       <div>
//         <h1>Pittsburgh Steelers</h1>
//         {/* Your content goes here */
//         <div>
//           {data ? (
//             <div>
//               <h2>API Data:</h2>
//               <pre>{JSON.stringify(data, null, 2)}</pre>
//             </div>
//               ) : (
//                 <p>Loading...</p>
//               )}
//         </div>}
//       </div>


//     );
//   };
  
//   export default PIT;

  const PIT = () => {
    const [data, setData] = useState(null);
  
    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await getPitData();
          setData(response);
        } catch (error) {
          // Handle the error, e.g., display an error message
        }
      };
  
      fetchData();
    }, []);
  
    return (
      <div>
        <h1>Pittsburgh Steelers</h1>
        {data ? (
          <div>
            <h2>API Data:</h2>
            <pre>{JSON.stringify(data, null, 2)}</pre>
          </div>
        ) : (
          <p>Loading...</p>
        )}
      </div>
    );
  };
  
  export default PIT;