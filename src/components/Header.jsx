import SmallButton from "./SmallButton";

function Header() {
    const styles = {
        backgroundColor: 'hsla(216, 18%, 16%, 0.8)',
        display: 'flex', 
        justifyContent: 'flex-end',
        position: 'fixed',
        zIndex: '999',
        width: '100%',
        height: '5.5rem',
    }

    const handleRegisterClick = () => {
        console.log("Register button clicked");
    };

    const handleLoginClick = () => {
        console.log("Login button clicked");
    };

    return (
        <div style={styles}>
            <SmallButton label='Zarejestruj się' color='#00ADB5' onClick={handleRegisterClick}/>
            <SmallButton label='Zaloguj się' color='#EAC435' onClick={handleLoginClick}/>
        </div>
    )
}

export default Header;