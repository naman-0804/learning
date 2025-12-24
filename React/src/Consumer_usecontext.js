import { useContext } from "react";
import { NameContext } from "./Proivder_usecontext";

function ChildC() {
  const name = useContext(NameContext);

  return (
    <h2>
      Child Component: Name is {name} that is passed using context 
    </h2>
  );
}

export default ChildC;
