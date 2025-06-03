import styles from './Header.module.css'
import SmallButton from '../SmallButton/SmallButton';

function Header() {
    const handleRegisterClick = () => {
        console.log("Register button clicked");
    };

    const handleLoginClick = () => {
        console.log("Login button clicked");
    };

    return ( 
        <div className={styles.header}>
            <div className={styles.buttonContainer}>
                <div className={styles.buttonWrapper}>
                    <SmallButton 
                        backgroundColor='#1E1825' 
                        color='#00ADB5' 
                        borderColor='#00ADB5' 
                        text='Zarejestruj się' 
                        onClick={() => handleLoginClick()}
                    />
                </div>
                <div className={styles.buttonWrapper}>
                    <SmallButton 
                        backgroundColor='#1E1825' 
                        color='#EAC435' 
                        borderColor='#EAC435' 
                        text='Zaloguj się' 
                        onClick={() => handleLoginClick()}
                    />
                </div>
            </div>
        </div>
    )   
}

export default Header;