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
                </div>
            </form>


        </header>
    );

}

export default Login;