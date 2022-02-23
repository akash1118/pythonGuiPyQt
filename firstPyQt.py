import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
dlgMain = QMainWindow()
dlgMain.setWindowTitle("Akash's GUI")
dlgMain.show()

sys.exit(app.exec_())