import React from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";
//import "./index.css";
//import road from "./images\\Screenshot 2025-07-18 222653.png";
function About() {
    const navigate=useNavigate();
    const {fname} = useParams();
    const location=useLocation();
    const go = () => {
        navigate("/clock");
    };
    return (  
        <>
        
            <h1>About</h1>
            <button className="btn" onClick={go}>Go to clock</button>
            <h1>Hello {fname}</h1>
            <p>Current location: {location.pathname}</p>
        </>
    );
}

export default About; 