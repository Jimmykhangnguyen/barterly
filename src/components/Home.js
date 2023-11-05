import styles from "./home.module.css"
import { React, useState, useEffect, useRef } from "react";
import axios from 'axios';

function Home() {

    const [isDisabled, setIsDisabled] = useState(false);
    function handleSearchFilter() {

    }
    const formRef = useRef();
    return (
        <header className="App-header">

            <form style={{ width: '100%', display: 'flex', justifyContent: 'center' }} ref={formRef} onSubmit={handleSearchFilter}>

                <div className={styles.mainBox}>
                    <div className={styles.searchParent}>
                        <input className={styles.textStyles} maxlength="50" type="text" id="searchfield" name="searchfield" placeholder='what are you looking for?' />
                        <input disabled={isDisabled} id='submits' className={styles.submit} maxlength="30" type="submit" value="search" />

                    </div>
                </div>
            </form>

        </header>
    );

}

export default Home;