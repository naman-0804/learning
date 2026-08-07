import express from 'express'
import cors from 'cors'
import mongoose from 'mongoose';
const app=express();
app.use(cors())
app.use(express.json());
const port=3000;
await mongoose.connect("mongodb+srv://namansrivastava1608_db_user:nlq1IdzwCTj4p0ly@cluster0.6cthoda.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",{
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
console.log("connected to mongodb");
const userSchema=new mongoose.Schema({
    id: Number,
    username: { type: String, required: true },
    password: { type: String, required: true },
})
const User=mongoose.model("User",userSchema);
app.get('/',(req,res)=>{
    res.send("my server");
})
app.post('/',async (req,res)=>{
    const {username,password}=req.body;
    if (!username || !password) {
      return res.status(400).send("Username and password required");
    }
    const newUser=new User({username,password,id:Date.now()});
    await newUser.save();
    console.log("Saved to DB:", newUser);
    //console.log(req.body);
    res.send("Data received and saved");
})
app.get('/users',async(req,res)=>{
    const users=await User.find({});
    res.json(users);
})
app.listen(port,()=>{
    console.log(`Listen on port:${port}`)
})