import React from "react";
import styles from "./menu.module.css";

const NavBar = ({ islogged }) => {

    function Logout(){
        localStorage.setItem('username', JSON.stringify(""));
        localStorage.setItem('loggedin', JSON.stringify(false));
    }
    return (
        <div className={styles.main} href="/profile">

            <div href="/" className={styles.toLanding}>
                <a href="/" className={styles.link}>barterly.</a>
            </div>

            <a className={styles.profile}>

                {islogged ?
                    <div style={{ color: "white", display: "flex" }}>
                        <a className={styles.link} href="/#/profile">Profile</a>
                        <a className={styles.link} style={{ marginLeft: "20px" }} onClick={Logout}>Logout</a>
                    </div>
                    :
                    <div style={{ color: "white", display: "flex" }}>
                        <a className={styles.link} href="/#/login">Log In</a>
                        <a className={styles.link} href="/#/signup" style={{ marginLeft: "20px" }}>Sign Up</a>
                    </div>
                }


            </a>


        </div>
    );

}

export default NavBar;