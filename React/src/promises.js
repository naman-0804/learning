import { useState } from "react";

function Promises() {
    const [message,setMessage]=useState("")
    let pro = new Promise((resolve, reject) => {
        setTimeout(()=>{        
        let api = false;
        if (api) {
            resolve("Resolved");
        }
        else {
            reject("Reject");
        }
    },5000)

    });
    pro.then((resolve)=>{
        console.log("Msg resolved")
        setMessage(resolve)
    })
    .catch((err)=> {
        console.log("Rejected")
        setMessage(err)
    })
    return (
        <div>
            <p>The message returned is {message}</p>
        </div>
    )
}
export default Promises