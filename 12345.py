from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import *
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QTimer, QPointF, Qt
import math



class Ui_Win1(object):
    def setupUi(self, Win1):
        Win1.setObjectName("Win1")
        Win1.resize(450, 800)
        self.widgetWin1 = QtWidgets.QWidget(Win1)
        self.widgetWin1.setObjectName("widgetWin1")



        self.text1 = QtWidgets.QLabel(self.widgetWin1)
        self.text1.setGeometry(QtCore.QRect(197, 378, 56, 16))
        self.text1.setObjectName("text1")

        Win1.setCentralWidget(self.widgetWin1)
        self.retranslateUi(Win1)
        QtCore.QMetaObject.connectSlotsByName(Win1)

    def retranslateUi(self, Win1):
        _translate = QtCore.QCoreApplication.translate
        Win1.setWindowTitle(_translate("Win1", "MainWindow"))
        self.text1.setText(_translate("Win1", " "))





class Ui_Win2(object):
    def setupUi(self, Win2):
        Win2.setObjectName("Win2")
        Win2.resize(450, 800)
        self.widgetWin2 = QtWidgets.QWidget(Win2)
        self.widgetWin2.setObjectName("widgetWin2")
        self.text2 = QtWidgets.QLabel(self.widgetWin2)
        self.text2.setGeometry(QtCore.QRect(197, 378, 56, 16))
        self.text2.setObjectName("text2")

        from PIL import Image
        #myImage = Image.open("eye.png")
        #myImage.show()


        Win2.setCentralWidget(self.widgetWin2)
        self.retranslateUi(Win2)
        QtCore.QMetaObject.connectSlotsByName(Win2)

    def retranslateUi(self, Win2):
        _translate = QtCore.QCoreApplication.translate
        Win2.setWindowTitle(_translate("Win2", "MainWindow"))
        self.text2.setText(_translate("Win2", "Win2"))


class Ui_Win3(object):
    def setupUi(self, Win3):
        Win3.setObjectName("Win3")
        Win3.resize(450, 800)
        self.widgetWin3 = QtWidgets.QWidget(Win3)
        self.widgetWin3.setObjectName("widgetWin3")
        self.text3 = QtWidgets.QLabel(self.widgetWin3)
        self.text3.setGeometry(QtCore.QRect(197, 378, 56, 16))
        self.text3.setObjectName("text3")

        Win3.setCentralWidget(self.widgetWin3)

        self.retranslateUi(Win3)
        QtCore.QMetaObject.connectSlotsByName(Win3)

    def retranslateUi(self, Win3):
        _translate = QtCore.QCoreApplication.translate
        Win3.setWindowTitle(_translate("Win3", "MainWindow"))
        self.text3.setText(_translate("Win3", "Win3"))

class Ui_Win4(object):
    def setupUi(self, Win4):
        Win4.setObjectName("Win4")
        Win4.resize(450, 800)
        self.widgetWin4 = QtWidgets.QWidget(Win4)
        self.widgetWin4.setObjectName("widgetWin4")

        self.text4 = QtWidgets.QLabel(self.widgetWin4)
        self.text4.setGeometry(QtCore.QRect(197, 378, 56, 16))
        self.text4.setObjectName("text1")

        Win4.setCentralWidget(self.widgetWin4)
        self.retranslateUi(Win4)
        QtCore.QMetaObject.connectSlotsByName(Win4)

    def retranslateUi(self, Win4):
        _translate = QtCore.QCoreApplication.translate
        Win4.setWindowTitle(_translate("Win4", "MainWindow"))
        self.text4.setText(_translate("Win4", "Win4"))

class Ui_Win5(object):
    def setupUi(self, Win5):
        Win5.setObjectName("Win5")
        Win5.resize(450, 800)
        self.widgetWin5 = QtWidgets.QWidget(Win5)
        self.widgetWin5.setObjectName("widgetWin5")
        self.text5 = QtWidgets.QLabel(self.widgetWin5)
        self.text5.setGeometry(QtCore.QRect(197, 378, 56, 16))
        self.text5.setObjectName("text5")

        Win5.setCentralWidget(self.widgetWin5)
        self.retranslateUi(Win5)
        QtCore.QMetaObject.connectSlotsByName(Win5)

    def retranslateUi(self, Win5):
        _translate = QtCore.QCoreApplication.translate
        Win5.setWindowTitle(_translate("Win5", "MainWindow"))
        self.text5.setText(_translate("Win5", "Win5"))

class Ui_Win6(object):
    def setupUi(self, Win6):
        Win6.setObjectName("Win6")
        Win6.resize(450, 800)
        self.widgetWin6 = QtWidgets.QWidget(Win6)
        self.widgetWin6.setObjectName("widgetWin6")
        self.text6 = QtWidgets.QLabel(self.widgetWin6)
        self.text6.setGeometry(QtCore.QRect(197, 378, 56, 16))
        self.text6.setObjectName("text6")

        Win6.setCentralWidget(self.widgetWin6)

        self.retranslateUi(Win6)
        QtCore.QMetaObject.connectSlotsByName(Win6)

    def retranslateUi(self, Win6):
        _translate = QtCore.QCoreApplication.translate
        Win6.setWindowTitle(_translate("Win6", "MainWindow"))
        self.text6.setText(_translate("Win6", "Win6"))


class Win1(QtWidgets.QMainWindow, Ui_Win1):
    def __init__(self, parent=None):
        super(Win1, self).__init__(parent)
        self.setupUi(self)




class Win2(QtWidgets.QMainWindow, Ui_Win2):
    def __init__(self, parent=None):
        super(Win2, self).__init__(parent)
        self.setupUi(self)


class Win3(QtWidgets.QMainWindow, Ui_Win3):
    def __init__(self, parent=None):
        super(Win3, self).__init__(parent)
        self.setupUi(self)

class Win4(QtWidgets.QMainWindow, Ui_Win4):
    def __init__(self, parent=None):
        super(Win4, self).__init__(parent)
        self.setupUi(self)

class Win5(QtWidgets.QMainWindow, Ui_Win5):
    def __init__(self, parent=None):
        super(Win5, self).__init__(parent)
        self.setupUi(self)

class Win6(QtWidgets.QMainWindow, Ui_Win6):
    def __init__(self, parent=None):
        super(Win6, self).__init__(parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.i = 2

        self.stacked = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked)

        self.window_Win1 = Win1(self)
        self.window_Win1.setStyleSheet('#Win1 {background-color: #ffbdcc;}')
        self.window_Win2 = Win2(self)
        self.window_Win2.setStyleSheet('#Win2 {background-color: #ccffbd;}')
        self.window_Win3 = Win3(self)
        self.window_Win3.setStyleSheet('#Win3 {background-color: #bdccccff;}')
        self.window_Win4 = Win4(self)
        self.window_Win4.setStyleSheet('#Win4 {background-color: #ffbdcc;}')
        self.window_Win5 = Win5(self)
        self.window_Win5.setStyleSheet('#Win5 {background-color: #ccffbd;}')
        self.window_Win6 = Win6(self)
        self.window_Win6.setStyleSheet('#Win6 {background-color: #bdccccff;}')

        self.stacked.addWidget(self.window_Win1)
        self.stacked.addWidget(self.window_Win2)
        self.stacked.addWidget(self.window_Win3)
        self.stacked.addWidget(self.window_Win4)
        self.stacked.addWidget(self.window_Win5)
        self.stacked.addWidget(self.window_Win6)


        self.create_buttonsWin1(self.window_Win1)


    def create_buttonsWin1(self, parent):
        bnt_2 = QtWidgets.QPushButton("Следующее упражнение", parent)
        #        self.bnt_2.setGeometry(QtCore.QRect(150, 772, 150, 28))
        bnt_2.setGeometry(QtCore.QRect(150, 572, 150, 28))
        bnt_2.clicked.connect(self.go_win)
        bnt_2.show()



    def create_buttonsWin2(self, parent):
        bnt_3 = QtWidgets.QPushButton("Следующее упражнение", parent)
        #        self.bnt_2.setGeometry(QtCore.QRect(150, 772, 150, 28))

        bnt_3.setGeometry(QtCore.QRect(150, 572, 150, 28))
        bnt_3.clicked.connect(self.go_win)
        bnt_3.show()

    def create_buttonsWin3(self, parent):
        bnt_4 = QtWidgets.QPushButton("Следующее упражнение", parent)
        #        self.bnt_2.setGeometry(QtCore.QRect(150, 772, 150, 28))
        bnt_4.setGeometry(QtCore.QRect(150, 572, 150, 28))
        bnt_4.clicked.connect(self.go_win)
        bnt_4.show()

    def create_buttonsWin4(self, parent):
        bnt_5 = QtWidgets.QPushButton("Следующее упражнение", parent)
        #        self.bnt_2.setGeometry(QtCore.QRect(150, 772, 150, 28))
        bnt_5.setGeometry(QtCore.QRect(150, 572, 150, 28))
        bnt_5.clicked.connect(self.go_win)
        bnt_5.show()

    def create_buttonsWin5(self, parent):
        bnt_6 = QtWidgets.QPushButton("Следующее упражнение", parent)
        #        self.bnt_2.setGeometry(QtCore.QRect(150, 772, 150, 28))
        bnt_6.setGeometry(QtCore.QRect(150, 572, 150, 28))
        bnt_6.clicked.connect(self.go_win)
        bnt_6.show()

    def create_buttonsWin6(self, parent):
        bnt_7 = QtWidgets.QPushButton("Следующее упражнение", parent)
        #        self.bnt_2.setGeometry(QtCore.QRect(150, 772, 150, 28))
        bnt_7.setGeometry(QtCore.QRect(150, 572, 150, 28))
        bnt_7.clicked.connect(self.go_win)
        bnt_7.show()

    def go_win(self, i):
        if self.i == 1:
            self.stacked.setCurrentIndex(0)
            self.create_buttonsWin1(self.window_Win1)
            self.i += 1
            

        elif self.i == 2:
            self.stacked.setCurrentIndex(1)
            self.create_buttonsWin2(self.window_Win2)
            self.i += 1

        elif self.i == 3:
            self.stacked.setCurrentIndex(2)
            self.create_buttonsWin3(self.window_Win3)
            self.i += 1
        elif self.i == 4:
            self.stacked.setCurrentIndex(3)
            self.create_buttonsWin4(self.window_Win4)
            self.i += 1

        elif self.i == 5:
            self.stacked.setCurrentIndex(4)
            self.create_buttonsWin5(self.window_Win5)
            self.i += 1

        elif self.i == 6:
            self.stacked.setCurrentIndex(5)
            self.create_buttonsWin6(self.window_Win6)
            self.i += 1





if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.resize(450, 650)  # <---- (450, 800)
    window.show()
    sys.exit(app.exec())