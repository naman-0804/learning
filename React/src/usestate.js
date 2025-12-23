function Counter({ cnt, setCnt }) {
  return (
    <div>
      <input
        value={cnt}
        onChange={(e) => setCnt(Number(e.target.value))}
      />
      <button onClick={() => setCnt(cnt+1)}>
        Increment
      </button>
    </div>
  );
}

export default Counter;
