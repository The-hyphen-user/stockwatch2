import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { TextField, Button } from "@material-ui/core";
import { useNavigate } from "react-router-dom";

const Login = () => {

  const URL = '127.0.0.1:8000'
  let navigate = useNavigate();

    const [email, setEmail] = useState('admin@email.com')
    const [password, setPassword] = useState('password')
    const [error, setError] = useState('')
    const [loading, setLoading] = useState(false)

    const handleSubmit = (e) => {
        e.preventDefault()
      //http://127.0.0.1:8000/api/token/
      axios.post(`http://${URL}/api/token/`, {
        email: email,
        password: password
      })
      // .then(res => {
      //   console.log(res)
      //   console.log(res.data)
      // })
      .then(res => {
        //set bearer token
        localStorage.setItem('token', res.data.access)
      })
      .then(() => {
        navigate("/user", { replace: true })})
    }

  return (
    <div>
      <div className="login-container">
        <TextField
          label="Email"
          variant="outlined"
          onChange={(e) => setEmail(e.target.value)}
          value={email}
        />
        <br />
        <br />
        <TextField
          id="outlined-password-input"
          label="Password"
          variant="outlined"
          autoComplete="current-password"
          type="password"
          onChange={(e) => setPassword(e.target.value)}
          value={password}
        />
        <br />
        <br />
        <Button onClick={handleSubmit} variant="contained">
          Log In
        </Button>

      </div>



    </div>
  )
}

export default Login