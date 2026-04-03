import React, { useState, useEffect } from 'react';

export const LearningPath = ({ studentId }) => {
  const [path, setPath] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchLearningPath(studentId);
  }, [studentId]);

  const fetchLearningPath = async (id) => {
    try {
      const response = await fetch(`/api/v1/learning-paths/${id}`);
      const data = await response.json();
      setPath(data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching learning path:', error);
      setLoading(false);
    }
  };

  if (loading) return <div>Loading learning path...</div>;

  return (
    <div className="learning-path-container">
      <h2>Your Learning Path</h2>
      {path && (
        <div>
          <div className="progress-info">
            <p>Current Topic: {path.current_topic}</p>
            <div className="progress-bar">
              <div className="progress" style={{width: path.progress + '%'}}></div>
            </div>
            <p>{path.progress}% Complete</p>
          </div>
          <div className="topics-list">
            <h3>Topics</h3>
            <ul>
              {path.path.map((topic, index) => (
                <li key={index} className={topic === path.current_topic ? 'active' : ''}>
                  {topic}
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
};
