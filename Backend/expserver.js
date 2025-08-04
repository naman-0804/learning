const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})
app.get('/first',(req,res)=>{
    res.send('This is the first endpoint!')
})
app.get('/second',(req,res)=>{ //path,handler(req,res)
    res.send('This is the second endpoint!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
