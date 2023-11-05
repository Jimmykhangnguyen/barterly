import './App.css';
import Landing from './components/Landing';
import UserProfile from './components/UserProfile';
import Login from './components/Login';
import NavBar from './components/NavBar';
import SignUp from './components/SignUp';
import { Routes, Route } from 'react-router-dom';
import {React, useState, useEffect} from 'react';

function App() {

  const [isLogged, setIsLogged] = useState(JSON.parse(localStorage.getItem('username')));
  const [currentUser, setCurrentUser] = useState(JSON.parse(localStorage.getItem('loggedin')));

  const handleUserDataDelta = (username, success) => {
    setCurrentUser(username);
    setIsLogged(success);
  };

  return (
    <div className="App">
      <NavBar islogged={isLogged}/>
      <Routes>
          <Route path='/' element={<Landing/>} />
          <Route path="/profile" element={<UserProfile/>}/>
          <Route path="/login" element={<Login userDataCallback={handleUserDataDelta}/>}/>
          <Route path="/signup" element={<SignUp/>}/>
      </Routes>
    </div>
  );
}

export default App;
