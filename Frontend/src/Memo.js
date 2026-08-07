import React, { useMemo, useState } from "react";
const Memo=()=>{
    const [add,setAdd] = useState(0); 
    const [state,setState]= useState(false);
    const addition = () => {
    setAdd(add+1);
    }
    function count(add) {
        console.log("Function running",add);
        for (let i = 0; i < 1000000000; i++) {
            // Simulating a heavy computation
        }
        return add;
    }
    let number=useMemo(() => {
        return count(add)
    }, [add]);
    return (
        <>
            <div>
                <h1>{number}</h1>
                <button onClick={addition}>Addition</button>
                <button onClick={() => setState(!state)}>Toggle State</button>
                <p>{state ? "State is true" : "State is false"}</p> 
            </div>
        </>
    )
}
export default Memo;