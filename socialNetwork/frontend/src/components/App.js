import React from 'react';
import { render } from "react-dom";

const App = () => {
  return (
    <div>
      <h1>App</h1>
    </div>
  );
}

export default App;

const container = document.getElementById("app");
render(<App />, container);