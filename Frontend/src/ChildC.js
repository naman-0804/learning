import React,{useContext} from "react";
import {fName} from './App';


function ChildC() {
  const name = useContext(fName);

  return (
    <div>
      <h1>{name}</h1>
    </div>
  );
}

export default ChildC;
