import './App.css';
import React,{useState} from 'react';

function App() { 
  const[count,setCount]=useState(0);
  const incre=()=>{
    setCount(count+1)
  }

  return (
    <>
      <div className='box'>
        <h1> {count}</h1>
        <button onClick={incre}>Increment</button>
      </div>
    </>
  );
}

export default App;
