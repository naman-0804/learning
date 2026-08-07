import React from "react";
import images from "./images/Screenshot 2025-07-18 222653.png";

function Card(props) {
    return (
        <>
            <div className="card">
                <img src={images} alt=""/>
                <h3>{props.name}</h3>
            </div>
        </>
    )
}
export default Card;