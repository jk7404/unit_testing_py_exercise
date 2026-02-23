import pytest
from bank_account.bank_account import BankAccount

@pytest.fixture
def start_account():
    return BankAccount(100)

def test_invalid_account():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount(-10)

def test_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150

def test_invalid_deposit(start_account):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        start_account.deposit(-10)

def test_withdraw(start_account):
    start_account.withdraw(30)
    assert start_account.balance == 70

def test_invalid_withdraw(start_account):
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        start_account.withdraw(-10)
        
def test_insufficient_funds(start_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        start_account.withdraw(150)

def test_transfer(start_account):
    target_account = BankAccount(50)
    start_account.transfer_to(target_account, 20)
    assert start_account.balance == 80
    assert target_account.balance == 70

def test_invalid_transfer(start_account):
    with pytest.raises(ValueError, match="Target must be a BankAccount"):
        start_account.transfer_to("not an account", 20)