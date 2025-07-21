import React,{useState} from "react";
import "./index.css"
const Events=()=>{
    const[bg,setBg]=useState("red");
    const[txt,setTxt]=useState("click")
    const chgcol=()=>{
        setBg("Green")
        setTxt("Clicked!")
    }

    return (
        <>
        <div style={{backgroundColor:bg}}className="box">
            <button onClick={chgcol}>{txt}</button>
        </div>
        </>
    )
}

export default Events;