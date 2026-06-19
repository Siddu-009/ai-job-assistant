import { useEffect, useState } from "react";

export default function Sidebar({
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
        width: "250px",

        minHeight: "100vh",

        background:
          darkMode
            ? "#020617"
            : "#1e293b",

        color: "#ffffff",

        padding: "25px"
      }}
    >

      <h1>
        AI Job Assistant
      </h1>

      <hr />

      <div
        style={{
          marginTop: "25px"
        }}
      >

        <p>🏠 Dashboard</p>

        <p>📊 ATS Score</p>

        <p>💼 Jobs</p>

        <p>⭐ Saved Jobs</p>

        <p>📄 Applications</p>

      </div>

      <button
        onClick={onLogout}
        style={{
          width: "100%",

          marginTop: "40px",

          padding: "12px",

          border: "none",

          borderRadius: "8px",

          cursor: "pointer",

          background: "#ffffff"
        }}
      >
        Logout
      </button>

    </div>

  );

}
