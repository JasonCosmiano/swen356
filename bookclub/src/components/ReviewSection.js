import React from 'react';

function ReviewSection() {
  return (
    <div className="review-section">
      <h2>ReviewerName's Review</h2>
      <p>Review text...</p>
      <div className="review-reactions">
        <button>👍</button>
        <button>👎</button>
        <button>😭</button>
      </div>
    </div>
  );
}

export default ReviewSection;
