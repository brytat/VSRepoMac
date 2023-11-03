import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import HomePage from "./pages/home-page";
import AboutPage from "./pages/about-page";
import ProjectsPage from "./pages/projects-page";
import "./App.css";
import Layout from "./components/layout";

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
        <Route path="/projects" element={<ProjectsPage/>}/>
      </Route>,
    ),
  );

  /* ----------------- HTML ----------------- */
  return <RouterProvider router={router} />;
}

export default App;