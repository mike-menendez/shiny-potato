'''
Authors: Cassandra Cabrera & Mike Menendez
Date: March 2, 2020
Purpose: Task 1 & 2 of Lab 10
	- Create a dropdown of colors
	- create button that when clicked will display chosen color
'''

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox)
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon

#defines my rgb values
my_rgb_dict = {"Pick a color" : "", "red" : (255,0,0), "orange" : (255,127,0), 
"yellow" : (255,255,0), "green" : (0,255,0), "blue" : (0,0,255), 
"purple" : (75,0,130), "lilac" : (143,0,255)}

#defines my hex values
my_hex_dict = {"Pick a color" : "", "red" : "#FF0000", "orange" : "#FF7F00", 
"yellow" : "#FFFF00", "green" : "#FFFF00", "blue" : "#0000FF", 
"purple" : "#4B0082)", "lilac" : "#8F00FF"}

#sets up the window for the selected color to be displayed
class Color(QWidget):
	def __init__(self, color):
		super().__init__()
		self.title = 'Your Color Selection!'
		self.left = 10
		self.top = 10
		self.width = 440
		self.height = 280
		self.color = color
		self.initUI()

	def initUI(self):
		super().__init__()
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		# Set window background color
		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), 
			QColor(self.color[0],self.color[1],self.color[2]))
		self.setPalette(p)

		self.show()

#sets up the main window
class Window(QWidget):
    def __init__(self):
        super().__init__()

        #creates the dropdown list
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(my_rgb_dict)
        self.my_title = QLabel("CST 205 Color Changer.")
        self.my_rgb = QLabel("RGB: ")
        self.my_hex = QLabel("Hex: ")
        self.my_btn = QPushButton("Display",self)

        self.my_btn.clicked.connect(self.on_click)

        tbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addWidget(self.my_rgb)
        hbox.addWidget(self.my_hex)

        vbox.addWidget(self.my_title)
        vbox.addWidget(self.my_combo_box)
        vbox.addWidget(self.my_btn)

        tbox.addLayout(vbox)
        tbox.addLayout(hbox)

        self.setLayout(tbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)
        self.setWindowTitle("Color Picker!")

    #sets the text based on color
    @pyqtSlot()
    def update_ui(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        self.my_rgb.setText(f'RGB: {my_rgb_dict[my_text]}.')
        self.my_hex.setText(f'Hex: {my_hex_dict[my_text]}.')

    #the on click listener for the button 
    @pyqtSlot()
    def on_click(self):
    	i = self.my_combo_box.currentText()
    	if i != "Pick a color":
    		self.color = Color(my_rgb_dict[i])
    		self.color.show()


app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())