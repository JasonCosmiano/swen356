import React from 'react';

function BookCard() {
  return (
    <div className="book-card">
      <div className="book-picture">Book Picture</div>
      <div className="book-info">
        <h1>Book Title</h1>
        <p>Book Description...</p>
        <div className="book-tags">
          <span>Tag1</span>
          <span>Tag2</span>
          <span>Tag3</span>
        </div>
      </div>
    </div>
  );
}

export default BookCard;
