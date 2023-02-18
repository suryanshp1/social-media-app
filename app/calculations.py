class InsufficientFunds(Exception):
    pass


def add(num1: int, num2: int = 2):
    return num1+num2

def subtract(num1: int, num2: int):
    return num1-num2

def multiply(num1: int, num2: int):
    return num1*num2

def divide(num1: int, num2: int):
    return num1/num2

class BankAccount():
    def __init__(self, starting_balance = 0) -> None:
        self.balance = starting_balance

    def deposite(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds account")
        self.balance -= amount

    def collect_interest(self):
        self.balance *= 1.1