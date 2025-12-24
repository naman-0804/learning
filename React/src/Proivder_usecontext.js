import { createContext } from "react";
import ChildC from "./Consumer_usecontext";

export const NameContext = createContext(null);

function Parent() {
  return (
    <NameContext.Provider value={{ firstName: "Naman", lastName: "Srivastava" }}>
      <ChildC />
    </NameContext.Provider>
  );
}

export default Parent;
