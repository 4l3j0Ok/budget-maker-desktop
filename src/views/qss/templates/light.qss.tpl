* {
    background-color: #f0f0f0;
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

QFrame#frNavbar > QPushButton {
    background-color: none;
    color: ${button_text};
}

QFrame#frNavbar > QPushButton:hover {
    background-color: ${accent};
    color: ${button_text_alt};
}

QLineEdit {
    border: 1px solid;
    border-radius: 5px;
    padding: 5px;
    color: ${text};
}

QLineEdit:focus {
    border-color: ${accent};
}