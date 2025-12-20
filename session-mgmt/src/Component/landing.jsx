import {
  SignedIn,
  SignedOut,
  SignInButton,
  UserButton,
  ClerkLoaded,
  ClerkLoading,
} from "@clerk/clerk-react";
import Dashboard from "./dashboard";
import React from "react";
export default function Landing() {
  return (
    <div style={{ padding: "2rem" }}>
      <ClerkLoading>
        <p>Loading auth...</p>
      </ClerkLoading>

      <ClerkLoaded>
        <SignedOut>
          <SignInButton mode="modal" />
        </SignedOut>

        <SignedIn>
          <UserButton />
          <h1>Session active</h1>
          <Dashboard/>
        </SignedIn>
      </ClerkLoaded>
    </div>
  );
}
