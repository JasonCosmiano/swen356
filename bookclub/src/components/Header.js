import React from 'react';

function Header() {
  return (
    <div className="header">
      <nav className="navigation">
        <a href="/home">Home</a>
        <a href="/friends">Friends</a>
        <a href="/reviews">Reviews</a>
        <a href="/books">Books</a>
        <a href="/profile">Profile</a>
      </nav>
    </div>
  );
}

export default Header;
