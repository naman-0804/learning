import express from 'express'
import cors from 'cors'
const app=express();
app.use(cors())
app.use(express.json());
const port=3000;
app.get('/',(req,res)=>{
    res.send("my server");
})
app.post('/',(req,res)=>{
    console.log(req.body);
    res.send("Data received");
})
app.listen(port,()=>{
    console.log(`Listen on port:${port}`)
})