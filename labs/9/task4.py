'''
Authors: Cassandra Cabrera & Mike Menendez
Date: February 26, 2020
Purpose: Task 4 of Lab 9
	- Create a GUI label with the buttons that send signals and update the labels
Code builds off our code from Task 2 of Lab 9
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import pyqtSlot 

class Buttons(QWidget):
	def __init__(self):
		super().__init__()
		vbox = QVBoxLayout()
		self.btn1 = QPushButton("Button 1", self)
		self.btn2 = QPushButton("Button 2", self)
		self.label = QLabel("Button Not Clicked")
		self.btn1.clicked.connect(self.on_click1)
		self.btn2.clicked.connect(self.on_click2)
		vbox.addWidget(self.btn1)
		vbox.addWidget(self.btn2)
		vbox.addWidget(self.label)

		self.setLayout(vbox)

	@pyqtSlot()
	def on_click1(self):
		self.label.setText('Button 1 clicked') 

	@pyqtSlot()
	def on_click2(self):
		self.label.setText('Button 2 clicked') 


app = QApplication(sys.argv)
click = Buttons()
click.show()

sys.exit(app.exec_())