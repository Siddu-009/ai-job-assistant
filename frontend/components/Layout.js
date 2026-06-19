import { useEffect, useState } from "react";
import Sidebar from "./Sidebar";
import Navbar from "./Navbar";

export default function Layout({
  children,
  onLogout
}) {

  const [darkMode, setDarkMode] =
    useState(false);

  useEffect(() => {

    const theme =
      localStorage.getItem("theme");

    setDarkMode(
      theme === "dark"
    );

  }, []);

  return (

    <div
      style={{
        display: "flex",
        minHeight: "100vh",
        background:
          darkMode
            ? "#0f172a"
            : "#f8fafc"
      }}
    >

      <Sidebar
        onLogout={onLogout}
      />

      <div
        style={{
          flex: 1,
          padding: "20px",
          background:
            darkMode
              ? "#0f172a"
              : "#f8fafc",
          color:
            darkMode
              ? "#ffffff"
              : "#111827"
        }}
      >

        <Navbar />

        {children}

      </div>

    </div>

  );

}
