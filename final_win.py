from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QHBoxLayout, QVBoxLayout, QPushButton,
    QGroupBox, QRadioButton, QListWidget, QLineEdit
)

import instr

class FinalWin(QWidget):
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
        self.layout = QVBoxLayout()
        self.index = QLabel("Индекс Руфье:")
        self.layout.addWidget(self.index)
        self.efficiency = QLabel("Работоспособность сердца:")
        self.layout.addWidget(self.efficiency)
        self.setLayout(self.layout)

    def connects(self):
        pass

    


        
