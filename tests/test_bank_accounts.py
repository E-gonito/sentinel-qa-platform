import pytest
from bank_accounts import SavingsAccount 

# Pytest fixture for reusable data
@pytest.fixture
def bank_account_data():
    return [
        {
            "name": "J.doe",
            "account_number": 1010,
            "balance": 500,
        },
    ]

# Reusable savings account 
@pytest.fixture
def savings_account(bank_account_data):
    return SavingsAccount(**bank_account_data[0])

def test_savings_account_creation(savings_account):
    assert isinstance(savings_account, SavingsAccount)
    assert savings_account.get_name() == "J.doe"
    assert savings_account.get_account_number() == 1010
    assert savings_account.get_balance() == 500

def test_savings_account_withdraw_money(savings_account):
    savings_account.withdraw_money(100)
    assert savings_account.get_balance() == 400

def test_savings_account_withdraw_money_negative_amount(savings_account):
    with pytest.raises(ValueError, match="Amount must be positive"):
        savings_account.withdraw_money(-10)

def test_savings_account_withdraw_money_insufficient_funds(savings_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        savings_account.withdraw_money(600)

def test_savings_account_withdraw_money_success(savings_account):
    new_balance = savings_account.withdraw_money(100)
    assert new_balance == 400
    assert savings_account.get_balance() == 400