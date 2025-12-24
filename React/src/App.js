import { BrowserRouter, Routes, Route } from "react-router-dom";
import Counter from "./usestate";
import ApiFetcher from "./useffect";
import RefCounter from "./useref";
import { useState } from "react";
import ChildC from "./Proivder_usecontext";
import GetData from "./axios";  
function App() {
  const [cnt, setCnt] = useState(1);

  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/usestate" element={<Counter cnt={cnt} setCnt={setCnt} />} />
          <Route path="/useeffect" element={<ApiFetcher cnt={cnt} />} />
          <Route path="/useref" element={<RefCounter />} />
          <Route path="/usecontext" element={<ChildC />} />
          <Route path="/axios" element={<GetData />} />
          <Route path="*" element={<h2>Welcome to React Hooks Examples. Please select a hook from below.</h2>} />
        </Routes>
      </BrowserRouter>
      <nav>
        <a href="/usestate">useState</a> |{" "}
        <a href="/useeffect">useEffect</a> |{" "}
        <a href="/useref">useRef</a> |{" "}
        <a href="/usecontext">useContext</a>
        <a href="/axios"> | Axios Example</a>
      </nav>
    </div>
  );
}

export default App;
