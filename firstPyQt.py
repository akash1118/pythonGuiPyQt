import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
dlgMain = QDialog()
dlgMain.setWindowTitle("Akash's GUI")
dlgMain.show()

app.exec_()