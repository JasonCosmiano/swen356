// FriendsPage.js
import React from 'react';
import FriendCard from './FriendCard';
import SuggestionCard from './SuggestionCard';
import './FriendsPage.css'; // Your CSS file for styling

function FriendsPage() {
  
  const friendsList = [
    
  ];
  
  const suggestedFriends = [
    
  ];

  return (
    <div className="friends-page">
      <div className="friend-list">
        {friendsList.map(friend => (
          <FriendCard key={friend.id} friend={friend} />
        ))}
      </div>
      <div className="suggested-friends">
        <h2>Suggested for you</h2>
        {suggestedFriends.map(suggestion => (
          <SuggestionCard key={suggestion.id} suggestion={suggestion} />
        ))}
      </div>
    </div>
  );
}

export default FriendsPage;
