'''
Authors: Cassandra Cabrera & Mike Menendez
Date: February 26, 2020
Purpose: Task 3 of Lab 9
	- Create a GUI image with the image of choice using pyqt5
Code adapted from Avner's GitHub Gist
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

my_qt_app = QApplication(sys.argv)

# our window object
my_window = QWidget()

my_window.setWindowTitle('TURTLE!!!!')

# create a label (our image will go in here)
picture_label = QLabel(my_window)

# create a QPixmap object
my_image = QPixmap('/Users/casscabrera/Desktop/CST205/download.jpeg')

# put QPixmap object in QLabel
picture_label.setPixmap(my_image)

# resize the window to the size of the image
my_window.resize(my_image.width(),my_image.height())


my_window.show()

sys.exit(my_qt_app.exec_())