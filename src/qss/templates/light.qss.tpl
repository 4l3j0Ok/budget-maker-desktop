* {
    background-color: #f0f0f0;
    color: #000000;
}

/* Eliminar el degradado de los botones: */
QPushButton {
    border: 0px;
    border-radius: 5px;
    padding: 5px;
}

QFrame#frNavbar > QPushButton:hover {
    background-color: ${accent};
    color: ${button_hover};
}
