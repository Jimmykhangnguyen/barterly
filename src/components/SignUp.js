import styles from "./login.module.css"
import { React, useState, useEffect, useRef } from "react";

const doSignup = ({ e }) => {

}
function SignUp() {

    const formRef = useRef();

    return (
        <header className="App-header">

            <h3 style={{ color: "white" }}>Sign Up</h3>
            <form style={{ width: '100%', display: 'flex',flexDirection:'column', justifyContent: 'center', alignItems:"center", rowGap:'10px'}} ref={formRef} onSubmit={doSignup}>
                <div className={styles.signUpParent}>
                    <div className={styles.mainBoxSU}>

                        <input className={styles.textStyles} maxlength="30" type="text" id="email" name="email" placeholder='email address' />
                        <input className={styles.textStyles} maxlength="30" type="text" id="username" name="username" placeholder='username' />
                        <input className={styles.textStyles} maxlength="30" type="text" id="password" name="password" placeholder='password' />
                        <input className={styles.textStyles} maxlength="30" type="text" id="passwordmatch" name="passwordmatch" placeholder='password (again)' />

                    </div>
                    <div className={styles.locInfoBox}>
                        <input className={styles.textStyles} maxlength="30" type="text" id="address" name="address" placeholder='address' />
                        <input className={styles.textStyles} maxlength="30" type="text" id="city" name="city" placeholder='city' />
                        <input className={styles.textStyles} maxlength="30" type="text" id="country" name="country" placeholder='country' />
                        <input className={styles.textStyles} maxlength="30" type="text" id="postalcd" name="postalcd" placeholder='postal code' />
                    </div>
                </div>

                <input id='submits' className={styles.submit} maxlength="30" type="submit" value="submit" />

            </form>

        </header>
    );

}

export default SignUp;