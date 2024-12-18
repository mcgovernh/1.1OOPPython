class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute
    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}. New balance: {self.__balance}"
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return f"Withdrew {amount}. New balance: {self.__balance}"
# Create an object
account = BankAccount("12345", 1000)
print(account.deposit(500))  # Output: Deposited 500. New balance: 1500
print(account.withdraw(2000))  # Output: Insufficient funds
