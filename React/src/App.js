import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Counter from "./usestate";
import ApiFetcher from "./useffect";
import RefCounter from "./useref";
import { useState } from "react";
import ChildC from "./Proivder_usecontext";
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
        </Routes>
      </BrowserRouter>
      <nav>
        <a href="/usestate">useState</a> |{" "}
        <a href="/useeffect">useEffect</a> |{" "}
        <a href="/useref">useRef</a> |{" "}
        <a href="/usecontext">useContext</a>
      </nav>
    </div>
  );
}

export default App;
