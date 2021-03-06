import moneyTransaction
import money
import datetime
from dateutil import relativedelta

class PassiveMoney(moneyTransaction.MoneyTransaction):
    def __init__(self, money, transactionType, category, memo, title, endDate, frequency, status = 1, time = datetime.datetime.now()):
        moneyTransaction.MoneyTransaction.__init__(self, money, transactionType, category, memo)
        self.title = title
        self.endDate = endDate
        self.frequency = frequency
        self.currentDate = time
        self.nextDate = self.calculate_nextDate(self.currentDate)
        self.status = status

    def get_title(self):
        return self.title
    
    def get_endDate(self):
        return self.endDate

    def get_frequency(self):
        return self.frequency
    
    def get_currentDate(self):
        return str(self.currentDate) #it stores date and time in the form of object

    def get_nextDate(self):
        return self.nextDate
    
    def get_status(self):
        return self.status
    
    def set_status(self, newStatus):
        self.status = newStatus

    def calculate_nextDate(self, currentDate):
        if(self.frequency == 'Monthly'):
            self.nextDate = self.currentDate + relativedelta.relativedelta(months=1)
        elif(self.frequency == 'Annually'):
            self.nextDate = self.currentDate + relativedelta.relativedelta(years=1)
        else:
            return
        return self.nextDate
    
    def update_nextDate(self): # call whe the nextDate is reach to update the current one
        self.currentDate = datetime.datetime.now()
        self.nextDate = self.calculate_nextDate(self.currentDate)


# if __name__ == '__main__':
#     t1 = PassiveMoney(money.Money(10,0), 'Income', '', '', 'Test', '10-10-2020', 'Annually')
#     print(t1)
#     print(t1.get_status())
#     print(str(t1.currentDate))
#     print(t1.get_nextDate())
#     t1.update_nextDate()
#     print(t1.get_nextDate())
#     print('te')