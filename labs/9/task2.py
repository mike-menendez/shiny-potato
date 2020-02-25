'''
Authors: Cassandra Cabrera & Mike Menendez
Date: February 26, 2020
Purpose: Task 2 of Lab 9
	- Create a GUI label with the teams name on it
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.label1 = QLabel('Cassandra Cabrera', self)
		self.label2 = QLabel('Mike Menenendez', self)
		vbox = QVBoxLayout()
		vbox.addWidget(self.label1)
		vbox.addWidget(self.label2)
		self.setLayout(vbox)
		self.setGeometry(100,100,600,400)
		self.show()

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())