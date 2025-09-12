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
// app.get('/blog/intro-to-js',(req,res)=>{
//     res.send("Into to js page")
// })
app.get('/blog/:slug',(req,res)=>{
    res.send(`hello ${req.params.slug} blog page`)
    console.log(req.params)
    console.log(req.query)
    //http://localhost:3000/blog/introdfh?mode=dark&region=in
})
app.listen(port,()=>{
    console.log(`Server is running on http://localhost:${port}`)
})