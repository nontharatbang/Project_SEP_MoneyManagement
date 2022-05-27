import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from UiForm_2 import Ui_MainWindow
import ZODB, ZODB.FileStorage
import transaction
import persistent
import datetime
import moneyTransaction
import money

class MoneyManagement(QMainWindow):
    def __init__(self):
        #set up UI
        QMainWindow.__init__(self, None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #set up database
        self.storage = ZODB.FileStorage.FileStorage('wallet.fs')
        self.db = ZODB.DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

        #money management attr
        try:
            self.balance = root['balance']
            self.currentIncome = root['currentIncome']
            self.currentExpense = root['currentExpense']
        except:
            self.root['balance'] = money.Money(0, 0)
            self.balance = self.root['balance']
            self.root['currentIncome'] = money.Money(0, 0)
            self.currentIncome = self.root['currentIncome']
            self.root['currentExpense'] = money.Money(0, 0)
            self.currentExpense = self.root['currentExpense']

        self.ui.label_balanceAmount.setText(str(self.root['balance']))
        self.ui.label_currentIncomeAmount.setText(str(self.root['currentIncome']))
        self.ui.label_currentExpenseAmount.setText(str(self.root['currentExpense']))

        #page 1
        self.ui.pb_home.clicked.connect(self.changePage)
        self.ui.pb_input.clicked.connect(self.changePage)
        self.ui.pb_history.clicked.connect(self.changePage)

        #page 2
        self.ui.pb_income.clicked.connect(self.add_transaction)
        self.ui.pb_expense.clicked.connect(self.add_transaction)

    def changePage(self):
        sender = self.sender().objectName()
        if(sender == 'pb_home'):
            self.ui.stackedWidget.setCurrentIndex(0)
        elif(sender == 'pb_input'):
            self.ui.stackedWidget.setCurrentIndex(1)
        elif(sender == 'pb_history'):
            self.ui.stackedWidget.setCurrentIndex(2)    
    
    def add_transaction(self):
        self.ui.label_error.setText("")
        sender = self.sender().objectName()
        if(sender == 'pb_income'):
            # try:
            baht = int(self.ui.lineEdit_amountBaht.text())
            satang = int(self.ui.lineEdit_amountSatang.text())
            category = self.ui.lineEdit_category.text()
            memo = self.ui.textEdit_memo.toPlainText()

            time = str(datetime.datetime.now())
            self.root[time] = moneyTransaction.MoneyTransaction(baht, satang, "income", category, memo)
            print('try pass!')
            # except:
            #     self.ui.label_error.setText("Error: Invalid Input!")
        elif(sender == 'pb_expense'):
            pass
        print(self.root.items())
        print(str(self.root[time]))
        #Add data to database
    
    def update_balance(self, transaction, transaction_type): #transaction type = negative/positive
        if(transactin_type == "positive"): self.user.balance.add(transaction.money)
        else: self.user.balance.subtract(transaction.money)

    def display_transaction_log(self):
        #display transaction log from the database
        pass

    def store_transaction_log(self):
        #store transaction in the database
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MoneyManagement()
    w.show()
    sys.exit(app.exec_())

        
    