# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:45:37 2021

@author: LiNaK
"""

# Standard module
import sys

# 3rd party's module
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# Original module  

button = QPushButton('Press Me')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My App')
        button = QPushButton('Press Me')
        
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.Qt import PYQT_VERSION_STR

print(QT_VERSION_STR)
print(PYQT_VERSION_STR)

app.exec_()
