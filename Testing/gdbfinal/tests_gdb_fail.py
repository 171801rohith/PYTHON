from models.account import Account
from services.transaction_manager import TransactionManager
from models.user import User
import datetime


def test_account_equality():
    a1 = Account("rohith",1000.0, 123, "GOLD")
    a2 = Account("rohith",1000.0, 190, "GOLD")
    assert a1.name == a2.name
    assert a1.balance == a2.balance
    assert a1.pin_number == a2.pin_number
    assert a1.privilege == a2.privilege

def test_account_field_access():
    a = Account("pranava",1002.0, 125, "GOLD")
    assert a.name == "pranava"
    assert a.balance == 1002.0
    assert a.pin_number == 125
    assert a.privilege == "SILVER"

def test_account_inequality():
    a1 = Account("rohith",1000.0, 123, "GOLD")
    a2 = Account("pranva",1340.0, 234, "PREMIUM")
    assert a1.name == a2.name
    assert a1.balance == a2.balance
    assert a1.pin_number == a2.pin_number
    assert a1.privilege == a2.privilege

def test_transaction_log_inequality():
    t1 = TransactionManager()
    transaction = {
        "account_number": 1001,
        "amount": 2000,
        "transaction_type": "transfer",
        "date": "2024-11-21T00:05:31.174050",
        "to_account_number": 1002,
    }
    t1.transaction_log.append(transaction)
    t2 = TransactionManager()
    transaction = {
        "account_number": 1001,
        "amount": 2020,
        "transaction_type": "transfer",
        "date": "2024-11-02T00:05:31.174050",
        "to_account_number": 1102,
    }
    t2.transaction_log.append(transaction)

    assert t1.transaction_log[0] != t2.transaction_log[0]

    def test_user_inequalities():
        u1 = User(123, "rohith", "234", "active")
        u2 = User(123, "gagan", "234", "inactive")
        assert u1.user_id == u2.user_id
        assert u1.name == u2.name
        assert u1.status == u2.status

def test_get_current_timestamp():
    timestamp = TransactionManager.get_current_timestamp()
    assert isinstance(timestamp, datetime.datetime)

# Test: Log a transaction
def test_log_transaction():
    TransactionManager.transaction_log = []  # Reset log to start fresh
    # Log a new transaction
    TransactionManager.log_transaction(12345, 100.0, "deposit")
    
    # Check if the transaction is added
    assert len(TransactionManager.transaction_log) == 1
    assert TransactionManager.transaction_log[0]["transaction_type"] == "transfer"