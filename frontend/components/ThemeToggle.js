import { useEffect, useState } from "react";

export default function ThemeToggle() {

  const [theme, setTheme] =
    useState("light");

  useEffect(() => {

    const savedTheme =
      localStorage.getItem("theme");

    if (savedTheme) {

      setTheme(savedTheme);

      document.body.style.background =
        savedTheme === "dark"
          ? "#0f172a"
          : "#f8fafc";

      document.body.style.color =
        savedTheme === "dark"
          ? "white"
          : "black";
    }

  }, []);

  const toggleTheme = () => {

    const newTheme =
      theme === "light"
        ? "dark"
        : "light";

    setTheme(newTheme);

    localStorage.setItem(
      "theme",
      newTheme
    );

    document.body.style.background =
      newTheme === "dark"
        ? "#0f172a"
        : "#f8fafc";

    document.body.style.color =
      newTheme === "dark"
        ? "white"
        : "black";
  };

  return (

    <button
      onClick={toggleTheme}
      style={{
        padding: "10px",
        borderRadius: "8px",
        cursor: "pointer"
      }}
    >
      {
        theme === "light"
          ? "🌙 Dark Mode"
          : "☀️ Light Mode"
      }
    </button>

  );

}
