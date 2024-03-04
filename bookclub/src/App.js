import React, { useState } from 'react';
import Header from './components/Header';
import NavigationBar from './components/NavigationBar';
import BookCard from './components/BookCard';
import RecentActivity from './components/RecentActivity';
import FriendsPage from './components/FriendsPage';
import './App.css';
import BookPage from './components/BookPage';

const App = () => {
  const [currentPage, setCurrentPage] = useState('home');

  const renderPage = () => {
    switch (currentPage) {
      case 'home':
        return (
          <div className="content">
            <BookCard />
            <RecentActivity />
          </div>
        );
      case 'friends':
        return <FriendsPage />;
      case 'books':
        return <BookPage />;
      default:
        return (
          <div className="content">
            <BookCard />
            <RecentActivity />
          </div>
        );
    }
  };

  return (
    <div className="app">
      <Header />
      <NavigationBar setCurrentPage={setCurrentPage} />
      {renderPage()}
    </div>
  );
};

export default App;
