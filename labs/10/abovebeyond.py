'''
Authors: Cassandra Cabrera & Mike Menendez
Date: March 2, 2020
Purpose: Bonus Task of Lab 10
    - Create a color picker widget
    - When selected display color with RGB and hex values
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor

class DisplayColor(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'CST205: The color you selected!'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        color = QColorDialog.getColor()

        if color.isValid():
            self.initColor(color)
    
        self.show()

    def initColor(self,color):
        super().__init__()
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.color = color

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), 
            QColor(self.color))
        self.setPalette(p)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DisplayColor()
    sys.exit(app.exec_())