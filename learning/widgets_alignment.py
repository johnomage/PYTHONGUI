from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox


def set_alignment(align: str):
    alignment_texts = [
        "left",
        "right",
        "top",
        "bottom",
        "center",
        "center top", "center_top", "center-top",
        "center bottom", "center_bottom", "center-bottom",
        "top left", "top_left", "topleft",
        "top right", "top_right", "topright",
        "bottom left", "bottom_left", "bottomleft",
        "bottom right", "bottom_right", "bottomright",
        ]

    match align.lower():
        case "right":
            return Qt.AlignmentFlag.AlignRight
        case 'left': return Qt.AlignmentFlag.AlignLeft
        case 'top': return Qt.AlignmentFlag.AlignTop
        case 'bottom': return Qt.AlignmentFlag.AlignBottom
        case 'center': return Qt.AlignmentFlag.AlignCenter
        case 'center top' | 'center_top' | 'center-top': return Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter
        case 'center bottom' | 'center_bottom' | 'center-bottom': return Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter
        case 'top left' | 'topleft' | 'top_left': return Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        case 'top right'| 'topright' | 'top_right': return Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight
        case 'bottom left' | 'bottomleft' | 'bottom_left': return Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft
        case 'bottom right' | 'bottomright' | 'bottom_right': return Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight
        case _:
            message = QMessageBox()
            message.setText(f'Align parameter must be one of:\n{alignment_texts}')
            message.exec()
            return 0