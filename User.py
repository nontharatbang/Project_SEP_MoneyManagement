import money
import persistent

class User(persistent.Persistent):
    def __init__(self, name):
        self.name = name
        self.balance = money.Money(0, 0)

    def get_name(self):
        return self.name
    
    def get_balance(self):
        return self.balance
