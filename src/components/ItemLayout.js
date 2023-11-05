import styles from "./layout.module.css"
import React from "react";

const ItemLayout = ({ items }) => {

    return (

        <div className={styles.masterGrid}>

            {items.map((item) => (
                <div className={styles.gridCellContainer}>
                    <div className={styles.imageContainer}>
                    
                    </div>
                    <div className={styles.infoContainer}>
                        <div><a style={{fontWeight:"bold"}}>Type: </a>{item[1]=="STN"?"Stationary":item[1]=="ELE"? "Electronics" : item[1]=="CLO"? "Clothes" : "Miscellaneous"}</div>
                        <div><a style={{fontWeight:"bold"}}>Condition: </a>{item[3]}</div>
                        <div><a style={{fontWeight:"bold"}}>Location: </a>{item[5]}</div>
                    </div>
                    
                </div>

            ))}
        </div>
    );

}

export default ItemLayout;