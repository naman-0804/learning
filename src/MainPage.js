import React from "react";
import Card from './Card';
import { NavLink } from "react-router-dom";
function MainPage() {
    return (
        <>
            <h1 className="heading">Card Gallery</h1>
            <div className="card-comp">
            <Card name="Nature 1st "/>
            <Card name="Nature 2nd "/>
            <Card name="Nature 3rd "/>
            <Card name="Nature 4th "/>
            <Card name="Nature 5th "/>
            <Card name="Nature 6th "/>
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
            </div>
            
        </>
    )
}
export default MainPage;