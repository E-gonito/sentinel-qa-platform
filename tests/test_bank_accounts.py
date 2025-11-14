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

def test_savings_account(bank_account_data):
    # 1. Get the dictionary from the list fixture
    data = bank_account_data[0]
    
    # 2. Instantiate the class using keyword arguments
    account = SavingsAccount(**data)

    # 3. Assert state
    assert isinstance(account, SavingsAccount)
    assert account.get_name() == "J.doe"
    assert account.get_account_number() == 1010
    assert account.get_balance() == 500
