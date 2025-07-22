import React from "react";
import ChildC from "./ChildC";
function ChildA({ name }) {
  return (
    <div>
      <ChildC name={name} />
      <p>Child A is a component that receives the name prop from its parent.</p>
    </div>
  );
}
export default ChildA;