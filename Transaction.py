class Transaction:
    def __init__(self, money, date, category, memo):
        self.money = money
        self.date = date
        self.category = category
        self.memo = memo

    def get_date(self):
        return self.date

    def get_detail(self, date):
        pass

    def get_category(self, category):
        return self.category
