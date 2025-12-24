import { useContext } from "react";
import { NameContext } from "./Proivder_usecontext";

function ChildC() {
  const { firstName, lastName } = useContext(NameContext);

  return (
    <h2>
      Child Component: {firstName} {lastName}
    </h2>
  );
}

export default ChildC;
