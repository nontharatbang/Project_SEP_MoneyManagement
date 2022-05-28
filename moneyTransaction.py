import money
import persistent

class MoneyTransaction(persistent.Persistent):
    def __init__(self, money, transactionType, category, memo):
        self.money = money
        self.transactionType = transactionType
        self.category = category
        self.memo = memo

    def __str__(self):
        string = self.transactionType + ', Money: ' + str(self.money)
        if(self.category != ''):
            string += ', Category: ' + self.get_category()
        if(self.memo != ''):
            string += ', Memo: ' + self.get_memo()
        return string

    def get_money(self):
        return self.money
    
    def get_transactionType(self):
        return self.transactionType

    def get_category(self):
        return self.category

    def get_memo(self):
        return self.memo
