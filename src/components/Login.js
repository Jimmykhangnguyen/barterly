import styles from "./login.module.css"
import { React, useState, useEffect, useRef } from "react";
import axios from 'axios';

function Login({ userDataCallback }) {

    const formRef = useRef();
    const [authData, setAuthData] = useState([]);
    const [username, setUsername] = useState("");
    const [name, setName] = useState("");
    const [submissionState, setSubmissionState] = useState(false);
    const [pass, setPass] = useState("");
    const [loginSuccess, setLoginSuccess] = useState(null);
    const [isDisabled, setIsDisabled] = useState(false);

    useEffect(() => {
        if (username) {
            // Only make the API request if the username is not empty
            axios
                .get(`http://100.66.68.63:8080/get_login?query=${username}`)
                .then((response) => {
                    setAuthData(response.data); // Assuming the API returns a success flag
                })
                .catch((error) => {
                    console.error(error);
                    setLoginSuccess(false); // Set loginSuccess to false on error
                }); 
        }
    }, [submissionState]); 
    useEffect(() => {
        if(authData[0]){
            validateLogin();
        }
    }, [authData]); 

    function redirectHome() {
        localStorage.setItem('username', JSON.stringify(username));
        localStorage.setItem('logged', JSON.stringify(true));
        localStorage.setItem('nameDisplay', JSON.stringify(authData[0][1]));

        // console.log(username);
        console.log(JSON.parse(localStorage.getItem("logged")));
        // console.log(authData[0][1]);

        window.location.href = "/";
    }
    function validateLogin() {

        if (authData[0][0] === pass) { 
            setLoginSuccess(true);
            setName(authData[0][1].toString());
            redirectHome();

        } else { 
            setLoginSuccess(false); 
            setIsDisabled(false); 
        }
    }
    function setUserState(event) {

        event.preventDefault(); // Prevent the default form submission
        const formState = event.target;
        setUsername(formState.username.value.trim());
        setPass(formState.password.value.trim());
        setIsDisabled(true);
        setSubmissionState(!submissionState);

    }

    userDataCallback(username, loginSuccess, name);

    return (
        <header className="App-header">


            <form style={{ width: '100%', display: 'flex', justifyContent: 'center' }} ref={formRef} onSubmit={setUserState}>
                <div className={styles.mainBox}>
                    <h3 style={{ color: "black" }}>Log in</h3>
                    <input className={styles.textStyles} maxlength="30" type="text" id="username" name="username" placeholder='username' />
                    <input className={styles.textStyles} maxlength="30" type="password" id="password" name="password" placeholder='password' />
                    <input disabled={isDisabled} id='submits' className={styles.submit} maxlength="30" type="submit" value="submit" />
                    <p className={styles.newTo}>New to barterly? Sign up <a style={{ color: "#555555" }} href="/#/signup">here</a></p>
                </div>
            </form>


        </header>
    );

}

export default Login;