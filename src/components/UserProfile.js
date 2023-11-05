import styles from "./profile.module.css";
import ItemLayout from "./ItemLayout";
import { React, useState, useEffect, useRef } from "react";
import axios from 'axios';

function UserProfile() {

    const [makeRequest, setMakeRequest] = useState(false);
    const [rqCount, setRqCount] = useState(0);

    const [name, setName] = useState("");
    const [location, setLocation] = useState("");
    const [email, setEmail] = useState("");
    const [joinedDate, setJoinedDate] = useState("");
    const [fi, setfi] = useState("");
    const [li, setli] = useState("");
    const [itemList, setItemList] = useState([]);
    const [loaded, setLoaded] = useState(false);

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
        if (!data[0] && rqCount < 2) {
            setMakeRequest(!makeRequest);
            setRqCount(rqCount + 1);
        } else {
            if(!data[0]){window.location.href = "/";}
            const ns = data[0][3].split(' ');
            console.log(ns)
            const nsplit = data[0][8].split(' ');
            setName(data[0][3]);
            setEmail(data[0][1]);
            setLocation(data[0][7]);
            setJoinedDate(nsplit[1] + " " + nsplit[2] + " " + nsplit[3]);
            setItemList(data.slice(1))

            setfi(ns[0][0]);
            setli(ns[1][0]);
            setLoaded(true);
        }
    }
    window.onload = function () { handleEmptyUser(); };

    useEffect(() => {
        axios
            .get(`http://100.66.68.63:8080/get_useritems?query=${username}`)
            .then((response) => {
                checkValidity(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    }, [makeRequest]);// On change of mkrq. 

    return (
        <div className={styles.header1}>

            <div style={{ marginTop:"10vh",width: "100%", display: "flex", justifyContent: "center", columnGap: "100px" }}>

                <div style={{ display: "flex", flexDirection: "column", rowGap: "20px", justifyContent: "center" }}>
                    <div className={styles.profile_pic}>
                        <div style={{ width: "100%", display: "flex", alignContent: 'center', justifyContent: 'center', marginTop: "40px", fontWeight: "bold", fontSize: "100px" }}>{fi}{li}</div>
                    </div>
                    <div className={styles.profile_edit}>
                        <a href="/" className={styles.link}>edit listings</a>
                    </div>
                </div>
                <div className={styles.profile_info}>

                    <p><a style={{fontWeight:"bold"}}>Name:</a> {name}</p>
                    <p><a style={{fontWeight:"bold"}}>Email:</a> {email}</p>
                    <p><a style={{fontWeight:"bold"}}>Location:</a> {location}</p>
                    <p>Joined on {joinedDate}</p>

                </div>



            </div>

            <ItemLayout items={itemList} />

        </div>

    );
}

export default UserProfile;