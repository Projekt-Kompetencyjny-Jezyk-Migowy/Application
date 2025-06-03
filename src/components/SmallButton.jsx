function SmallButton (props) {
    const styles = {
        backgroundColor: '#222831',
        color: props.color,
        padding: '0.2rem 1.5rem',
        border: 'none',
        borderRadius: '0.5rem',
        margin: '1rem',
        marginTop: '1.5rem',
        marginBottom: '0.5rem',
        fontWeight: 'bold',
        fontSize: '1.2em',
        minWidth: '12rem',
        maxWidth: '14rem',
        boxShadow: `0 0 0.2rem 0.5rem ${props.color}`,
        cursor: 'pointer',
    }

    return (
        <button style={styles} onClick={props.onClick}>
            {props.label}
        </button>

    )
}

export default SmallButton;