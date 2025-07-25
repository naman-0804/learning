import React, { lazy, Suspense } from "react";
//import Data from "./Data";
const Data=lazy(() => import("./Data"));
const Lazyloading=()=>{
    return (
        <div>
        <h1>Lazy Loading Example</h1>
        <Suspense fallback={<div>Loading...</div>} >
            <Data/>
        </Suspense>
        </div>
    );
}
export default Lazyloading;