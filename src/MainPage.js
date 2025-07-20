import React from "react";
import Card from './Card';

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
            </div>
        </>
    )
}
export default MainPage;