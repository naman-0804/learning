import react,{useState} from 'react'
function Form(){
    const[fname,setFname]=useState("") ;
    const[lname,setLname]=useState("");
    const[show,setShow]=useState("") ;

    const getName=(event)=>{
        if(event.target.name=='fn'){
            setFname(event.target.value);
        }
        else{
            setLname(event.target.value)
        }
    }
    const submitbtn=(event)=>{
        event.preventDefault();
        setShow(fname+" "+ lname);
    }
    return(
        <>
            <form onSubmit={submitbtn}>
                <h1>{show}</h1>
                <label>Enter first Name</label>
                <input type='text' name="fn" onChange={getName} value={fname}></input>
                <input type='text' name="ln" onChange={getName} value={lname}></input>
                <button type='submit'>Submit</button>
            </form>
        </>
    )
}
export default Form;