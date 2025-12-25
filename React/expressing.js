const express = require('express');
const app = express()
const port = 3000
app.get("/", async (req, res) => {
    try {
        const response = await fetch("https://dummyjson.com/c/3029-d29f-4014-9fb4")
        const data =await response.json()
        res.json({
            query:req.query,
            apiData: data
        })
        console.log("User ID received");
       
    } catch (error) {
        res.status(500).send("ISR")
    }
})
app.listen(port, () => {
    console.log(`Listening on port ${3000}`);
})