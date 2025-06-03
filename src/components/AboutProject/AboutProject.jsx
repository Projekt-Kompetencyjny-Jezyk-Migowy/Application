import signlyLogo from '../../assets/logo_final.png'
import styles from './AboutProject.module.css'

function AboutProject() {
    return (
        <div className={styles.mainContent}>
            <div className={styles.aboutContainer}>
                <div className={styles.titleWrapper}>
                    O projekcie
                </div>
                <div className={styles.textWrapper}>
                    Signly - system nauki języka migowego, opracowany przez studentów informatyki na wydziale Elektrotechniki, Elektroniki, Informatyki i Automatyki Politechniki Łodzkiej w ramach projektu kompetencyjnego
                </div>
            </div>
            <div className={styles.logoWrapper}>
                <img className={styles.logo} src={signlyLogo} />
            </div>
        </div>
    )
}

export default AboutProject;