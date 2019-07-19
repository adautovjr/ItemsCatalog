import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  fetch('http://localhost:5000/category/10/')
  .then(results => {
    if (results.code == 200) {
      console.log("alou")
    }
  })

  return (
    <div className="App">
      <header className="App-header">
        Alou mundo
      </header>
    </div>
  );
}

export default App;
