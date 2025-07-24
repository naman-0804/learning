import React from "react";
import { Link } from "react-router-dom";
const Home = () => {
    return (
        <React.Fragment>
            <h1>Welcome to the Home Page!</h1>
            <p>This is a simple React component.</p>
            <nav>
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/mainpage">Main Page</Link></li>
                    <li><Link to="/condition">Condition</Link></li>
                    <li><Link to="/clock">Clock</Link></li>
                    <li><Link to="/events">Events</Link></li>
                    <li><Link to="/form">Form</Link></li>
                    <li><Link to="/incdec">Increment/Decrement</Link></li>
                </ul>
            </nav>
        </React.Fragment>
    )
} 

export default Home;     