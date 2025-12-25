const express = require('express');
const app = express()
const port = 3000
app.use(express.json());
app.get("/", async (req, res) => {
    try {
        const response = await fetch("https://dummyjson.com/c/3029-d29f-4014-9fb4")
        const data =await response.json()
        res.json(data)
       
    } catch (error) {
        res.status(500).send("ISR")
    }
})
app.post("/post",async(req,res)=>{
    const response=await fetch("https://dummyjson.com/posts/add ",
        {
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(req.body)
        }
    );
    const data = await response.json();
    res.json(data);
})
app.delete("/delete",async(req,res)=>{
    const response=await fetch("https://dummyjson.com/posts/3",
        {
            method:"DELETE",
        })
    const data=await response.json();
    res.json(data)
})
app.listen(port, () => {
    console.log(`Listening on port ${3000}`);
})