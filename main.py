import sys

from PySide2 import QtWidgets

from app import mainwindow

app = QtWidgets.QApplication(sys.argv)
window = mainwindow.MainWindow()
window.show()

app.exec_()
