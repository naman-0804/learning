import './App.css';
import React,{useState} from 'react';
import ChildA from './ChildA';
const App=()=> { 

const name="Naman"
  return (
    <>
      <h1>Props drilling</h1>
      <ChildA name={name}/>
    </>
  );
}

export default App;
