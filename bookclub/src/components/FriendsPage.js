// FriendsPage.js
import React from 'react';
import FriendCard from './FriendCard';
import SuggestionCard from './SuggestionCard';
import '../FriendsPage.css';

function FriendsPage() {
  const friendsList = [
    { name: "Alice", lastMessage: "2" },
    { name: "Bob", lastMessage: "5" },
  ];

  const suggestedFriends = [
    { name: "Charlie" },
    { name: "Dave" },
  ];

  return (
    <div className="friends-page">
      <div className="friends-list">
        {friendsList.map((friend, index) => (
          <FriendCard key={index} name={friend.name} lastMessage={friend.lastMessage} />
        ))}
      </div>
      <div className="suggested-friends">
        <h2>Suggested for you</h2>
        {suggestedFriends.map((suggestion, index) => (
          <SuggestionCard key={index} name={suggestion.name} onAdd={() => console.log("Add friend")} />
        ))}
      </div>
    </div>
  );
}

export default FriendsPage;
