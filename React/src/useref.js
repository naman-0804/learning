import { useRef } from "react";

function RefCounter() {
  const refCount = useRef(0);

  const handleClick = () => {
    refCount.current += 1;
    console.log("Ref count:", refCount.current);
  };

  return (
    <div>
      <h3>useRef Example</h3>
      <button onClick={handleClick}>
        Click (check console)
      </button>
    </div>
  );
}

export default RefCounter;
