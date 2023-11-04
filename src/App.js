import './App.css';
import Landing from './components/Landing';
import UserProfile from './components/UserProfile';
import Login from './components/Login';
import NavBar from './components/NavBar';
import { Routes, Route } from 'react-router-dom';
import {React, useState, useEffect} from 'react';

function App() {

  const [isLogged, setisLogged] = useState(false);

  return (
    <div className="App">
      <NavBar islogged={isLogged}/>
      <Routes>
          <Route path='/' element={<Landing/>} />
          <Route path="/profile" element={<UserProfile/>}/>
          <Route path="/login" element={<Login/>}/>
      </Routes>
    </div>
  );
}

export default App;
