import React from "react";
import { NavLink } from "react-router-dom";
const Home = () => {
    return (
        <React.Fragment>
            <h1>Welcome to the Home Page!</h1>
            <p>This is a simple React component.</p>
            <nav>
                <ul>
                    <li><NavLink to="/">Home</NavLink></li>
                    <li><NavLink to="/mainpage">Main Page</NavLink></li>
                    <li><NavLink to="/condition">Condition</NavLink></li>
                    <li><NavLink to="/clock">Clock</NavLink></li>
                    <li><NavLink to="/events">Events</NavLink></li>
                    <li><NavLink to="/form">Form</NavLink></li>
                    <li><NavLink to="/incdec">Increment/Decrement</NavLink></li>
                </ul>
            </nav>
        </React.Fragment>
    )
} 

export default Home;     