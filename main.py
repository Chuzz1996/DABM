from Inicio import *
from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
main()
