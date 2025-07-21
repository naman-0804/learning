import react,{useState} from 'react'
const Incdec=()=>{
    const[count,setCount]=useState(0);
    const counter=(event)=>{
        if(event.target.name=='Inc')
        {
            setCount(count+1);
        }
        else if(event.target.name=="dec")
        {
            setCount(count-1);
        }
    }
    return (
        <>
            <div>
                <h1>{count}</h1>
                <button name="Inc" onClick={counter}>Increment</button>
                <button name="dec" onClick={counter}>Decrement</button>
            </div>
        </>
    )

}
export default Incdec;