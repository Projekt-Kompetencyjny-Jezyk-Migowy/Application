import Logo from '../assets/logo_final.png'
import '../css/Register.css'

function Register() {
    return (
        <div className='register-page-content'>
            <div className='register-logo-wrapper'>
                <img src={Logo} alt="Signly" className='register-logo'/>
            </div>
            <div className='register-form'>
                <div className='register-double-wrapper'>
                    <div className='register-small-container'>
                        <input type="text" name="fname" id="fname" placeholder='Imię' className='register-text-input'/>
                    </div>
                    <div className='register-small-container'>
                        <input type="text" name="lname" id="lname" placeholder='Nazwisko' className='register-text-input'/>
                    </div>
                </div>
                <div className='register-detail-wrapper'>
                    <div className='register-small-container'>
                        <div className='register-text'>Data urodzenia</div>
                        <input type="date" className='register-date-input'/>
                    </div>
                    <div className='register-small-container'>
                        <div className='register-text'>Płeć</div>
                        <select id="sex" name="sex" className='register-date-input'>
                            <option value="NotSelected" selected disabled>Wybierz płeć</option>
                            <option value="Female">Kobieta</option>
                            <option value="Male">Mężczyzna</option>
                            <option value="Other">Inne</option>
                            <option value="Unknown ">Wolę nie podawać</option>
                        </select>
                    </div>
                </div>
                <div className='register-account-data-container'>
                    <input type="email" className='register-big-container' placeholder='Adres email'/>
                    <input type="password" className='register-big-container' placeholder='Hasło'/>
                    <input type="password" className='register-big-container' placeholder='Powtórz hasło'/>
                </div>
                <div className='register-accept-button-wrapper'>
                    <button className='register-accept-button'>Zarejestruj się</button>
                </div>
                <div className='register-login-wrapper'>
                    <a href='https://youtu.be/qQvIAs-nPSo' className='register-login-link'>Masz już konto?</a>
                </div>
            </div>
        </div>
    )
}

export default Register