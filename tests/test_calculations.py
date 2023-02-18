import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds


@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3,2,5), 
    (7,1,8),
    (12,4,16)
])
def test_add(num1, num2, expected):
    print("Testing add function")
    assert add(num1,num2) == expected

def test_subtract():
    assert subtract(5,3) == 2

def test_multiply():
    assert multiply(2,2) == 4

def test_divide():
    assert divide(10, 5) == 2


def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_bank_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.balance == 20

def test_bank_deposite(bank_account):
    bank_account.deposite(30)
    assert bank_account.balance == 80

def test_bank_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55

@pytest.mark.parametrize("deposited, withdrew, expected", [
    (30,20,10), 
    (400,200,200),
    (120,40,80),
    (1200,40,1160)
])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposite(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)