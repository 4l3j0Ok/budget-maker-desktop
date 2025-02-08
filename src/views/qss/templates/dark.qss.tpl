* {
    background-color: #2c2c2c;
    color: ${text};
}

QPushButton {
    border: none;
    border-radius: 5px;
    padding: 5px;
    background-color: ${accent};
    color: ${button_text_alt};
}

QPushButton:pressed {
    background-color: ${accent_alt};
}

/* Eliminar el degradado de los botones: */
QFrame#frNavbar > QPushButton {
    background-color: none;
    color: ${button_text};
}

QFrame#frNavbar > QPushButton:hover {
    background-color: ${accent};
    color: ${button_text_alt};
}

QLineEdit {
    border: 0.5px solid;
    border-color: grey;
    border-radius: 5px;
    padding: 5px;
    color: ${text};
    background-color: #3c3c3c;
}

QWebEngineView {
    border: 0.5px solid;
    border-color: grey;
    border-radius: 5px;
    padding: 5px;
    background-color: #3c3c3c;
}

QLineEdit:focus {
    border-color: ${accent};
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
}