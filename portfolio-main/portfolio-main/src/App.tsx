import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import HomePage from "./pages/home-page";
import AboutPage from "./pages/about-page";
import "./App.css";
import Layout from "./components/layout";
import RegisterPage from "./pages/register-page";

// Components are capitalized
function App() {
  /* ----------------- Logic ----------------- */

  // Where you define your pages
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path="/" element={<Layout />}>
        {/* Child pages will be displayed here */}
        <Route index element={<HomePage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/register" element={<RegisterPage />} />
      </Route>,
    ),
  );

  /* ----------------- HTML ----------------- */
  return <RouterProvider router={router} />;
}

export default App;
