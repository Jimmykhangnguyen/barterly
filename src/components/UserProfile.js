import styles from "./profile.module.css";
import React from "react";
import profileImage from './profile_pic/profile1.jpg'; // Import the image file


function UserProfile() {
    return (
        <header className="App-header">
            <div className={styles.profile_header}>
                <p className={styles.profile_text}>My profile.</p>
            </div>

            <div>
                <a href="/SignUp" className={styles.linkToTrade}>items for trade</a>
            </div>

            <div className={styles.profile_info}>
                <ul><p>Name: Thomas Yonge</p></ul>
                <ul><p>Email: thomas@gmail.com</p></ul>
                <ul><p>Location: Toronto</p></ul>
                <ul><p>Privacy setting: Private</p></ul>
                <ul><p>Joined on 20/6/2023</p></ul>
            </div>

            <div className={styles.profile_pic}>
                <img src={profileImage} alt="My profile picture" />
            </div>

            <div className={styles.profile_edit}>
                <a href="/SignUp" className={styles.profile_edit_text}>edit profile</a>
            </div>
        </header>
    );
}

export default UserProfile;