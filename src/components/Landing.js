import styles from "./landing.module.css"
import React from "react";

function Landing() {

    return (
        <header className="App-header">

            <h1 className="barterlytext">barterly.</h1>
            <h3 className={styles.startContainer}>
                <div style={{width: "50%", display: "flex", justifyContent:"right", marginRight:"50px"}}>start trading</div>
                <div className={styles.fancyArrow} style={{ width: "50%", height: "100%" }}>
                    <svg width="30%" height="50%" viewBox="0 0 422 90" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M420.243 49.2426C422.586 46.8995 422.586 43.1005 420.243 40.7574L382.059 2.57359C379.716 0.230447 375.917 0.230447 373.574 2.57359C371.23 4.91674 371.23 8.71573 373.574 11.0589L407.515 45L373.574 78.9411C371.23 81.2843 371.23 85.0833 373.574 87.4264C375.917 89.7696 379.716 89.7696 382.059 87.4264L420.243 49.2426ZM0 51H416V39H0V51Z" fill="white" />
                    </svg>
                </div>
            </h3>

        </header>
    );

}

export default Landing;