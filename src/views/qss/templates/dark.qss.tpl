* {
    background-color: #2c2c2c;
    color: #f0f0f0;
}

QPushButton {
    border: none;
    border-radius: 5px;
    padding: 5px;
    background-color: ${accent};
}

/* Eliminar el degradado de los botones: */
QFrame#frNavbar > QPushButton {
    background-color: none;
}

QFrame#frNavbar > QPushButton:hover {
    background-color: ${accent};
    color: ${button_text_alt};
}