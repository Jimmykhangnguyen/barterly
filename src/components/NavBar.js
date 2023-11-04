import React from "react";
import styles from "./menu.module.css";

const NavBar = ({ islogged }) => {

    return (
        <div className={styles.main} href="/profile">

            <div href="/" className={styles.toLanding}>
                <a href="/" className={styles.link}>barterly.</a>
            </div>

            <a className={styles.profile}>

                {islogged ?
                    <svg width="55%" height="75%" viewBox="0 0 184 184" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M184 92C184 142.81 142.81 184 92 184C41.1898 184 0 142.81 0 92C0 41.1898 41.1898 0 92 0C142.81 0 184 41.1898 184 92Z" fill="#181818" />
                        <path d="M116 58.5C116 71.4787 105.479 82 92.5 82C79.5213 82 69 71.4787 69 58.5C69 45.5213 79.5213 35 92.5 35C105.479 35 116 45.5213 116 58.5Z" fill="#888888" />
                        <path d="M130.5 129.5C130.5 147.173 110.673 146 93 146C75.3269 146 57 147.173 57 129.5C57 111.827 75.3269 89.5 93 89.5C110.673 89.5 130.5 111.827 130.5 129.5Z" fill="#888888" />
                    </svg>
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