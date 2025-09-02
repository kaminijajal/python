from abc import ABC,abstractmethod

class Account(ABC): 
    
    balance = 0
    @abstractmethod                                                                            
    def deposite(self):
        pass
    
    def checkbalance(self):
        print(f"Curent Balance {self.balance}")

class SavingAccount(Account):

    def deposite(self,amount):
      self.balance = self.balance+amount
      print(f"{amount} : Credited")

class loanAccount(Account):

    def __init__(self,amount):
        self.balance = amount

    def deposite(self,amount):
        self.balance = self.balance-amount
        print(f"{amount} : credited")


s = SavingAccount()
s.deposite(10000)
s.checkbalance()

print("-------------------------")

l = loanAccount(20000)
l.deposite(10000)
l.checkbalance()