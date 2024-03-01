// FriendCard.js
import React from 'react';
import './FriendCard.css'; 

function FriendCard({ friend }) {
  return (
    <div className="friend-card">
      <img src={friend.profilePicture} alt={`${friend.username}'s profile`} />
      <div className="friend-info">
        <h3>{friend.username}</h3>
        <p>Last message {friend.lastMessageTime} ago</p>
      </div>
    </div>
  );
}

export default FriendCard;
