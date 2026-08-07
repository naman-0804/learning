import React from "react";
import { useUser } from "@clerk/clerk-react";

function Dashboard() {
  const { isLoaded, user } = useUser();

  if (!isLoaded) return <p>Loading user...</p>;
  if (!user) return <p>No user found</p>;

  return (
    <div>
      <h2>Welcome to the protected landing page {user.firstName}!</h2>
      <p>With user id {user.id}</p>
    </div>
  );
}

export default Dashboard;
