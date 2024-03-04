// SuggestionCard.js
import React from 'react';
import '../SuggestionCard.css';

function SuggestionCard({ name, onAdd }) {
  return (
    <div className="suggestion-card">
      <div className="suggestion-profile-picture">PFP</div>
      <div className="suggestion-info">
        <h3>{name}</h3>
        <button onClick={onAdd}>+</button>
      </div>
    </div>
  );
}

export default SuggestionCard;
