# import sys
# from PySide6.QtGui import *
# from PySide6.QtCore import *
# from PySide6.QtWidgets import *
# from UiForm_2 import Ui_MainWindow

# class MainWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self, None)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

#         self.ui.pb_home.clicked.connect(self.changePage)
#         self.ui.pb_input.clicked.connect(self.changePage)
#         self.ui.pb_history.clicked.connect(self.changePage)

#     def changePage(self):
#         sender = self.sender().objectName()
#         if(sender == 'pb_home'):
#             self.ui.stackedWidget.setCurrentIndex(0)
#         elif(sender == 'pb_input'):
#             self.ui.stackedWidget.setCurrentIndex(1)
#         elif(sender == 'pb_history'):
#             self.ui.stackedWidget.setCurrentIndex(2)        

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = MainWindow()
#     w.show()
#     sys.exit(app.exec_())