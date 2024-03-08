// src/components/Header.js
import React from 'react';
import SearchBar from './SearchBar';
import '../Header.css';

const Header = () => (
  <header className="header">
    <div className="logo-placeholder"></div>
    <h1>BookClub</h1>
    <SearchBar />
  </header>
);

export default Header;
