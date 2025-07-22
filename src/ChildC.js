import React from "react";
function ChildC({ name }) {
  return (
    <div>
      <h2>Child C</h2>
      <p>Name: {name}</p>
      <p>Child C is a component that receives the name prop from Child A.</p>
    </div>
  );
}

export default ChildC;
