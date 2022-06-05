from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QHBoxLayout, QVBoxLayout, QPushButton,
    QGroupBox, QRadioButton, QListWidget, QLineEdit
)

import instr

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.set_appear()
        self.exp = exp
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(instr.txt_title)
        self.resize(instr.win_width, instr.win_height)
        self.move(instr.win_x, instr.win_y)
    
    def initUI(self):
        self.layout = QVBoxLayout()
        self.efficiency = QLabel("Работоспособность сердца:"+ self.results())
        self.index_txt = QLabel("Индекс Руфье:" + str(self.index))
        self.layout.addWidget(self.index_txt)
        self.layout.addWidget(self.efficiency)
        self.setLayout(self.layout)

    def connects(self):
        pass

    def results(self):
        if self.exp.age < 7:
            self.index = 0
            return "Нет данных для такого возраста."
        self.index = (4*(self.exp.test_1+self.exp.test_2+self.exp.test_3)-200)/10
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return instr.txt_res1
            elif self.index < 21 and self.index >= 17:
                return instr.txt_res2
            elif self.index < 17 and self.index >= 12:
                return instr.txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return instr.txt_res4
            else:
                return instr.txt_res5
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return instr.txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return instr.txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return instr.txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return instr.txt_res4
            else:
                return instr.txt_res5
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return instr.txt_res1
            elif self.index < 18 and self.index >= 14:
                return instr.txt_res2
            elif self.index < 14 and self.index >= 9:
                return instr.txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return instr.txt_res4
            else:
                return instr.txt_res5
        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5:
                return instr.txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return instr.txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return instr.txt_res3
            elif self.index < 7.2 and self.index >= 2:
                return instr.txt_res4
            else:
                return instr.txt_res5
        if self.exp.age >= 15:
            if self.index >= 15:
                return instr.txt_res1
            elif self.index < 15 and self.index >= 11:
                return instr.txt_res2
            elif self.index < 11 and self.index >= 6:
                return instr.txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return instr.txt_res4
            else:
                return instr.txt_res5
            
        

    


        
