class User:
    def __init__(self, name):
        self.name = name
        self.balance = Money(0, 0)

    def get_name(self):
        return self.name
    
    def get_balance(self):
        return self.balance