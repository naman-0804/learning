import { createContext } from "react";
import ChildC from "./Consumer_usecontext";

export const NameContext = createContext("");

function Parent() {
  return (
    <NameContext.Provider value="Naman Srivastava">
      <ChildC />
    </NameContext.Provider>
  );
}

export default Parent;
