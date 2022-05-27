# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiForm_2.ui'
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
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(12)
        self.stackedWidget.setFont(font)
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
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_savingBalance.setFont(font1)
        self.label_savingBalance.setTextFormat(Qt.PlainText)
        self.label_savingBalance.setIndent(10)

        self.horizontalLayout_2.addWidget(self.label_savingBalance)

        self.label_balanceAmount = QLabel(self.verticalLayoutWidget)
        self.label_balanceAmount.setObjectName(u"label_balanceAmount")
        self.label_balanceAmount.setFont(font)

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
        self.label_currentIncomeAmount.setFont(font)

        self.p1_vBox_hBoxLayout.addWidget(self.label_currentIncomeAmount)

        self.label_currentExpense = QLabel(self.verticalLayoutWidget)
        self.label_currentExpense.setObjectName(u"label_currentExpense")
        self.label_currentExpense.setFont(font2)
        self.label_currentExpense.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.p1_vBox_hBoxLayout.addWidget(self.label_currentExpense)

        self.label_currentExpenseAmount = QLabel(self.verticalLayoutWidget)
        self.label_currentExpenseAmount.setObjectName(u"label_currentExpenseAmount")
        self.label_currentExpenseAmount.setFont(font)

        self.p1_vBox_hBoxLayout.addWidget(self.label_currentExpenseAmount)


        self.p1_vBoxLayout.addLayout(self.p1_vBox_hBoxLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_today = QLabel(self.verticalLayoutWidget)
        self.label_today.setObjectName(u"label_today")
        self.label_today.setFont(font1)
        self.label_today.setIndent(10)

        self.horizontalLayout_3.addWidget(self.label_today)


        self.p1_vBoxLayout.addLayout(self.horizontalLayout_3)

        self.listWidget_today = QListWidget(self.page_1)
        self.listWidget_today.setObjectName(u"listWidget_today")
        self.listWidget_today.setGeometry(QRect(10, 210, 381, 531))
        self.listWidget_today.setFont(font)
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
        self.label_transaction.setFont(font1)
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
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(12)
        font3.setKerning(True)
        self.lineEdit_amountBaht.setFont(font3)
        self.lineEdit_amountBaht.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.lineEdit_amountBaht, 0, 1, 1, 1)

        self.label_category = QLabel(self.verticalLayoutWidget_2)
        self.label_category.setObjectName(u"label_category")
        self.label_category.setFont(font)
        self.label_category.setIndent(10)

        self.gridLayout_6.addWidget(self.label_category, 2, 0, 1, 1)

        self.label_amountBaht = QLabel(self.verticalLayoutWidget_2)
        self.label_amountBaht.setObjectName(u"label_amountBaht")
        self.label_amountBaht.setFont(font)
        self.label_amountBaht.setIndent(10)

        self.gridLayout_6.addWidget(self.label_amountBaht, 0, 0, 1, 1)

        self.lineEdit_category = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_category.setObjectName(u"lineEdit_category")
        sizePolicy.setHeightForWidth(self.lineEdit_category.sizePolicy().hasHeightForWidth())
        self.lineEdit_category.setSizePolicy(sizePolicy)
        self.lineEdit_category.setFont(font)

        self.gridLayout_6.addWidget(self.lineEdit_category, 2, 1, 1, 1)

        self.label_amountSatang = QLabel(self.verticalLayoutWidget_2)
        self.label_amountSatang.setObjectName(u"label_amountSatang")
        self.label_amountSatang.setFont(font)
        self.label_amountSatang.setIndent(10)

        self.gridLayout_6.addWidget(self.label_amountSatang, 1, 0, 1, 1)

        self.lineEdit_amountSatang = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_amountSatang.setObjectName(u"lineEdit_amountSatang")
        sizePolicy.setHeightForWidth(self.lineEdit_amountSatang.sizePolicy().hasHeightForWidth())
        self.lineEdit_amountSatang.setSizePolicy(sizePolicy)
        self.lineEdit_amountSatang.setFont(font)
        self.lineEdit_amountSatang.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.lineEdit_amountSatang, 1, 1, 1, 1)


        self.p2_vBoxLayout.addLayout(self.gridLayout_6)

        self.label_memo = QLabel(self.verticalLayoutWidget_2)
        self.label_memo.setObjectName(u"label_memo")
        self.label_memo.setFont(font)
        self.label_memo.setIndent(10)

        self.p2_vBoxLayout.addWidget(self.label_memo)

        self.textEdit_memo = QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_memo.setObjectName(u"textEdit_memo")
        self.textEdit_memo.setFont(font)

        self.p2_vBoxLayout.addWidget(self.textEdit_memo)

        self.label_error = QLabel(self.verticalLayoutWidget_2)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setFont(font)
        self.label_error.setAlignment(Qt.AlignCenter)

        self.p2_vBoxLayout.addWidget(self.label_error)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_income = QPushButton(self.verticalLayoutWidget_2)
        self.pb_income.setObjectName(u"pb_income")
        self.pb_income.setFont(font)

        self.horizontalLayout.addWidget(self.pb_income)

        self.pb_expense = QPushButton(self.verticalLayoutWidget_2)
        self.pb_expense.setObjectName(u"pb_expense")
        self.pb_expense.setFont(font)

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
        self.label_history.setFont(font1)
        self.label_history.setIndent(10)

        self.verticalLayout.addWidget(self.label_history)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_year = QLabel(self.verticalLayoutWidget_4)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setFont(font)
        self.label_year.setIndent(10)

        self.gridLayout.addWidget(self.label_year, 0, 0, 1, 1)

        self.lineEdit_year = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_year.setObjectName(u"lineEdit_year")
        sizePolicy.setHeightForWidth(self.lineEdit_year.sizePolicy().hasHeightForWidth())
        self.lineEdit_year.setSizePolicy(sizePolicy)
        self.lineEdit_year.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_year, 0, 1, 1, 1)

        self.label_month = QLabel(self.verticalLayoutWidget_4)
        self.label_month.setObjectName(u"label_month")
        self.label_month.setFont(font)
        self.label_month.setIndent(10)

        self.gridLayout.addWidget(self.label_month, 1, 0, 1, 1)

        self.lineEdit_month = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_month.setObjectName(u"lineEdit_month")
        sizePolicy.setHeightForWidth(self.lineEdit_month.sizePolicy().hasHeightForWidth())
        self.lineEdit_month.setSizePolicy(sizePolicy)
        self.lineEdit_month.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_month, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_search_error = QLabel(self.verticalLayoutWidget_4)
        self.label_search_error.setObjectName(u"label_search_error")
        self.label_search_error.setFont(font)
        self.label_search_error.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_search_error)

        self.pb_search = QPushButton(self.verticalLayoutWidget_4)
        self.pb_search.setObjectName(u"pb_search")
        self.pb_search.setFont(font)

        self.verticalLayout.addWidget(self.pb_search)

        self.listWidget_history = QListWidget(self.verticalLayoutWidget_4)
        self.listWidget_history.setObjectName(u"listWidget_history")
        self.listWidget_history.setFont(font)

        self.verticalLayout.addWidget(self.listWidget_history)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayoutWidget_5 = QWidget(self.page_4)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 20, 381, 101))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_typeDetail = QLabel(self.verticalLayoutWidget_5)
        self.label_typeDetail.setObjectName(u"label_typeDetail")
        self.label_typeDetail.setFont(font1)
        self.label_typeDetail.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label_typeDetail)

        self.label_dateDetail = QLabel(self.verticalLayoutWidget_5)
        self.label_dateDetail.setObjectName(u"label_dateDetail")
        font4 = QFont()
        font4.setFamilies([u"Calibri"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.label_dateDetail.setFont(font4)
        self.label_dateDetail.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_dateDetail)

        self.gridLayoutWidget_2 = QWidget(self.page_4)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 140, 379, 361))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_memoDetail = QLabel(self.gridLayoutWidget_2)
        self.label_memoDetail.setObjectName(u"label_memoDetail")
        self.label_memoDetail.setFont(font2)
        self.label_memoDetail.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_memoDetail.setMargin(15)

        self.gridLayout_2.addWidget(self.label_memoDetail, 2, 0, 1, 1)

        self.label_moneyDetail = QLabel(self.gridLayoutWidget_2)
        self.label_moneyDetail.setObjectName(u"label_moneyDetail")
        self.label_moneyDetail.setFont(font2)
        self.label_moneyDetail.setMargin(15)

        self.gridLayout_2.addWidget(self.label_moneyDetail, 0, 0, 1, 1)

        self.label_categoryDetail = QLabel(self.gridLayoutWidget_2)
        self.label_categoryDetail.setObjectName(u"label_categoryDetail")
        self.label_categoryDetail.setFont(font2)
        self.label_categoryDetail.setMargin(15)

        self.gridLayout_2.addWidget(self.label_categoryDetail, 1, 0, 1, 1)

        self.label_moneyDetailAmount = QLabel(self.gridLayoutWidget_2)
        self.label_moneyDetailAmount.setObjectName(u"label_moneyDetailAmount")
        self.label_moneyDetailAmount.setFont(font)
        self.label_moneyDetailAmount.setAlignment(Qt.AlignCenter)
        self.label_moneyDetailAmount.setMargin(15)

        self.gridLayout_2.addWidget(self.label_moneyDetailAmount, 0, 1, 1, 1)

        self.label_categoryDetailAmount = QLabel(self.gridLayoutWidget_2)
        self.label_categoryDetailAmount.setObjectName(u"label_categoryDetailAmount")
        self.label_categoryDetailAmount.setFont(font)
        self.label_categoryDetailAmount.setAlignment(Qt.AlignCenter)
        self.label_categoryDetailAmount.setMargin(15)

        self.gridLayout_2.addWidget(self.label_categoryDetailAmount, 1, 1, 1, 1)

        self.textEdit_memoDetail = QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_memoDetail.setObjectName(u"textEdit_memoDetail")
        self.textEdit_memoDetail.setFont(font)

        self.gridLayout_2.addWidget(self.textEdit_memoDetail, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 750, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pb_home = QPushButton(self.horizontalLayoutWidget)
        self.pb_home.setObjectName(u"pb_home")
        self.pb_home.setFont(font)

        self.horizontalLayout_6.addWidget(self.pb_home)

        self.pb_input = QPushButton(self.horizontalLayoutWidget)
        self.pb_input.setObjectName(u"pb_input")
        self.pb_input.setFont(font)

        self.horizontalLayout_6.addWidget(self.pb_input)

        self.pb_history = QPushButton(self.horizontalLayoutWidget)
        self.pb_history.setObjectName(u"pb_history")
        self.pb_history.setFont(font)

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

        self.stackedWidget.setCurrentIndex(3)


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
        self.label_year.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.label_month.setText(QCoreApplication.translate("MainWindow", u"Month(Optional)", None))
        self.label_search_error.setText("")
        self.pb_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_typeDetail.setText(QCoreApplication.translate("MainWindow", u"Income/ Expense", None))
        self.label_dateDetail.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_memoDetail.setText(QCoreApplication.translate("MainWindow", u"Memo:", None))
        self.label_moneyDetail.setText(QCoreApplication.translate("MainWindow", u"Money:", None))
        self.label_categoryDetail.setText(QCoreApplication.translate("MainWindow", u"Category:", None))
        self.label_moneyDetailAmount.setText("")
        self.label_categoryDetailAmount.setText("")
        self.pb_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pb_input.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.pb_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
    # retranslateUi

