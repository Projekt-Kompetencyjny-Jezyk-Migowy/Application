function SmallButton (props) {
    const inlineStyles = {
        backgroundColor: props.backgroundColor ? props.backgroundColor : 'none',
        color: props.color ? props.color : '#010102',
        border: props.borderColor ? `0.4rem solid ${props.borderColor}` : 'none',
        fontSize: props.fontSize ? props.fontSize : '1.2rem',
        borderRadius: '1rem',
        width: '100%',
        height: '100%',
        fontWeight: 'bold',
        cursor: 'pointer',
    }

    return (
        <button style={inlineStyles} onClick={props.onClick}>
            {props.text ? props.text : 'NO TEXT'}
        </button>
    )
}

export default SmallButton;