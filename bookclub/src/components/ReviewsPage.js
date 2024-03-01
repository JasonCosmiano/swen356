import React, { useState } from 'react';
import SearchBar from './SearchBar'; // Reuse your existing SearchBar component
import BookInfo from './BookInfo'; // Component to display book info
import ReviewForm from './ReviewForm'; // Component for users to write a review

function ReviewsPage() {
  const [selectedBook, setSelectedBook] = useState(null);

  const handleBookSearch = (bookData) => {
    
    const mockBookData = {
      title: "Example Book Title",
      author: "Author Name",
      imageUrl: "path/to/book/image.jpg"
    };
    setSelectedBook(mockBookData);
  };

  return (
    <div className="reviews-page">
      <SearchBar onSearch={handleBookSearch} />
      {selectedBook && (
        <>
          <BookInfo book={selectedBook} />
          <ReviewForm book={selectedBook} />
        </>
      )}
    </div>
  );
}

export default ReviewsPage;
