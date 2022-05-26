class MoneyManagement:
    def __init__(self):
        self.user
        self.transaction_log #may be something that connect to database ; right now is just a list
    
    def add_transaction(self, money):
        self.transaction_log.append(money)
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


        
    