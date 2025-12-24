import axios from "axios";
import { useEffect, useState } from "react";
function GetData() {
    const [data, setData] = useState(null);
    useEffect(() => {
        axios.get("https://jsonplaceholder.typicode.com/todos/3")
            .then((res) => {
                console.log(res.data);
                setData(res.data);
            })
            .catch((err) => {
                console.log(err);
            })
    }, [])
    if (!data) return <h1>Loading...</h1>;
    return (
        <div>
            <h1>The data is:</h1>
            <p>ID: {data.id}</p>
            <p>Title: {data.title}</p>
            <p>Completed: {data.completed.toString()}</p>
        </div>
    );
}
export default GetData;