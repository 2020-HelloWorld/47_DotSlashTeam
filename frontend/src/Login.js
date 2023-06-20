import React, { useState } from 'react';
import './Login.css';
import { useHistory } from 'react-router-dom';
import axios from 'axios';
import Cookies from 'js-cookie';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();

  const handleGoToNext = (who) => {
    if (who === 'students') {
      history.push('/home');
      window.location.reload();
    } else if (who === 'clubs') {
      history.push('/ClubEventList');
      window.location.reload();

    } else if (who === 'faculties') {
      history.push('/home');
      window.location.reload();
    }
  };

 

  const setCookie = (name, value, options = {}) => {
    Cookies.set(name, value, options);
  };

  const handleLoginSubmit = async (e) => {
    e.preventDefault();
  
    try {
      const jsonData = {
        id: username,
        passwd: password,
        //type:"login"
      };
  
      axios.post('http://192.168.156.204:4000/login', jsonData, {
          withCredentials: true, // Include this option to send cookies
          headers: {
            'Content-Type': 'application/json',
          },
        })
        .then((response) => {
          console.log(document.cookie+"hi")
          console.log(response.data['sessionid']);
          setCookie('sessionid',response.data['sessionid'],{expires:7});

          if (response.status === 200) {
            handleGoToNext(response.data['group']);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    } catch (error) {
      console.error('Error occurred while logging in:', error);
    }
  };

  
  return (
    <div className="login-container">
      <h2 className="htwo">Login</h2>
      <form className="login-form" onSubmit={handleLoginSubmit}>
        <input
          type="text"
          placeholder="Username"
          className="input-field"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          className="input-field"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit" className="login-button">
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;