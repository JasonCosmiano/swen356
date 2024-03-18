// FriendCard.js
import React from 'react';
import '../FriendCard.css';

function FriendCard({ name, lastMessage }) {
  return (
    <div className="friend-card">
      <div className="friend-profile-picture">PFP</div>
      <div className="friend-info">
        <h3>{name}</h3>
        <p>Last message {lastMessage} days ago</p>
      </div>
    </div>
  );
}

export default FriendCard;
