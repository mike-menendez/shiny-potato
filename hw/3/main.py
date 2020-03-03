'''
Authors: Cassandra Cabrera & Mike Menendez
Date: March 9, 2020
Purpose: Homework 3 for CST205
	- ...
'''

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox)
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon

manipulations = ['please select','sepia','negative','grayscale','thumbnail','none']

# #sets up the window for the image from search to be displayed
# class ImageDisplay(QWidget):
# 	def __init__(self, color):
# 		super().__init__()
# 		


#sets up the main window
class Search(QWidget):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit()
        self.combo_box = QComboBox()
        self.combo_box.addItems(manipulations)
        self.btn = QPushButton("Search", self)
        self.title = QLabel("Find The Picture")
        self.search = QLabel("Enter Search Terms: ")
        self.change = QLabel("Select Image Manipulation: ")

        self.btn.clicked.connect(self.on_click)
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        hbox1.addWidget(self.search)
        hbox1.addWidget(self.line_edit)

        hbox2.addWidget(self.change)
        hbox2.addWidget(self.combo_box)

        vbox.addWidget(self.title)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)

        self.setWindowTitle("Image Search & Manipulation If You Want")

    #the on click listener for the button 
    @pyqtSlot()
    def on_click(self):
    	return


app = QApplication(sys.argv)
main = Search()
main.show()
sys.exit(app.exec_())