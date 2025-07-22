import react, { useEffect, useRef, useState } from 'react';
const Ref=()=>{
    const [val,setVal]=useState("");
    const refElem=useRef(0);
    const change=(event)=>{
        setVal(event.target.value)
        refElem.current=refElem.current+1;
    }
    //useEffect(()=>{
     //   setNum(num+1);
   // }) //this will go infineitly as rerenders after every num+1

   return(
        <>
            <div className='container'>
                <h1>useRef hook: </h1>
                <input type='text' value={val} onChange={change}/>
                <h1>Count:{refElem.current}</h1>
            </div>
        </>
    )
}
export default Ref;