"use client"
import React from 'react';
import './SignInSignUp.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser, faLock, faEnvelope } from '@fortawesome/free-solid-svg-icons';
import { faFacebookF, faTwitter, faGoogle, faLinkedinIn } from '@fortawesome/free-brands-svg-icons';

import {useEffect, useState} from 'react'
import { useRouter } from 'next/navigation'
import axios from 'axios';
import { toast, ToastContainer } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'

const SignInSignUp: React.FC = () => {
  const signInBtnRef = React.useRef<HTMLButtonElement>(null);
  const signUpBtnRef = React.useRef<HTMLButtonElement>(null);
  const containerRef = React.useRef<HTMLDivElement>(null);

  const handleSignUpClick = () => {
    containerRef.current?.classList.add('sign-up-mode');
  };

  const handleSignInClick = () => {
    containerRef.current?.classList.remove('sign-up-mode');
  };

  const router = useRouter()
  const [user, setUser] = useState({
    username: '',
    email: '',
    password: ''
  })

  const [buttonDisabled, setButtonDisabled] = useState(true)
  useEffect(() => {
    if(user.email !== '' && user.password !== '') {
      setButtonDisabled(false)
    } else {
      setButtonDisabled(true)
    }
  }, [user])

  const [loading, setLoading] = useState(false)

  const handleChanges = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUser({...user, [e.target.name]: e.target.value})
  }

  const handleLogin = async (e:React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault()
    try {
      setLoading(true)
      console.log(user)
      const formdata = new FormData() 
      formdata.append('email', user.email)
      formdata.append('password', user.password)
      const response = await axios.post(process.env.NEXT_PUBLIC_LOGIN_URL!, formdata)
      
      if (response.data.jwt) {
        document.cookie = `jwt=${response.data.jwt}; path=/; secure; SameSite=None;`
        console.log(response.data.jwt)
        toast.success('Login successful')
        router.push('/profile')
      }
      else {
        console.log('Login failed')
        toast.error('Login failed')
      }
    } catch (error:any) {
      console.log(error.message)
      
      toast.error(error.message)
      
    } finally {
      setLoading(false)
    }
  }

  const handleSignup = async (e:React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault()
    try {
        setLoading(true)
        console.log(user)
        const formdata = new FormData()
        formdata.append('username', user.username)
        formdata.append('email', user.email)
        formdata.append('password', user.password)
        const response = await axios.post(process.env.NEXT_PUBLIC_SIGNUP_URL!, formdata)
        console.log("response", response.data)
        if (response.data.success) {
            toast.success('Signup successful')
            router.push('/login')
        }
        else {
            console.log('Signup failed')
            toast.error('Signup failed')
        }
        
    } catch (error:any) {
       console.log(error.message)
       toast.error(error.message)
    } finally {
        setLoading(false)
    }
}

  return (
    <div className="container" ref={containerRef}>
      <div className="forms-container">
        <div className="signin-signup">
          <form className="sign-in-form">
            <h2 className="title">Sign in</h2>
            <div className="input-field">
                <FontAwesomeIcon icon={faUser} style={{"padding":"20"}} />
                <input 
                    id="email"
                    name="email"
                    type="email"
                    autoComplete="email"
                    required
                    value={user.email}
                    onChange={handleChanges}
                    placeholder="Email" />
                
            </div>
            <div className="input-field">
              <FontAwesomeIcon icon={faLock} style={{"padding":"20"}}/>
              <input
                  id="password"
                  name="password"
                  type="password"
                  autoComplete="current-password"
                  required
                  placeholder='Password'
                  value={user.password}
                  onChange={handleChanges}
                />
            </div>
            
            <button
                type="submit"
                className='btn solid'
                disabled={buttonDisabled}
                onClick={handleLogin}
              >
                {loading ? "Logging in..." : "Login"}
              </button>
            <p className="social-text">Or Sign in with social platforms</p>
            <div className="social-media">
              <a href="#" className="social-icon">
                <FontAwesomeIcon icon={faFacebookF} />
              </a>
              <a href="#" className="social-icon">
                <FontAwesomeIcon icon={faTwitter} />
              </a>
              <a href="#" className="social-icon">
                <FontAwesomeIcon icon={faGoogle} />
              </a>
              <a href="#" className="social-icon">
                <FontAwesomeIcon icon={faLinkedinIn} />
              </a>
            </div>
          </form>
          <form className="sign-up-form">
            <h2 className="title">Sign up</h2>
            <div className="input-field">
              <FontAwesomeIcon icon={faUser} style={{"padding":"20"}}/>
              <input 
                    id="username"
                    name="username"
                    type="username"
                    autoComplete="username"
                    required
                    value={user.username}
                    onChange={handleChanges}
                    placeholder="Username" />
            </div>
            <div className="input-field">
              <FontAwesomeIcon icon={faEnvelope} style={{"padding":"20"}} />
              <input 
                    id="email"
                    name="email"
                    type="email"
                    autoComplete="email"
                    required
                    value={user.email}
                    onChange={handleChanges}
                    placeholder="Email" />
            </div>
            <div className="input-field">
              <FontAwesomeIcon icon={faLock} style={{"padding":"20"}}/>
              <input
                  id="password"
                  name="password"
                  type="password"
                  autoComplete="current-password"
                  required
                  placeholder='Password'
                  value={user.password}
                  onChange={handleChanges}
                />
            </div>
            <button
                type="submit"
                className='btn solid'
                disabled={buttonDisabled}
                onClick={handleSignup}
              >
                {loading ? "Signing Up..." : "Sign Up"}
              </button>
            <p className="social-text">Or Sign up with social platforms</p>
            <div className="social-media">
              <a href="#" className="social-icon">
                <FontAwesomeIcon icon={faFacebookF} />
              </a>
              <a href="#" className="social-icon">
                <FontAwesomeIcon icon={faTwitter} />
              </a>
              <a href="#" className="social-icon">
                <FontAwesomeIcon icon={faGoogle} />
              </a>
              <a href="#" className="social-icon">
                <FontAwesomeIcon icon={faLinkedinIn} />
              </a>
            </div>
          </form>
        </div>
      </div>

      <div className="panels-container">
        <div className="panel left-panel">
          <div className="content">
            <h3>New here ?</h3>
            <p>
              Lorem ipsum, dolor sit amet consectetur adipisicing elit. Debitis,
              ex ratione. Aliquid!
            </p>
            <button className="btn transparent" id="sign-up-btn" ref={signUpBtnRef} onClick={handleSignUpClick}>
              Sign up
            </button>
          </div>
          <img src="/log.svg" className="image" alt="" />
        </div>

        <div className="panel right-panel">
          <div className="content">
            <h3>One of us ?</h3>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum
              laboriosam ad deleniti.
            </p>
            <button className="btn transparent" id="sign-in-btn" ref={signInBtnRef} onClick={handleSignInClick}>
              Sign in
            </button>
          </div>
          <img src="/register.svg" className="image" alt="" />
        </div>
      </div>
      <ToastContainer />
    </div>
  );
};

export default SignInSignUp;