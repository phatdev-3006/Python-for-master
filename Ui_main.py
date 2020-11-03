from main import Ui_Ui_main
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QTimer
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_Ui_main()
		self.ui.setupUi(self)
		self.ui.setWindowFlags(Qt.FramelessWindowHint)
		self.ui.setAttribute(Qt.WA_TranslucentBackground)




		self.show()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())