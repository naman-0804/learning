import axios from 'axios';
import React from 'react'

const Axiospost = () => {
    const data= {
        fname: "",
        lname: ""
    }
    const [input, setInput] = React.useState(data);
    const handle = (e) => {
        console.log(e.target.value);
        setInput({...input,[e.target.name]: e.target.value});
    }
    const handlevent = (e) => {
        e.preventDefault();
        axios.post("https://jsonplaceholder.typicode.com/todos", input)
        .then((res) => {
            console.log("Data posted successfully:", res.data);
        })
        .catch((err) => {
            console.error("Error posting data:", err);
        });
    }
    const handleUpdate = () => {
        axios.put("https://jsonplaceholder.typicode.com/todos/1", input)
        .then((res) => {
            console.log("Data updated successfully:", res.data);
        })
        .catch((err) => {
            console.error("Error updating data:", err);
        });
    }
  return (
    <div>
    <form onSubmit={handlevent}>
        <input type="text" name="fname" placeholder="Enter title" onChange={handle}/>
        <input type="text" name="lname" placeholder="Enter srname" onChange={handle}/>
        <button type="submit">Submit</button>
        <button onClick={handleUpdate}>update</button>
    </form>
        <p>First Name: {input.fname}</p>
        <p>Last Name: {input.lname}</p>
    
    </div>
  )
}

export default Axiospost