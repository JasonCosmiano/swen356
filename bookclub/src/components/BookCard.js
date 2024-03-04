// src/components/BookCard.js
import React from 'react';
import '../BookCard.css';
import ReactionButtons from './ReactionButtons'; 

const BookCard = () => (
  <div className="book-card">
    <div className="book-info">
      <h2>Book Title</h2>
      <p>
Book Description:
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
<br></br><br></br><br></br>
ReviewerName's Review:
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum...

</p>
      <div className="book-tags">
      Tags: <span>Tag1</span> <span>Tag2</span> <span>Tag3</span> <span>Tag4</span>
      </div>
    </div>
    <div className="book-picture-container">
      <div className="book-picture">Book Picture</div>
      <ReactionButtons />
    </div>
  </div>
);

export default BookCard;
