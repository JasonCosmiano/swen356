// NavigationBar.js
import React from 'react';
import '../NavigationBar.css';

const NavigationBar = ({ setCurrentPage }) => (
  <nav className="navigation">
    <div onClick={() => setCurrentPage('home')}>Home</div>
    <div onClick={() => setCurrentPage('friends')}>Friends</div>
    <div onClick={() => setCurrentPage('review')}>Review</div>
    <div onClick={() => setCurrentPage('books')}>Books</div>
    <div onClick={() => setCurrentPage('profile')}>Profile</div>
  </nav>
);

export default NavigationBar;
