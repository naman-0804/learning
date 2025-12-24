import Counter from "./usestate";
import ApiFetcher from "./useffect";
import RefCounter from "./useref";
import { useState } from "react";
import ChildC from "./Proivder_usecontext";  
function App() {
  const [cnt, setCnt] = useState(1);

  return (
    <div>
      <Counter cnt={cnt} setCnt={setCnt} />
      <ApiFetcher cnt={cnt} />
      <RefCounter />
      <ChildC/>
    </div>
  );
}

export default App;
