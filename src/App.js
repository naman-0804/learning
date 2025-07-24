import './App.css';
import React,{createContext, useState} from 'react'
import {BrowserRouter,Routes,Route} from 'react-router-dom';
import Home from './Home';
import About from './About';
import MainPage from './MainPage';
import Condition from './Condition';
import Clock from './Clock';
import Events from './Events';
import Form from './Form';
import Incdec from './Incdec';
import Ref from './Ref';
import Memo from './Memo';
import Callback from './Callback';
import Error from './Error'; 
const App=()=> { 
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/mainpage" element={<MainPage />} />
          <Route path="/condition" element={<Condition />} />

          <Route path="/clock/" element={<Clock />} >
            <Route path="form" element={<Form />} />
          </Route>
        
          <Route path="/events" element={<Events />} />
          <Route path="/form" element={<Form />} />
          <Route path="/incdec" element={<Incdec />} />
          <Route path="*" element={<Error/>} />
        </Routes>
      </BrowserRouter>
    </>
  );
} 

export default App;
