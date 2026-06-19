import { useState, useEffect } from "react";

import Layout from "../components/Layout";
import DashboardCards from "../components/DashboardCards";
import ATSScore from "../components/ATSScore";
import RecommendedJobs from "../components/RecommendedJobs";
import SavedJobs from "../components/SavedJobs";
import Applications from "../components/Applications";
import RecentApplications from "../components/RecentApplications";
import ResumeCenter from "../components/ResumeCenter";
import Profile from "../components/Profile";

import { login, register } from "../services/api";

export default function Home() {

  const [mounted, setMounted] = useState(false);

  const [mode, setMode] = useState("login");

  const [name, setName] = useState("");

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const [message, setMessage] = useState("");

  const [token, setToken] = useState(null);

  useEffect(() => {

    setMounted(true);

    const savedToken =
      localStorage.getItem("token");

    if (savedToken) {

      setToken(savedToken);

    }

  }, []);

  const handleRegister = async () => {

    const result = await register(
      name,
      email,
      password
    );

    if (
      result.message ||
      result.id
    ) {

      setMessage(
        "Registration Successful. Please Login."
      );

      setMode("login");

    } else {

      setMessage(
        JSON.stringify(result)
      );

    }
  };

  const handleLogin = async () => {

    const result = await login(
      email,
      password
    );

    if (
      result.access_token
    ) {

      localStorage.setItem(
        "token",
        result.access_token
      );

      setToken(
        result.access_token
      );

      setMessage(
        "Login Successful"
      );

    } else {

      setMessage(
        JSON.stringify(result)
      );

    }
  };

  const handleLogout = () => {

    localStorage.removeItem(
      "token"
    );

    setToken(null);

    setName("");

    setEmail("");

    setPassword("");

    setMessage("");
  };

  if (!mounted) {

    return null;

  }

  if (token) {

    return (

      <Layout
        onLogout={
          handleLogout
        }
      >

        <DashboardCards />

	<RecentApplications />

	<ATSScore />

	<ResumeCenter />

	<Profile />

        <RecommendedJobs />

        <SavedJobs />

        <Applications />

      </Layout>

    );

  }

  return (

    <div
      style={{
        maxWidth: "500px",
        margin: "50px auto",
        padding: "20px",
        border: "1px solid #ddd",
        borderRadius: "10px",
        fontFamily: "Arial"
      }}
    >

      <h1>
        AI Job Assistant
      </h1>

      <div
        style={{
          marginBottom: "20px"
        }}
      >

        <button
          onClick={() =>
            setMode(
              "login"
            )
          }
          style={{
            marginRight: "10px"
          }}
        >
          Login
        </button>

        <button
          onClick={() =>
            setMode(
              "register"
            )
          }
        >
          Register
        </button>

      </div>

      {
        mode === "register" && (

          <>

            <input
              type="text"
              placeholder="Name"
              value={name}
              onChange={(e) =>
                setName(
                  e.target.value
                )
              }
              style={{
                width: "100%",
                padding: "10px"
              }}
            />

            <br />
            <br />

          </>

        )
      }

      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) =>
          setEmail(
            e.target.value
          )
        }
        style={{
          width: "100%",
          padding: "10px"
        }}
      />

      <br />
      <br />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) =>
          setPassword(
            e.target.value
          )
        }
        style={{
          width: "100%",
          padding: "10px"
        }}
      />

      <br />
      <br />

      {
        mode === "login"
          ? (
            <button
              onClick={
                handleLogin
              }
            >
              Login
            </button>
          )
          : (
            <button
              onClick={
                handleRegister
              }
            >
              Register
            </button>
          )
      }

      <br />
      <br />

      <p>
        {message}
      </p>

    </div>

  );

}
