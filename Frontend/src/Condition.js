import react from 'react'
// const MyFun=()=>{
//     let age=20;
//     if(age>=18){
//         return(
//             <h1>Eligible for vote</h1>
//         )
//     }
//     else
//     {
//         return(
//         <h1>Not Eligible for vote</h1>
//         )
//     }
//     
// }
const Condition=()=>{
    let age=20;
    //let result;
    // if(age>=18){
    //     return(
    //         <h1>Eligible for vote</h1>
    //     )
    // }
    // else
    // {
    //     return(
    //     <h1>Not Eligible for vote</h1>
    // )
    // }
    // if(age>18)
    // {
    //     result=<h1>You can Vote</h1>
    // }
    // else
    // {
    //     result =<h1>You can't vote</h1>
    // }
    return(
        <>
            <div>
                {age>18 ?<h1>Eligible to vote</h1>:<h1>Not eligible to vote</h1>}    
            </div>
        </>
    )

}
export default Condition; 