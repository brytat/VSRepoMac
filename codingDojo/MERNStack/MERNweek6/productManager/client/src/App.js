import "./App.css";
import ProductForm from "./components/ProductForm";
import Main from "./view/Main";
import DisplayOne from "./components/DisplayOne";
import Update from "./view/Update";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
          <Route path= "/" element={<ProductForm/>} />
          <Route path="/product" element={<Main/>} />
          <Route path="/product/:id" element={<DisplayOne/>} />
          <Route path="/product/edit/:id" element={<Update/>} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
