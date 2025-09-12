const express=require('express');
const app=express();
const port=3000;
app.get('/',(req,res)=>{
    res.send("Hello world")
})
app.get('/about',(req,res)=>{
    res.send("About page")
})
app.get('/contact',(req,res)=>{
    res.send("Contact page")
})
app.get('/blog',(req,res)=>{
    res.send("Blog page")
})
app.listen(port,()=>{
    console.log(`Server is running on http://localhost:${port}`)
})