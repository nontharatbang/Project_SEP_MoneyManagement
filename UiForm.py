# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UiForm.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 850)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 401, 751))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.verticalLayoutWidget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayoutWidget = QWidget(self.page_1)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 30, 401, 101))
        self.p1_vBoxLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.p1_vBoxLayout.setObjectName(u"p1_vBoxLayout")
        self.p1_vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.label_savingBalance = QLabel(self.verticalLayoutWidget)
        self.label_savingBalance.setObjectName(u"label_savingBalance")
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_savingBalance.setFont(font)
        self.label_savingBalance.setTextFormat(Qt.PlainText)

        self.p1_vBoxLayout.addWidget(self.label_savingBalance)

        self.p1_vBox_hBoxLayout = QHBoxLayout()
        self.p1_vBox_hBoxLayout.setObjectName(u"p1_vBox_hBoxLayout")
        self.label_currentIncome = QLabel(self.verticalLayoutWidget)
        self.label_currentIncome.setObjectName(u"label_currentIncome")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_currentIncome.setFont(font1)
        self.label_currentIncome.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.p1_vBox_hBoxLayout.addWidget(self.label_currentIncome)

        self.label_currentExpense = QLabel(self.verticalLayoutWidget)
        self.label_currentExpense.setObjectName(u"label_currentExpense")
        self.label_currentExpense.setFont(font1)
        self.label_currentExpense.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.p1_vBox_hBoxLayout.addWidget(self.label_currentExpense)


        self.p1_vBoxLayout.addLayout(self.p1_vBox_hBoxLayout)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayoutWidget_2 = QWidget(self.page_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 401, 541))
        self.p2_vBoxLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.p2_vBoxLayout.setObjectName(u"p2_vBoxLayout")
        self.p2_vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.label_transaction = QLabel(self.verticalLayoutWidget_2)
        self.label_transaction.setObjectName(u"label_transaction")
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.label_transaction.setFont(font2)
        self.label_transaction.setAlignment(Qt.AlignCenter)

        self.p2_vBoxLayout.addWidget(self.label_transaction)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_expense = QPushButton(self.verticalLayoutWidget_2)
        self.pb_expense.setObjectName(u"pb_expense")

        self.horizontalLayout.addWidget(self.pb_expense)

        self.pb_income = QPushButton(self.verticalLayoutWidget_2)
        self.pb_income.setObjectName(u"pb_income")

        self.horizontalLayout.addWidget(self.pb_income)


        self.p2_vBoxLayout.addLayout(self.horizontalLayout)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_6.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_6.addWidget(self.lineEdit_2, 1, 1, 1, 1)


        self.p2_vBoxLayout.addLayout(self.gridLayout_6)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.p2_vBoxLayout.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit.setObjectName(u"textEdit")

        self.p2_vBoxLayout.addWidget(self.textEdit)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 750, 401, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pb_home = QPushButton(self.horizontalLayoutWidget)
        self.pb_home.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.pb_input = QPushButton(self.horizontalLayoutWidget)
        self.pb_input.setObjectName(u"pb_input")

        self.horizontalLayout_6.addWidget(self.pb_input)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Money Management", None))
        self.label_savingBalance.setText(QCoreApplication.translate("MainWindow", u"Saving Balance: \u0e3f", None))
        self.label_currentIncome.setText(QCoreApplication.translate("MainWindow", u"Income:", None))
        self.label_currentExpense.setText(QCoreApplication.translate("MainWindow", u"Expense:", None))
        self.label_transaction.setText(QCoreApplication.translate("MainWindow", u"Transaction", None))
        self.pb_expense.setText(QCoreApplication.translate("MainWindow", u"Expense", None))
        self.pb_income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Memo", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pb_input.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
    # retranslateUi



