import pytest
from wallet import Wallet, InsufficientAmount

def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    """Test proper exception is raised when spend cash exceed balance"""

    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)