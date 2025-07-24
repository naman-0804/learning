import React from "react";
import { useNavigate } from "react-router-dom";
//import "./index.css";
//import road from "./images\\Screenshot 2025-07-18 222653.png";
function About() {
    const navigate=useNavigate();

    const go = () => {
        navigate("/clock");
    };
    return (  
        <>
        
            <h1>About</h1>
            <button className="btn" onClick={go}>Go to clock</button>
        </>
    );
}

export default About; 