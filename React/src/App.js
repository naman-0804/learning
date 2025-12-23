  import react, { useEffect, useState } from 'react'
  function App(){
    const [cnt,setCnt]=useState(0);

    const count=()=>{
      setCnt(cnt+1);
    } 
    const handlechng=(e)=>{
      setCnt(Number(e.target.value))
    }
    useEffect(() => {
      fetch(`https://jsonplaceholder.typicode.com/todos/${cnt}`) //triggers api call when count is changed 
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));
}, [cnt]);
    //setInterval(()=>{count()},1000)
    return(
      <div>
        <input value={cnt} onChange={handlechng}></input>
        <button id="btn"onClick={count}>Increment</button>
      </div>
    )
  }
  export default App