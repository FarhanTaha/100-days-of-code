# Bank Account Class (Template/Blueprint)

class BankAccount:
    def __init__(self, account_holder, starting_balance = 0):
        self.account_holder = account_holder
        self.balance = starting_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        print(f"{self.account_holder} deposited {amount}. New balance is {self.balance} ")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            print(f"{self.account_holder} withdrew {amount}. New balance is {self.balance}")
        else:
            self.transaction_history.append(f"Failed withdrawal attempt: ${amount} (Insufficient funds)")
            print(f"Insufficient funds! Cannot withdraw {amount} from {self.account_holder}'s account.")

    def get_balance(self):
        print(f"{self.account_holder}'s current balance is {self.balance}")

    def show_transaction_history(self):
        print(f"Transaction history for {self.account_holder}:")
        for transaction in self.transaction_history:
            print(transaction)
    
    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"
    
    
# Creating a Bank Account Object for one person
account_1 = BankAccount("Taha", 1000)

# Attributes and Methods of Taha's Bank Account
account_1.deposit(500) # Method: deposit 500
account_1.withdraw(200) # Method: withdraw 200
account_1.get_balance() # Method: get current balance
account_1.withdraw(1500) # Method: attempt to withdraw more than the balance
print(account_1) # Method: display account information
account_1.show_transaction_history() # Method: display transaction history


# Creating a Bank Account Object for another person
account_2 = BankAccount("Robert", 2000)

# Attributes and Methods of Robert's Bank Account
account_2.deposit(300) # Method: deposit 300
account_2.withdraw(1000) # Method: withdraw 1000
account_2.get_balance() # Method: get current balance
account_2.withdraw(2500) # Method: attempt to withdraw more than the balance
print(account_2) # Method: display account information
account_2.show_transaction_history() # Method: display transaction history