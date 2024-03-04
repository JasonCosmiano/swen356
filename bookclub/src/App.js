// src/App.js
import React from 'react';
import Header from './components/Header';
import NavigationBar from './components/NavigationBar';
import SearchBar from './components/SearchBar';
import BookCard from './components/BookCard';
import RecentActivity from './components/RecentActivity';
import ReactionButtons from './components/ReactionButtons';
import './App.css';

const App = () => (
  <div className="app">
    <Header />
    <NavigationBar />
    <div className="content">
      <BookCard />
      <RecentActivity />
    </div>
  </div>
);

export default App;
