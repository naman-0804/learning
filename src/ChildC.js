import React from "react";
import {fName} from './App';
function ChildC() {
  return (
    <div>
      <fName.Consumer>
        {
          (fName) =>{
            return (
              <h1>My name is {fName}</h1>
            );
          }
        }
      </fName.Consumer>
    </div>
  );
}

export default ChildC;
