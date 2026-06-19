import { useEffect, useState } from "react";
import ThemeToggle from "./ThemeToggle";

export default function Navbar() {

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
        background:
          darkMode
            ? "#1e293b"
            : "#2563eb",

        color: "white",

        padding: "20px",

        borderRadius: "12px",

        marginBottom: "20px",

        display: "flex",

        justifyContent:
          "space-between",

        alignItems: "center"
      }}
    >

      <h1
        style={{
          margin: 0
        }}
      >
        AI Job Assistant Dashboard
      </h1>

      <ThemeToggle />

    </div>

  );

}
