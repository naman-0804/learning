import { useRef } from "react";

function RefDemo() {
  console.log("🔄 Component rendered");

  const clicks = useRef(0);

  return (
    <div>
    <h1>UserRef example</h1>
    <button
      onClick={() => {
        clicks.current++;
        console.log("Clicks:", clicks.current);
      }}
    >
      Click me
    </button>
    </div>
  );
}

export default RefDemo;
