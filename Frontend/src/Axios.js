import axios from "axios";
import React, { useEffect, useState } from "react";

const Axios=()=>{
    const[store,setStore]=useState();
    // const getData = ()=>{
    //     axios.get("https://jsonplaceholder.typicode.com/posts")
    //     .then((res)=>{
    //         console.log(res.data);
    //         setStore(res.data);
    //     })
    //     .catch((err)=>{
    //         console.error("Error fetching data:", err);
    //     });
    // }

//async await
    const getData = async ()=>{
        try{
            const response = await axios.get("https://jsonplaceholder.typicode.com/posts")
            console.log(response.data);
        }
        catch(err){
            console.error("Error fetching data:", err);
        }
    }



    useEffect(() => {
        getData();
    }, []); //1 time call after render

    return(
        <div>
            <h1>Axios Example</h1>
            <p>Check the console for fetched data.</p>
        </div>
    )
}
export default Axios;