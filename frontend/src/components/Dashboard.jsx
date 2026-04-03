import React, { useState, useEffect } from 'react';

export const Dashboard = () => {
  const [studentData, setStudentData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      const response = await fetch('/api/v1/analytics/dashboard');
      if (!response.ok) throw new Error('Failed to fetch dashboard data');
      const data = await response.json();
      setStudentData(data);
      setLoading(false);
    } catch (err) {
      setError(err.message);
      setLoading(false);
    }
  };

  if (loading) return <div className="loading">Loading dashboard...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="dashboard-container">
      <h1>Student Dashboard</h1>
      <div className="metrics-grid">
        <div className="metric-card">
          <h3>Overall Performance</h3>
          <p className="score">82%</p>
          <p className="label">Average Score</p>
        </div>
        <div className="metric-card">
          <h3>Learning Progress</h3>
          <div className="progress-bar">
            <div className="progress" style={{width: '65%'}}></div>
          </div>
          <p className="label">65% Complete</p>
        </div>
        <div className="metric-card">
          <h3>Study Time</h3>
          <p className="score">45.5h</p>
          <p className="label">Total Hours</p>
        </div>
        <div className="metric-card">
          <h3>Engagement</h3>
          <p className="score">High</p>
          <p className="label">Active Learner</p>
        </div>
      </div>
    </div>
  );
};
