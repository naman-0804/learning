import React, { useState } from "react";
const Form=()=>{
  const [username,setUsername]=useState("");
  const [password,setPassword]=useState("");
  const handlesubmit=async(data)=>{
    data.preventDefault();
    let r=await fetch("http://localhost:3000/",{
      method:"POST",
      body:JSON.stringify({username,password}),
      headers:{"content-type":"application/json"}
    });
    let res= await r.text() //data recieved back from server
    console.log(res)//prints witht ehtdata sent
  }
  return(
    <div>
      <form onSubmit={handlesubmit}>

      <input placeholder="Username"
        value={username} 
        onChange={(e)=>setUsername(e.target.value)}>
      </input>
      <input placeholder="Password" 
        value={password}
        onChange={(e)=>setPassword(e.target.value)}>
      </input>

      <button type='submit' >Submit</button>
      </form>
    </div>
  )
}
export default Form;