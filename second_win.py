from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QHBoxLayout, QVBoxLayout, QPushButton,
    QGroupBox, QRadioButton, QListWidget, QLineEdit
)

import instr
from final_win import FinalWin

class TestWin(QWidget):
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
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.name_txt = QLabel(instr.label_1)
        self.l_line.addWidget(self.name_txt, alignment=Qt.AlignLeft)
        self.name_line = QLineEdit("Ф.И.О")
        self.l_line.addWidget(self.name_line, alignment=Qt.AlignLeft)
        self.age_txt = QLabel(instr.label_2)
        self.l_line.addWidget(self.age_txt, alignment=Qt.AlignLeft)
        self.age_line = QLineEdit("0")
        self.l_line.addWidget(self.age_line, alignment=Qt.AlignLeft)
        self.ex1_txt = QLabel(instr.label_3)
        self.l_line.addWidget(self.ex1_txt, alignment=Qt.AlignLeft)
        self.start_button = QPushButton("Начать первый тест")
        self.l_line.addWidget(self.start_button, alignment=Qt.AlignLeft)
        self.result1 = QLineEdit("0")
        self.l_line.addWidget(self.result1, alignment=Qt.AlignLeft)
        self.ex2_txt = QLabel(instr.label_4)
        self.l_line.addWidget(self.ex2_txt, alignment=Qt.AlignLeft)
        self.start_squads_button = QPushButton("Начать делать приседания")
        self.l_line.addWidget(self.start_squads_button, alignment=Qt.AlignLeft)
        self.ex3_txt = QLabel(instr.label_5)
        self.l_line.addWidget(self.ex3_txt, alignment=Qt.AlignLeft)
        self.start_final_ex = QPushButton("Начать финальный тест")
        self.l_line.addWidget(self.start_final_ex, alignment=Qt.AlignLeft)
        self.result2 = QLineEdit("0")
        self.l_line.addWidget(self.result2, alignment=Qt.AlignLeft)
        self.result3 = QLineEdit("0")
        self.l_line.addWidget(self.result3, alignment=Qt.AlignLeft)
        self.send_results = QPushButton("Отправить результаты")
        self.l_line.addWidget(self.send_results, alignment=Qt.AlignCenter)
        self.timer = QLabel("00:00:15")
        self.r_line.addWidget(self.timer, alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.send_results.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = FinalWin()




        
