from config import Path


class Light:
    template_file = f"{Path.qss_tpls}/light.qss.tpl"
    background = "#eee"
    accent = "#4285F4"
    accent_alt = "#2d5ba7"
    selected = "#0c9100"
    selected_alt = "#085a00"
    text = "#333"
    deselected = "#9e9e9e"
    deselected_alt = "#7c7c7c"
    button_text = text
    button_text_alt = "#f0f0f0"
    delete = "#9b2424"
    delete_alt = "#631717"
    le_enabled = "#ffffff"
    le_disabled = background
    card_background = "white"
    card_border = "#e0e0e0"


class Dark:
    template_file = f"{Path.qss_tpls}/dark.qss.tpl"
    background = "#2c2c2c"
    accent = "#4285F4"
    accent_alt = "#2d5ba7"
    selected = "#0c9100"
    selected_alt = "#085a00"
    le_enabled = "#464646"
    le_disabled = background
    deselected = "#9e9e9e"
    deselected_alt = "#7c7c7c"
    text = "#ffffff"
    button_text = "#ffffff"
    button_text_alt = "#ffffff"
    delete = "#9b2424"
    delete_alt = "#631717"
    card_background = "#2c2c2c"
    card_border = "#3c3c3c"
