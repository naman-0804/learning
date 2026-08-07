import react, { useEffect, useRef, useState } from 'react';
const Ref=()=>{
    const [val,setVal]=useState("");
    const refElem=useRef(0);
    const change=(event)=>{
        setVal(event.target.value)
        //refElem.current=refElem.current+1;
    }
    const submit=()=>{
        refElem.current.style.color="red"
    }
    //useEffect(()=>{
     //   setNum(num+1);
   // }) //this will go infineitly as rerenders after every num+1

   return(
        <>
            <div className='container'>
                <h1>useRef hook: </h1>
                <input type='text' ref={refElem} value={val} onChange={change}/>
                <button onClick={submit}></button>
                
            </div>
        </>
    )
}
export default  Ref;