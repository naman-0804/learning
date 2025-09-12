const express=require('express');
const app=express();

const blog=require('./routes/blog.js')

app.use(express.static('public'));
app.use('/blog',blog);
//http://localhost:3000/naman.txt accessible
const port=3000;
app.get('/',(req,res)=>{
    res.send("Hello world")
})
app.post('/',(req,res)=>{
    res.send("Hello world post request")
})
app.get('/about',(req,res)=>{
    res.send("About page")
})
app.get('/index',(req,res)=>{
    res.sendFile('templates/index.html',{root:__dirname});
});
app.get('/contact',(req,res)=>{
    res.send("Contact page")
})
app.get('/blog',(req,res)=>{
    res.send("Blog page")
})
app.get('/api',(req,res)=>{
    res.json({name:"naman",age:22,city:"delhi"})
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