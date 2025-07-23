import './App.css';
import React,{createContext, useState} from 'react';
import ChildC from './ChildC';
const fName=createContext();
const App=()=> { 
  return (
    <>
    <fName.Provider value={"Naman srivastava"}>
      <ChildC/>
    </fName.Provider>
    </>
  );
}

export default App;
export {fName};