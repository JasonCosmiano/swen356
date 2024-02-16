import React from 'react';
import Header from './components/Header';
import SearchBar from './components/SearchBar';
import BookCard from './components/BookCard';
import ReviewSection from './components/ReviewSection';
import ActivityFeed from './components/ActivityFeed';
import './App.css'; 

function App() {
  return (
    <div className="App">
      <div style={{ display: 'flex' }}>
      <div className="logo">BCLogo</div>
      <div className="maintitle">Book Club</div>
      <SearchBar />
    </div>
      <Header />
      <div className="main-content">
        <BookCard />
        <ReviewSection />
        <ActivityFeed />
      </div>
    </div>
  );
}

export default App;
