import react,{useEffect, useState} from 'react'

const Incdec=()=>{
    const[count,setCount]=useState(0);
    const counter=(event)=>{
        if(event.target.name=='Inc')
        {
            setCount(count+1);
        }
        else if(event.target.name=="dec")
        {
            if(count==0)
            {
                alert("Cant decrement further")
            }
            else{
                setCount(count-1);
            }
        }
    }
    useEffect(()=>{
        console.log("Running useEffect()");
    } ,[count])
    return (
        <>
            <div>
                <h1 id="cn">{count}</h1>
                <button id="btn" name="Inc" onClick={counter}>Increment</button>
                <button id="btn" name="dec" onClick={counter}>Decrement</button>
            </div>
        </>
    )

}
export default Incdec;