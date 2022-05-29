from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QHBoxLayout, QVBoxLayout, QPushButton,
    QGroupBox, QRadioButton, QListWidget, QLineEdit
)

import instr
from second_win import TestWin

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(instr.txt_title)
        self.resize(instr.win_width, instr.win_height)
        self.move(instr.win_x, instr.win_y)

    def initUI(self):
        self.hello_text = QLabel(instr.txt_hello)
        self.instruction = QLabel(instr.txt_instruction)
        self.button = QPushButton(instr.txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()


app = QApplication([])
mw = MainWin()
app.exec_()