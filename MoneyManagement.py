import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from uiForm_2 import Ui_MainWindow
import ZODB, ZODB.FileStorage
import transaction
import persistent
import datetime
import moneyTransaction
import passiveMoney
import money
import user

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

        self.passiveStorage = ZODB.FileStorage.FileStorage('passive.fs')
        self.passiveDb = ZODB.DB(self.passiveStorage)
        self.passiveConnection = self.passiveDb.open()
        self.passiveRoot = self.passiveConnection.root()

        #money management attr
        try:
            self.user = self.root['user']
            self.balance = self.root['user'].get_balance()
            self.currentIncome = self.root['currentIncome']
            self.currentExpense = self.root['currentExpense']
        except:
            self.root['user'] = user.User('Admin')
            self.balance = self.root['user'].get_balance()
            self.root['currentIncome'] = money.Money(0, 0)
            self.currentIncome = self.root['currentIncome']
            self.root['currentExpense'] = money.Money(0, 0)
            self.currentExpense = self.root['currentExpense']

        self.today = str(datetime.datetime.now())[:10]
        self.update_passiveMoney()

        self.update_listWidget_today()
        self.ui.label_today.setText("Today: " + self.today)
        self.ui.label_balanceAmount.setText(str(self.balance))
        self.ui.label_currentIncomeAmount.setText(str(self.currentIncome))
        self.ui.label_currentExpenseAmount.setText(str(self.currentExpense))

        #page 1
        self.ui.pb_home.clicked.connect(self.change_page)
        self.ui.pb_input.clicked.connect(self.change_page)
        self.ui.pb_history.clicked.connect(self.change_page)

        #page 2
        self.ui.pb_income.clicked.connect(self.add_transaction)
        self.ui.pb_expense.clicked.connect(self.add_transaction)
        self.ui.pb_addPassive.clicked.connect(self.change_page)

        #page 3
        self.ui.dateEdit_endDate.setDate(QDateTime().currentDateTime().date())
        self.ui.pb_passiveIncome.clicked.connect(self.add_passive)
        self.ui.pb_passiveExpense.clicked.connect(self.add_passive)

        #page 4
        self.ui.pb_search.clicked.connect(self.search_history)

        #set background
        self.setStyleSheet('background-image: url("C:/Users/BankYiSip/Desktop/SE_Lab/SEP/Project_SEP_MoneyManagement/stripe.png")')

    def change_page(self):
        sender = self.sender().objectName()
        if(sender == 'pb_home'):
            self.ui.stackedWidget.setCurrentIndex(0)
        elif(sender == 'pb_input'):
            self.ui.stackedWidget.setCurrentIndex(1)
        elif(sender == 'pb_addPassive'):
            self.ui.stackedWidget.setCurrentIndex(2)
        elif(sender == 'pb_history'):
            self.ui.stackedWidget.setCurrentIndex(3)   
    
    def add_transaction(self):
        self.ui.label_error.setText("")
        sender = self.sender().objectName()
        try:
            baht = int(self.ui.lineEdit_amountBaht.text())
            satang = int(self.ui.lineEdit_amountSatang.text())
            category = self.ui.lineEdit_category.text()
            memo = self.ui.textEdit_memo.toPlainText()
        except:
            self.ui.label_error.setText("Error: Invalid Input!")
            return
        time = str(datetime.datetime.now())
        transaction_money = money.Money(baht, satang)
        if(sender == 'pb_income'):
            transaction_type = 'Income'
            self.update_current_income(transaction_money)
        elif(sender == 'pb_expense'):
            transaction_type = 'Expense'
            self.update_current_expense(transaction_money)
        self.root[time] = moneyTransaction.MoneyTransaction(transaction_money, transaction_type, category, memo)
        self.update_balance(transaction_money, transaction_type)
        self.update_listWidget_today()
        # transaction.commit()

    def add_passive(self):
        self.ui.label_passiveError.setText("")
        sender = self.sender().objectName()
        if(self.ui.lineEdit_title.text() == ''):
            self.ui.label_passiveError.setText("Error: Please enter the Title!")
            return
        if(not self.ui.rb_monthly.isChecked() and not self.ui.rb_annually.isChecked()):
            self.ui.label_passiveError.setText("Error: Please choose the frequency!")
            return
        try:
            title = self.ui.lineEdit_title.text()
            baht = int(self.ui.lineEdit_passiveBaht.text())
            satang = int(self.ui.lineEdit_passiveSatang.text())
            category = self.ui.lineEdit_passiveCategory.text()
            memo = self.ui.textEdit_passiveMemo.toPlainText()
            if(self.ui.rb_monthly.isChecked()):
                frequency = self.ui.rb_monthly.text()
            else:
                frequency = self.ui.rb_annually.text()
            endDate = self.ui.dateEdit_endDate.date().toString('yyyy-MM-dd')
        except:
            self.ui.label_passiveError.setText("Error: Invalid Input!")
            return
        
        passive_money = money.Money(baht, satang)
        if(sender == 'pb_passiveIncome'):
            transaction_type = 'Income'
        elif(sender == 'pb_passiveExpense'):
            transaction_type = 'Expense'
        
        pMoney = passiveMoney.PassiveMoney(passive_money, transaction_type, category, memo, title, endDate, frequency)
        self.passiveRoot[pMoney.get_title()] = pMoney
        self.update_passive_continue(pMoney.get_title())

    def update_passive_continue(self, key):
        transaction_money = self.passiveRoot[key].get_money()
        transaction_type = self.passiveRoot[key].get_transactionType()
        category = self.passiveRoot[key].get_category()
        memo = self.passiveRoot[key].get_memo()

        if(transaction_type == 'Income'):
            self.update_current_income(transaction_money)
        elif(transaction_type == 'Expense'):
            self.update_current_expense(transaction_money)

        time = str(datetime.datetime.now())
        self.root[time] = moneyTransaction.MoneyTransaction(transaction_money, transaction_type, category, memo)
        self.update_balance(transaction_money, transaction_type)
        self.update_listWidget_today()
    
    def update_balance(self, money, transaction_type): #transaction type = income/expense
        if(transaction_type == 'Income'): 
            self.root['user'].get_balance().deposit(money)
        elif(transaction_type == 'Expense'): 
            self.root['user'].get_balance().withdraw(money)
        
        self.balance = self.root['user'].get_balance()
        self.ui.label_balanceAmount.setText(str(self.balance))

    def update_current_income(self, money):
        self.currentIncome.deposit(money)
        self.root['currentIncome'] = self.currentIncome
        self.ui.label_currentIncomeAmount.setText(str(self.currentIncome))

    def update_current_expense(self, money):
        self.currentExpense.withdraw(money)
        self.root['currentExpense'] = self.currentExpense
        self.ui.label_currentExpenseAmount.setText(str(self.currentExpense))

    def update_listWidget_today(self):
        self.ui.listWidget_today.clear()
        for key in self.root:
            if(key[:10] == self.today):
                self.ui.listWidget_today.addItem(str(self.root[key]))

    def update_passiveMoney(self):
        delKey = []
        for key in self.passiveRoot:
            if(self.passiveRoot[key].get_endDate() == self.today):
                self.delList.append(key)

        for key in delKey:
            del self.passiveRoot[key]
        delKey.clear()

        for pMoney in self.passiveRoot:
            if(self.passiveRoot[pMoney].get_nextDate() == self.today):
                self.passiveRoot[pMoney].update_nextDate()
                self.add_passive_continue(pMoney)

    def search_history(self):
        self.ui.listWidget_history.clear()
        self.ui.label_search_error.setText("")
        year = self.ui.lineEdit_year.text()
        month = self.ui.lineEdit_month.text()
        
        if((month.isnumeric() or month == '') and year.isnumeric()): 
            pass
        else:
            self.ui.label_search_error.setText("Error: Invalid Input!")
            return
        
        if(month == ''):
           for key in self.root:
                if(key[:4] == year):
                    self.ui.listWidget_history.addItem(key[:19] + ' ' + str(self.root[key]))
                else:
                    if(key[:4].isnumeric()):
                        self.ui.label_search_error.setText('Information not found!')
        else:
            for key in self.root:
                if(key[:7] == (year + '-' + month) or key[:7] == (year + '-0' + month)):
                    self.ui.listWidget_history.addItem(key[:19] + ' ' + str(self.root[key]))
                else:
                    if(key[:4].isnumeric()):
                        self.ui.label_search_error.setText('Information not found!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MoneyManagement()
    w.show()
    sys.exit(app.exec_())

        
###### dont forget to add transaction.commit()