import "./App.css";
import ProductForm from "./components/ProductForm";
import Main from "./views/Main";
import DisplayOne from "./components/DisplayOne";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
          <Route path= "/" element={<ProductForm/>} />
          <Route path="/product" element={<Main/>} />
          <Route path="/product/:id" element={<DisplayOne/>} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
