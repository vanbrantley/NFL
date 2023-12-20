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
  const [sortBy, setSortBy] = useState("fantasy_points");
  const [isAscending, setIsAscending] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getFilteredLogs(position, startWeek, endWeek, sortBy, isAscending);
        // console.log(response);
        setData(response);
      } catch (error) {
        // Handle the error, e.g., display an error message
      }
    };

    fetchData();
  }, [position, startWeek, endWeek, sortBy, isAscending]);

  const positionOptions = [
    { value: 'QB', label: 'QB' },
    { value: 'RB', label: 'RB' },
    { value: 'WR', label: 'WR' },
    { value: 'TE', label: 'TE' },
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
    { value: 11, label: '11' },
    { value: 12, label: '12' },
    { value: 13, label: '13' },
    { value: 14, label: '14' },
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
    { value: 11, label: '11' },
    { value: 12, label: '12' },
    { value: 13, label: '13' },
    { value: 14, label: '14' },
  ];

  const handlePositionSelect = (e) => {
    const newPosition = e.value;
    if (newPosition !== position) {
      setPosition(newPosition);
      if (isAscending) setIsAscending(false);
      setSortBy("fantasy_points");
    }
  };

  const handleStartWeekSelect = (e) => {
    setStartWeek(e.value);
  };

  const handleEndWeekSelect = (e) => {
    setEndWeek(e.value);
  };

  const handleHeaderClick = (columnName) => {
    if (columnName !== 'rank' && columnName !== 'player') {
      if (sortBy === columnName) {
        // If the same column is clicked, toggle the sorting order
        setIsAscending(!isAscending);
      } else {
        // If a new column is clicked, set it as the sortBy column and default to ascending order
        setSortBy(columnName);
        setIsAscending(false);
      }
    }
  };

  const renderHeader = (columnName, displayName) => (
    <div
      className={`flex justify-center col-span-1 ${columnName !== 'rank' && columnName !== 'player' ? 'cursor-pointer' : ''} ${sortBy === columnName ? 'font-bold' : ''}`}
      onClick={() => handleHeaderClick(columnName)}
    >
      <p>{displayName}</p>
      {sortBy === columnName && (
        <span>{isAscending ? ' ↑' : ' ↓'}</span>
      )}
    </div>
  );

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
          {(position == "QB") && <PassingFilteredLogsTable data={data} renderHeader={renderHeader} />}
          {(position == "RB") && <RushingFilteredLogsTable data={data} renderHeader={renderHeader} />}
          {(position == "WR" || position == "TE") && <ReceivingFilteredLogsTable data={data} renderHeader={renderHeader} />}
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default FilteredLogsManipulator;