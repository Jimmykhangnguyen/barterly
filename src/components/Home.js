import styles from "./home.module.css"
import HomeItemLayout from "./HomeItemLayout";
import { React, useState, useEffect, useRef } from "react";
import axios from 'axios';

function Home() {

    const [isDisabled, setIsDisabled] = useState(false);

    const [dataStream, setDataStream] = useState([]);
    const [makeRequest, setMakeRequest] = useState(false);
    const [requestType, setRequestType] = useState("get_marketplace");
    const [rqCount, setRqCount] = useState(0);

    const username = JSON.parse(localStorage.getItem('username'));
    const isLogged = JSON.parse(localStorage.getItem('logged'));

    function handleEmptyUser() {
        if (!(username && isLogged)) {
            window.location.href = "/";
        } else {
            setMakeRequest(!makeRequest);
        }
    }
    function checkValidity(data) {
        if (!data && rqCount < 2) {
            setMakeRequest(!makeRequest);
            setRqCount(rqCount + 1);
        } else {
            if (!data) {
                window.location.href = "/";
            } else {
                console.log(data)
                setDataStream(data)
            }
        }
    }
    window.onload = function () { handleEmptyUser(); };

    useEffect(() => {
        axios
            .get(`http://localhost:8080/${requestType}`)
            .then((response) => {
                checkValidity(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    }, [makeRequest]);// On change of mkrq. 

    function handleSearchFilter(event) {
        event.preventDefault(); // Prevent the default form submission
        const formState = event.target;
        setRequestType("get_recommended");
        setMakeRequest(!makeRequest);
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
            <HomeItemLayout items={dataStream} />

        </header>
    );

}

export default Home;