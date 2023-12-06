import { getFilteredLogs } from "@/pages/api/api";
import { useState, useEffect } from "react";
import PassingFilteredLogsTable from "./PassingFilteredLogsTable";
import RushingFilteredLogsTable from "./RushingFilteredLogsTable";
import ReceivingFilteredLogsTable from "./ReceivingFilteredLogsTable";
import Select from 'react-select';

const FilteredLogsManipulator = () => {

  const [data, setData] = useState(null);
  const [position, setPosition] = useState("QB");
  const [startWeek, setStartWeek] = useState(1);
  const [endWeek, setEndWeek] = useState(2);

  // use react-select: https://react-select.com/home
  // position select
  // startWeek select
  // endWeek select 

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getFilteredLogs(position, startWeek, endWeek);
        console.log(response);
        setData(response);
      } catch (error) {
        // Handle the error, e.g., display an error message
      }
    };

    fetchData();
  }, [position, startWeek, endWeek]);

  const positionOptions = [
    { value: 'QB', label: 'QB' },
    { value: 'WR', label: 'WR' },
    { value: 'RB', label: 'RB' }
  ];

  const startWeekOptions = [
    { value: 1, label: '1' },
    { value: 2, label: '2' },
    { value: 3, label: '3' },
    { value: 4, label: '4' },
    { value: 5, label: '5' },
    { value: 6, label: '6' },
    { value: 7, label: '7' },
    { value: 8, label: '8' },
    { value: 9, label: '9' },
    { value: 10, label: '10' },
  ];

  const endWeekOptions = [
    { value: 1, label: '1' },
    { value: 2, label: '2' },
    { value: 3, label: '3' },
    { value: 4, label: '4' },
    { value: 5, label: '5' },
    { value: 6, label: '6' },
    { value: 7, label: '7' },
    { value: 8, label: '8' },
    { value: 9, label: '9' },
    { value: 10, label: '10' },
  ];

  const handlePositionSelect = (e) => {
    setPosition(e.value);
  };

  const handleStartWeekSelect = (e) => {
    setStartWeek(e.value);
  };

  const handleEndWeekSelect = (e) => {
    setEndWeek(e.value);
  };

  return (
    <div>

      <div className="flex p-8">
        <div className="flex flex-grow items-center justify-center space-x-4">
          <p>Position: </p>
          <Select options={positionOptions} value={positionOptions.find(option => option.value === position)} onChange={handlePositionSelect} />
        </div>
        <div className="flex flex-grow items-center justify-center space-x-4">
          <p>Start Week: </p>
          <Select options={startWeekOptions} value={startWeekOptions.find(option => option.value === startWeek)} onChange={handleStartWeekSelect} />
        </div>
        <div className="flex flex-grow items-center justify-center space-x-4">
          <p>End Week: </p>
          <Select options={endWeekOptions} value={endWeekOptions.find(option => option.value === endWeek)} onChange={handleEndWeekSelect} />
        </div>
      </div>

      {data ? (
        <div>
          {(position == "QB") && <PassingFilteredLogsTable data={data} />}
          {(position == "RB") && <RushingFilteredLogsTable data={data} />}
          {(position == "WR") && <ReceivingFilteredLogsTable data={data} />}
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default FilteredLogsManipulator;