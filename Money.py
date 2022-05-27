class Money:
    def __init__(self, baht, satang):
        self.baht = baht
        self.satang = satang

    def __str__(self):
        return str(self.baht) + '.' + str(self.satang)
    
    def get_baht(self):
        return self.baht
    
    def get_satang(self):
        return self.satang
    
    def deposit(self, transaction_money):
        self.baht += transaction_money.get_baht()
        self.satang += transaction_money.get_satang()
    
    def withdraw(self, transaction_money):
        self.baht -= transaction_money.get_baht()
        self.satang -= transaction_money.get_satang()