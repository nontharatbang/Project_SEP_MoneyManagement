import money

class MoneyTransaction:
    def __init__(self, baht, satang, transactionType, category, memo):
        self.money = money.Money(baht, satang)
        self.transactin_type = transactionType
        self.category = category
        self.memo = memo

    def __str__(self):
        return self.transactin_type + ', Money: ' + str(self.money) + ', Category: ' + self.get_category() + ', Memo: ' + self.get_memo()

    def get_category(self):
        return self.category

    def get_memo(self):
        return self.memo
