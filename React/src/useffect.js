import { useEffect } from "react";

function ApiFetcher({ cnt }) {

  useEffect(() => {
    fetch(`https://jsonplaceholder.typicode.com/todos/${cnt}`)
      .then(res => res.json())
      .then(data => console.log("API DATA:", data))
      .catch(err => console.error(err));
  }, [cnt]);

  return (
    <div>
      <h3>useEffect Example</h3>
      <p>Check console for API response</p>
    </div>
  );
}

export default ApiFetcher;
