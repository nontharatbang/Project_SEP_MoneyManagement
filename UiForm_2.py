# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UiForm_2.ui'
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
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

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
        self.verticalLayoutWidget.setGeometry(QRect(0, 30, 401, 171))
        self.p1_vBoxLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.p1_vBoxLayout.setObjectName(u"p1_vBoxLayout")
        self.p1_vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_savingBalance = QLabel(self.verticalLayoutWidget)
        self.label_savingBalance.setObjectName(u"label_savingBalance")
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_savingBalance.setFont(font)
        self.label_savingBalance.setTextFormat(Qt.PlainText)
        self.label_savingBalance.setIndent(10)

        self.horizontalLayout_2.addWidget(self.label_savingBalance)

        self.label_balanceAmount = QLabel(self.verticalLayoutWidget)
        self.label_balanceAmount.setObjectName(u"label_balanceAmount")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(12)
        self.label_balanceAmount.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_balanceAmount)


        self.p1_vBoxLayout.addLayout(self.horizontalLayout_2)

        self.p1_vBox_hBoxLayout = QHBoxLayout()
        self.p1_vBox_hBoxLayout.setObjectName(u"p1_vBox_hBoxLayout")
        self.label_currentIncome = QLabel(self.verticalLayoutWidget)
        self.label_currentIncome.setObjectName(u"label_currentIncome")
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_currentIncome.setFont(font2)
        self.label_currentIncome.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_currentIncome.setIndent(10)

        self.p1_vBox_hBoxLayout.addWidget(self.label_currentIncome)

        self.label_currentIncomeAmount = QLabel(self.verticalLayoutWidget)
        self.label_currentIncomeAmount.setObjectName(u"label_currentIncomeAmount")
        self.label_currentIncomeAmount.setFont(font1)

        self.p1_vBox_hBoxLayout.addWidget(self.label_currentIncomeAmount)

        self.label_currentExpense = QLabel(self.verticalLayoutWidget)
        self.label_currentExpense.setObjectName(u"label_currentExpense")
        self.label_currentExpense.setFont(font2)
        self.label_currentExpense.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.p1_vBox_hBoxLayout.addWidget(self.label_currentExpense)

        self.label_currentExpenseAmount = QLabel(self.verticalLayoutWidget)
        self.label_currentExpenseAmount.setObjectName(u"label_currentExpenseAmount")
        self.label_currentExpenseAmount.setFont(font1)

        self.p1_vBox_hBoxLayout.addWidget(self.label_currentExpenseAmount)


        self.p1_vBoxLayout.addLayout(self.p1_vBox_hBoxLayout)

        self.label_today = QLabel(self.verticalLayoutWidget)
        self.label_today.setObjectName(u"label_today")
        self.label_today.setFont(font)
        self.label_today.setIndent(10)

        self.p1_vBoxLayout.addWidget(self.label_today)

        self.listWidget_today = QListWidget(self.page_1)
        self.listWidget_today.setObjectName(u"listWidget_today")
        self.listWidget_today.setGeometry(QRect(10, 210, 381, 531))
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(10)
        self.listWidget_today.setFont(font3)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayoutWidget_2 = QWidget(self.page_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 20, 381, 581))
        self.p2_vBoxLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.p2_vBoxLayout.setObjectName(u"p2_vBoxLayout")
        self.p2_vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.label_transaction = QLabel(self.verticalLayoutWidget_2)
        self.label_transaction.setObjectName(u"label_transaction")
        self.label_transaction.setFont(font)
        self.label_transaction.setAlignment(Qt.AlignCenter)

        self.p2_vBoxLayout.addWidget(self.label_transaction)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_amountBaht = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_amountBaht.setObjectName(u"lineEdit_amountBaht")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_amountBaht.sizePolicy().hasHeightForWidth())
        self.lineEdit_amountBaht.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Calibri"])
        font4.setPointSize(12)
        font4.setKerning(True)
        self.lineEdit_amountBaht.setFont(font4)
        self.lineEdit_amountBaht.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.lineEdit_amountBaht, 0, 1, 1, 1)

        self.label_category = QLabel(self.verticalLayoutWidget_2)
        self.label_category.setObjectName(u"label_category")
        self.label_category.setFont(font1)
        self.label_category.setIndent(10)

        self.gridLayout_6.addWidget(self.label_category, 2, 0, 1, 1)

        self.label_amountBaht = QLabel(self.verticalLayoutWidget_2)
        self.label_amountBaht.setObjectName(u"label_amountBaht")
        self.label_amountBaht.setFont(font1)
        self.label_amountBaht.setIndent(10)

        self.gridLayout_6.addWidget(self.label_amountBaht, 0, 0, 1, 1)

        self.lineEdit_category = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_category.setObjectName(u"lineEdit_category")
        sizePolicy.setHeightForWidth(self.lineEdit_category.sizePolicy().hasHeightForWidth())
        self.lineEdit_category.setSizePolicy(sizePolicy)
        self.lineEdit_category.setFont(font1)

        self.gridLayout_6.addWidget(self.lineEdit_category, 2, 1, 1, 1)

        self.label_amountSatang = QLabel(self.verticalLayoutWidget_2)
        self.label_amountSatang.setObjectName(u"label_amountSatang")
        self.label_amountSatang.setFont(font1)
        self.label_amountSatang.setIndent(10)

        self.gridLayout_6.addWidget(self.label_amountSatang, 1, 0, 1, 1)

        self.lineEdit_amountSatang = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_amountSatang.setObjectName(u"lineEdit_amountSatang")
        sizePolicy.setHeightForWidth(self.lineEdit_amountSatang.sizePolicy().hasHeightForWidth())
        self.lineEdit_amountSatang.setSizePolicy(sizePolicy)
        self.lineEdit_amountSatang.setFont(font1)
        self.lineEdit_amountSatang.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.lineEdit_amountSatang, 1, 1, 1, 1)


        self.p2_vBoxLayout.addLayout(self.gridLayout_6)

        self.label_memo = QLabel(self.verticalLayoutWidget_2)
        self.label_memo.setObjectName(u"label_memo")
        self.label_memo.setFont(font1)
        self.label_memo.setIndent(10)

        self.p2_vBoxLayout.addWidget(self.label_memo)

        self.textEdit_memo = QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_memo.setObjectName(u"textEdit_memo")
        self.textEdit_memo.setFont(font1)

        self.p2_vBoxLayout.addWidget(self.textEdit_memo)

        self.label_error = QLabel(self.verticalLayoutWidget_2)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setFont(font1)
        self.label_error.setAlignment(Qt.AlignCenter)

        self.p2_vBoxLayout.addWidget(self.label_error)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_income = QPushButton(self.verticalLayoutWidget_2)
        self.pb_income.setObjectName(u"pb_income")
        self.pb_income.setFont(font1)

        self.horizontalLayout.addWidget(self.pb_income)

        self.pb_expense = QPushButton(self.verticalLayoutWidget_2)
        self.pb_expense.setObjectName(u"pb_expense")
        self.pb_expense.setFont(font1)

        self.horizontalLayout.addWidget(self.pb_expense)


        self.p2_vBoxLayout.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayoutWidget_4 = QWidget(self.page_3)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 20, 381, 721))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_history = QLabel(self.verticalLayoutWidget_4)
        self.label_history.setObjectName(u"label_history")
        self.label_history.setFont(font)
        self.label_history.setIndent(10)

        self.verticalLayout.addWidget(self.label_history)

        self.listWidget_history = QListWidget(self.verticalLayoutWidget_4)
        self.listWidget_history.setObjectName(u"listWidget_history")
        self.listWidget_history.setFont(font3)

        self.verticalLayout.addWidget(self.listWidget_history)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 750, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pb_home = QPushButton(self.horizontalLayoutWidget)
        self.pb_home.setObjectName(u"pb_home")
        self.pb_home.setFont(font1)

        self.horizontalLayout_6.addWidget(self.pb_home)

        self.pb_input = QPushButton(self.horizontalLayoutWidget)
        self.pb_input.setObjectName(u"pb_input")
        self.pb_input.setFont(font1)

        self.horizontalLayout_6.addWidget(self.pb_input)

        self.pb_history = QPushButton(self.horizontalLayoutWidget)
        self.pb_history.setObjectName(u"pb_history")
        self.pb_history.setFont(font1)

        self.horizontalLayout_6.addWidget(self.pb_history)

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
        self.label_balanceAmount.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_currentIncome.setText(QCoreApplication.translate("MainWindow", u"Income:", None))
        self.label_currentIncomeAmount.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_currentExpense.setText(QCoreApplication.translate("MainWindow", u"Expense:", None))
        self.label_currentExpenseAmount.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_today.setText(QCoreApplication.translate("MainWindow", u"Today:", None))
        self.label_transaction.setText(QCoreApplication.translate("MainWindow", u"Transaction", None))
        self.lineEdit_amountBaht.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_category.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_amountBaht.setText(QCoreApplication.translate("MainWindow", u"Amount(Baht)", None))
        self.label_amountSatang.setText(QCoreApplication.translate("MainWindow", u"Amount(Satang)", None))
        self.lineEdit_amountSatang.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_memo.setText(QCoreApplication.translate("MainWindow", u"Memo", None))
        self.label_error.setText("")
        self.pb_income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.pb_expense.setText(QCoreApplication.translate("MainWindow", u"Expense", None))
        self.label_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.pb_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pb_input.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.pb_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
    # retranslateUi

