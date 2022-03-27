import "./App.css";
import Create from "./views/Create";
import DisplayAll from "./components/DisplayAll";
import Update from "./views/Update";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import React from 'react'


function App() {

  return (
    <BrowserRouter>
      <h1>Favorite Authors</h1>
      <div className="App">
        <Routes>
          <Route path= "/" element={<DisplayAll />}/>
          <Route path="/new" element={<Create/>} />
          <Route path="/edit/:id" element={<Update />} />
        </Routes>
      </div>
  </BrowserRouter>
  );
}

export default App;
