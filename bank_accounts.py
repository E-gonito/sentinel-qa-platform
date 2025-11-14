from abc import ABC, abstractmethod

# Abstraction Base Class: Cannot directly initialise this class
class BankAccount(ABC):
    def __init__(self, name, account_number, balance):
        self.__name = name # Private
        self.__account_number = account_number
        self._balance = balance # Protected, children can access
        
    # Concrete Methods: Shared by all children
    def get_name(self):
        return self.__name
    
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self._balance
    
    def add_money(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        return self.get_balance
    
    # Abstract Methods: Children must implement their own functions defined here
    @abstractmethod
    def withdraw_money(self, amount):
        pass
    
# This class inherits from above class
class CurrentAccount(BankAccount):
    def __init__(self, name, account_number, balance, overdraft_limit):
        super().__init__(name, account_number, balance)
        self.__overdraft_limit = overdraft_limit
            
    # Polymorphism: this overrides the parent's withdraw_money class
    def withdraw_money(self,amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        elif amount > (self.get_balance() + self.__overdraft_limit):
            raise ValueError("Insufficient funds")
        else:
            self._balance -= amount
            return self.get_balance()
        
class SavingsAccount(BankAccount):
    def withdraw_money(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        elif amount > self._balance:
            raise ValueError("Insufficient funds")
        else:
            self._balance -= amount
            return self.get_balance()
