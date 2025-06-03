import signlyLogo from '../assets/logo_final.png'
import '../css/AboutProject.css'

function AboutProject() {
    return (
        <div className='about-project'>
            <div className='text-container'>
                <div className='title'>
                    O projekcie
                </div>
                <div className='content'>
                    Signly - system nauki języka migowego, opracowany przez studentów informatyki na wydziale Elektrotechniki, Elektroniki, Informatyki i Automatyki Politechniki Łodzkiej w ramach projektu kompetencyjnego
                </div>
            </div>
            <div className='img-container'>
                <img className='logo' src={signlyLogo}/>
            </div>
        </div>
    )
}

export default AboutProject;