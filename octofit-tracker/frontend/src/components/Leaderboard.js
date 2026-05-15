import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = `https://${codespace}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Leaderboard API:', endpoint);
        console.log('Leaderboard data:', data);
        setLeaderboard(data.results || data);
      });
  }, [endpoint]);

  return (
    <div className="container">
      <h2 className="mt-4 mb-4 display-6">Leaderboard</h2>
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th>Team</th>
            <th>Points</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.map((item, idx) => (
            <tr key={idx}>
              <td>{item.team}</td>
              <td>{item.points}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button className="btn btn-primary mt-3" onClick={()=>window.location.reload()}>Reload</button>
    </div>
  );
};

export default Leaderboard;
