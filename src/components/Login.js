import styles from "./login.module.css"
import { React, useState, useEffect, useRef } from "react";

const doLogin = ({ e }) => {

}
function Login() {

    const formRef = useRef();

    return (
        <header className="App-header">


            <form style={{ width: '100%', display: 'flex', justifyContent: 'center' }} ref={formRef} onSubmit={doLogin}>
                <div className={styles.mainBox}>
                    <h3 style={{color: "black"}}>Log in</h3>
                    <input className={styles.textStyles} maxlength="30" type="text" id="username" name="username" placeholder='username' />
                    <input className={styles.textStyles} maxlength="30" type="text" id="password" name="username" placeholder='password' />
                    <input id='submits' className={styles.submit} maxlength="30" type="submit" value="submit" />
                    <p className={styles.newTo}>New to barterly? Sign up <a style={{color: "#555555"}}href="/#/signup">here</a></p>
                </div>
            </form>


        </header>
    );

}

export default Login;