import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from UiForm import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pb_home.clicked.connect(self.goToInput)
        self.ui.pb_input.clicked.connect(self.goToInput)

    def goToInput(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def goToHome(self):
        self.ui.stackedWidget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())