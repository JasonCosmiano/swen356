// src/components/NavigationBar.js
import React from 'react';
import '../NavigationBar.css';

const NavigationBar = () => (
  <nav className="navigation">
    <a href="/home">Home</a>
    <a href="/friends">Friends</a>
    <a href="/reviews">Reviews</a>
    <a href="/books">Books</a>
    <a href="/profile">Profile</a>
  </nav>
);

export default NavigationBar;
