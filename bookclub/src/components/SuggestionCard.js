// SuggestionCard.js
import React from 'react';
import './SuggestionCard.css'; // Your CSS file for styling

function SuggestionCard({ suggestion }) {
  const handleAddFriend = () => {
  };

  return (
    <div className="suggestion-card">
      <img src={suggestion.profilePicture} alt={`${suggestion.username}'s profile`} />
      <div className="suggestion-info">
        <h3>{suggestion.username}</h3>
        <button onClick={handleAddFriend}>+</button>
      </div>
    </div>
  );
}

export default SuggestionCard;
