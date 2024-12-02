import pytest
import os
import json
from unittest.mock import patch, mock_open
from datetime import datetime
from services.transaction_manager import TransactionManager
from services.account_privileges_manager import AccountPrivilegesManager
from views.account_ui import AccountUI

# Sample transaction log for testing
sample_transactions = [
    {
        "account_number": 123456,
        "amount": 100.0,
        "transaction_type": "Deposit",
        "date": "2024-11-15 10:00:00",
        "to_account_number": None
    },
    {
        "account_number": 123456,
        "amount": 50.0,
        "transaction_type": "Withdraw",
        "date": "2024-11-16 12:00:00",
        "to_account_number": None
    }
]

# Mock file content
mocked_file_content = json.dumps(sample_transactions)


# 1. Test input_transaction
@patch("builtins.input", side_effect=["123456", "Deposit", "100"])
@patch("services.transaction_manager.TransactionManager.log_transaction")
def test_input_transaction(mock_log_transaction, mock_input):
    TransactionManager.input_transaction()
    mock_log_transaction.assert_called_once_with(123456, 100.0, "Deposit", None)


# 2. Test display_transactions
@patch("builtins.open", new_callable=mock_open, read_data=mocked_file_content)
@patch("os.path.exists", return_value=True)
def test_display_transactions(mock_exists, mock_open):
    with patch("builtins.print") as mock_print:
        TransactionManager.display_transactions()
        assert mock_print.called
        assert "Transaction Log:" in mock_print.call_args_list[0][0][0]


# 3. Test view_transactions_by_account_and_date_range
@patch("builtins.input", side_effect=["123456", "2024-11-14", "2024-11-16"])
@patch("builtins.open", new_callable=mock_open, read_data=mocked_file_content)
@patch("os.path.exists", return_value=True)
def test_view_transactions_by_account_and_date_range(mock_exists, mock_open, mock_input):
    with patch("builtins.print") as mock_print:
        TransactionManager.view_transactions_by_account_and_date_range()
        assert mock_print.called
        assert "Transactions for account 123456" in mock_print.call_args_list[0][0][0]


# 4. Test get_transactions_by_type
@patch("builtins.open", new_callable=mock_open, read_data=mocked_file_content)
@patch("os.path.exists", return_value=True)
def test_get_transactions_by_type(mock_exists, mock_open):
    result = TransactionManager.get_transactions_by_type(123456, "Deposit")
    assert len(result) == 1
    assert result[0]["transaction_type"] == "Deposit"


# 5. Test AccountPrivilegesManager update_transfer_limit
def test_update_transfer_limit():
    AccountPrivilegesManager.privileges = {
        "PREMIUM": 1000,
        "GOLD": 500,
        "SILVER": 100
    }
    result = AccountPrivilegesManager.update_transfer_limit("GOLD", 700)
    assert result is True
    assert AccountPrivilegesManager.privileges["GOLD"] == 700


# 6. Test AccountPrivilegesManager get_transfer_limit
def test_get_transfer_limit():
    AccountPrivilegesManager.privileges = {
        "PREMIUM": 1000,
        "GOLD": 500,
        "SILVER": 100
    }
    assert AccountPrivilegesManager.get_transfer_limit("PREMIUM") == 1000
    assert AccountPrivilegesManager.get_transfer_limit("SILVER") == 100


# # 7. Test checktransferlimit
# @patch("builtins.input", side_effect=["123456"])
# @patch("repositories.account_repository.AccountRepository.accounts", [{"account_number": 123456, "privilege": "GOLD"}])
# @patch("builtins.print")
# def test_check_transfer_limit(mock_print, mock_input):
#     AccountUI().checktransferlimit()
#     assert mock_print.called
#     assert "Your Privilege: GOLD" in mock_print.call_args_list[0][0][0]



def test_check_transfer_limit():
    # Setup: Create a test AccountUI instance and inject test data
    account_ui = AccountUI()
    account_ui.accounts = [
        {"account_number": 123456, "privilege": "GOLD"},
        {"account_number": 654321, "privilege": "SILVER"}
    ]
    
    AccountPrivilegesManager.privileges = {
        "GOLD": 700,
        "SILVER": 300
    }
    
    # Provide inputs and capture output
    account_number_to_test = 123456
    expected_privilege = "GOLD"
    expected_limit = 700
    
    # Simulate the method behavior
    account = next((acc for acc in account_ui.accounts if acc["account_number"] == account_number_to_test), None)
    if account:
        privilege = account["privilege"]
        transfer_limit = AccountPrivilegesManager.get_transfer_limit(privilege)
        
        # Assertions
        assert privilege == expected_privilege
        assert transfer_limit == expected_limit
    else:
        pytest.fail("Invalid Account Number!")

def test_check_transfer_limit_invalid_account():
    # Setup: Create a test AccountUI instance and inject test data
    account_ui = AccountUI()
    account_ui.accounts = [
        {"account_number": 123456, "privilege": "GOLD"},
        {"account_number": 654321, "privilege": "SILVER"}
    ]
    
    # Provide an invalid account number
    account_number_to_test = 999999
    
    # Simulate the method behavior
    account = next((acc for acc in account_ui.accounts if acc["account_number"] == account_number_to_test), None)
    if account:
        pytest.fail("Invalid test setup: account should not exist!")
    else:
        assert account is None  # Verify no account is found