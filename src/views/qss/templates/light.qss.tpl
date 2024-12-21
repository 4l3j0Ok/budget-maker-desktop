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

QPushButton#btnDelete {
    background-color: ${delete};
    color: white;
}

QPushButton#btnDelete:pressed {
    background-color: ${delete_alt};
    color: white;
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
    border: 0.5px solid;
    border-color: grey;
    border-radius: 5px;
    padding: 5px;
    color: ${text};
    background-color: white;
}

QLineEdit:focus {
    border-color: ${accent};
}
