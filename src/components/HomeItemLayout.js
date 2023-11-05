import styles from "./homelayout.module.css"
import React from "react";

const HomeItemLayout = ({ items }) => {

    return (

        <div className={styles.masterGrid}>

            {items.map((item) => (
                <div className={styles.gridCellContainer}>
                    <div className={styles.imageContainer}>
                    
                    </div>
                    <div className={styles.infoContainer}>
                        <div><a style={{fontWeight:"bold"}}>Owner: </a>{item[0]}</div>
                        <div><a style={{fontWeight:"bold"}}>Item: </a>{item[1]}</div>
                        <div><a style={{fontWeight:"bold"}}>Condition: </a>{item[2]}</div>
                        <div><a style={{fontWeight:"bold"}}>Location: </a>{item[3]}</div>
                        <div className={styles.buttonParent}>
                            <a className={styles.buttons}>trade</a>
                            <a className={styles.buttons}>message</a>
                        </div>
                    </div>
                    
                </div>

            ))}
        </div>
    );

}

export default HomeItemLayout;