import pytest
from bank_accounts import CurrentAccount 

@pytest.fixture
def bank_account_data():
    return [
        {
            "name": "J.doe",
            "account_number": 1010,
            "balance": 500,
        },
    ]

def test_current_account(bank_account_data):
    assert CurrentAccount()

def test_fail():
    assert False