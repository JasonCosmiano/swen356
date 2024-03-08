// BookPage.js
import React from 'react';
import '../BookPage.css'; // Adjust the path if necessary

function BookPage() {
  return (
    <div className="book-page">
      <h1>Book Title</h1>
      <p className="book-description">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ...
      </p>
      <div className="book-content">
        <div className="book-image">Book Picture</div>
        <div className="book-actions">
          <button className="action-btn">Write a review</button>
          <button className="action-btn">Add to wishlist</button>
          <button className="action-btn">E-Book/Link to Purchase</button>
        </div>
      </div>
      <div className="book-tags">
        Tags: <span>Tag1</span> <span>Tag2</span> <span>Tag3</span> <span>Tag4</span>
      </div>
    </div>
  );
}

export default BookPage;
