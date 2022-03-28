import "./App.css";
import Create from "./views/Create";
import DisplayAll from "./components/DisplayAll";
import DisplayOne from "./components/DisplayOne";
import Update from "./views/Update";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import React from 'react'


function App() {

  return (
    <BrowserRouter>
      <header><h1 className="text-center">Pet Shelter</h1></header>
      <div className="App">
        <Routes>
          <Route path= "/" element={<DisplayAll />}/>
          <Route path= "/pets/:id" element={<DisplayOne />}/>
          <Route path="/pets/new" element={<Create />} />
          <Route path="/pets/edit/:id" element={<Update />} />
        </Routes>
      </div>
  </BrowserRouter>
  );
}

export default App;