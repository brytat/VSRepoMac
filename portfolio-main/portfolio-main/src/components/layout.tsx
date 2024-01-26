import React from "react";
import { Outlet } from "react-router-dom";
import { ThemeContext } from "../contexts/theme-provider";
import Footer from "./footer";
import Navbar from "./navbar";

function Layout() {
  const { theme } = React.useContext(ThemeContext);

  console.log("Theme: ", theme);

  return (
    <div
      className={`flex flex-col min-h-screen ${
        theme === "dark" && "bg-[#202023] text-white"
      }`}
    >
      {/* Navbar */}
      <Navbar />

      {/* Content */}
      <main className="flex-grow">
        {/* Displaying the content of the child page */}
        <Outlet />
      </main>

      {/* Footer */}
      <Footer />
    </div>
  );
}

export default Layout;
