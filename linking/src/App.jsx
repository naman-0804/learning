import { set } from "mongoose";
import React, { useEffect, useState } from "react";
const Form=()=>{
  const [username,setUsername]=useState("");
  const [password,setPassword]=useState("");
  const [users,setUsers]=useState([]);
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
  useEffect(()=>{
    const fetchUser =async()=>{
      let r=await fetch("http://localhost:3000/users")
      let res= await r.json();
      setUsers(res);
      console.log(res)
    }
    fetchUser();
    const interval = setInterval(fetchUser, 5000);
    return () => clearInterval(interval);
  },[]);
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
      <div>
        <ul>
          {users.map((u) => (
            <li key={u._id}>
              Username: {u.username} | Password: {u.password}
            </li>
          ))}
        </ul>          
      </div>
    </div>
  )
}
export default Form;