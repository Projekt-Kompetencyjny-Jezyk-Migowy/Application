import styles from './Header.module.css'
import SmallButton from '../SmallButton';

function Header() {
    const handleRegisterClick = () => {
        console.log("Register button clicked");
    };

    const handleLoginClick = () => {
        console.log("Login button clicked");
    };

    return ( 
        <div className={styles.header}>
            <SmallButton label="Register" color='red' onClick={() => handleRegisterClick()} />
            <SmallButton label="Login"  color='blue'  onClick={() => handleLoginClick()} />
        </div>
    )   
}

export default Header;