import React, { useState } from 'react'

const Login = (props) => {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [loginError, setLoginError] = useState('')

  const onButtonClick = () => {
    login()
  }

  const login = () => {
    let jData = JSON.stringify({
        username: username,
        password: password
        });
    fetch("http://localhost:5000/login", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
          },
        body: jData
    })
    .then(
        (response) => 
        {
            if (response.status === 200) {
                console.log("login in progress");
                return (response.json()) ;
            }
            else
                return ([ ["status ", response.status]]);
        })
    .then(loginResult => {
        setLoginError(loginResult)
    })
}

  return (
    <div className={'mainContainer'}>
      <div className={'titleContainer'}>
        <div>Login</div>
      </div>
      <br />
      <div className={'inputContainer'}>
        <input
          value={username}
          placeholder="Enter your username here"
          onChange={(ev) => setUsername(ev.target.value)}
          className={'inputBox'}
        />
      </div>
      <br />
      <div className={'inputContainer'}>
        <input
          value={password}
          placeholder="Enter your password here"
          onChange={(ev) => setPassword(ev.target.value)}
          className={'inputBox'}
        />
        <label className="errorLabel">{loginError}</label>
      </div>
      <br />
      <div className={'inputContainer'}>
        <input className={'inputButton'} type="button" onClick={onButtonClick} value={'Log in'} />
      </div>
    </div>
  )
}

export default Login