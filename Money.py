import persistent

class Money(persistent.Persistent):
    def __init__(self, baht, satang):
        self.baht = baht
        self.satang = satang

    def __str__(self):
        string_satang = str(self.satang)
        if(self.satang < 0):
            string_satang = str(self.satang)[1:]
        return str(self.baht) + '.' + string_satang
    
    def get_baht(self):
        return self.baht
    
    def get_satang(self):
        return self.satang
    
    def deposit(self, transaction_money):
        self.baht += transaction_money.get_baht()
        self.satang += transaction_money.get_satang()
        if(self.satang >= 100):
            self.satang -= 100
            self.baht += 1
    
    def withdraw(self, transaction_money):
        self.baht -= transaction_money.get_baht()
        self.satang -= transaction_money.get_satang()
        if(self.satang <= -100):
            self.satang += 100
            self.baht -= 1