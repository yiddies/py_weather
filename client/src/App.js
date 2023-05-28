import React, { useState, useEffect } from 'react';

function App() {
  useEffect(() => {
    fetch('/test')
      .then(response => response.json())
      .then(data => {
        console.log(data);
      });
  }, []);

  return (
    <div></div>
  );
}

export default App;
