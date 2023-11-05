import styles from "./login.module.css"
import { React, useState, useEffect, useRef } from "react";
import axios from 'axios';

function SignUp() {

    const formRef = useRef();
    const [queryString, setQueryString] = useState("");
    const [authData, setAuthData] = useState();
    const [notif, setNotif] = useState("Sign Up");

    function doSignup(event) {
        event.preventDefault(); // Prevent the default form submission

        const formState = event.target;
        const passwd = formState.password.value.trim();
        const passwdmtc = formState.password.value.trim();

        if (passwd === passwdmtc && passwd.split(' ').join('_') === passwd) {
            let qs = formState.username.value.trim() + "+" +
                formState.email.value.trim() + "+" +
                passwd + "+" +
                formState.postalcd.value.trim() + "+" +
                formState.city.value.trim() + "+" +
                formState.name.value.trim();

            setQueryString(qs.split(' ').join('_'));
        } else {
            setNotif("Passwords Don't Match or Invalid Password.")
        }

    }

    useEffect(() => {
        // Only make the API request if the username is not empty
        axios
            .get(`http://100.66.68.63:8080/add_user?query=${queryString}`)
            .then((response) => {
                setAuthData(response.data); // Assuming the API returns a success flag
                console.log(authData);
            })
            .catch((error) => {
                console.error(error);
            });
    }, [queryString]);
    useEffect(() => {
        if(authData && queryString){
            window.location.href = "/#/login";
        }
    }, [authData]);

    return (
        <header className="App-header">

            <h3 style={{ color: "white" }}>{notif}</h3>
            <form style={{ width: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: "center", rowGap: '10px' }} ref={formRef} onSubmit={doSignup}>
                <div className={styles.signUpParent}>
                    <div className={styles.mainBoxSU}>

                        <input className={styles.textStyles} maxlength="30" type="text" id="email" name="email" placeholder='email address' />
                        <input className={styles.textStyles} maxlength="30" type="text" id="username" name="username" placeholder='username' />
                        <input className={styles.textStyles} maxlength="30" type="password" id="password" name="password" placeholder='password' />
                        <input className={styles.textStyles} maxlength="30" type="password" id="passwordmatch" name="passwordmatch" placeholder='password (again)' />

                    </div>
                    <div className={styles.locInfoBox}>
                        <input className={styles.textStyles} maxlength="30" type="text" id="name" name="name" placeholder='name (first last)' />
                        <input className={styles.textStyles} maxlength="30" type="text" id="address" name="address" placeholder='address' />
                        <input className={styles.textStyles} maxlength="30" type="text" id="city" name="city" placeholder='city' />
                        <input className={styles.textStyles} maxlength="30" type="text" id="postalcd" name="postalcd" placeholder='postal code' />
                    </div>
                </div>

                <input id='submits' className={styles.submit} maxlength="30" type="submit" value="submit" />

            </form>

        </header>
    );

}

export default SignUp;