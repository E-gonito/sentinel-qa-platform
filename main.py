class BankAccount:
    company = "BigBanks"
    def __init__(self, name, account_number, balance, has_overdraft):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.has_overdraft = has_overdraft
    
    def balance(self):
        return f"Your balance is: £${self.balance}"
    
    def add_money(self, amount):
        self.balance += amount
        return f"Your new balance is: £${self.balance}"
        
"""
Testing Data
bank_account = BankAccount("Jane", 101010, 200, False)
print(bank_account.name)
"""