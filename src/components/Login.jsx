import '../css/Login.css'
import Logo from '../assets/logo_final.png'

function Login () {
    return (
        <div className="login-content">
            <div className="about-container">
                <div className="logo-login">
                    <img className='singly-logo-login' src={Logo}/> 
                </div>
                <div className="text-login">
                    Signly otwiera przed Tobą nowe 
                    <br />
                    możliwości, burzy bariery. 
                    <br />
                    Signly - łączymy ludzi
                </div>
            </div>
            <div>
                <div className="login-form">
                    <input className='input-box' type="email" placeholder='Adres email'/>
                    <input className='input-box' type="password" placeholder='Hasło'/>
                    <button className='login-button'>Zaloguj się</button>
                    <a href='https://youtu.be/dQw4w9WgXcQ' className='login-link'>Nie pamiętasz hasła?</a>
                    <button className='register-button'>Nowe konto</button>
                </div>
            </div>
        </div>
    )
}

export default Login;