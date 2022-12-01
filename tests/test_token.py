from unittest import TestCase
import pytest

from tartarus.constants import ETH_NATIVE_ADDRESS
from tartarus.token import Token


@pytest.fixture
def token_contract(w3, get_contract):
    code = """
@external
@view
def get_balance() -> uint256:
    a: uint256 = self.balance
    return a

@external
@payable
def __default__():
    pass
    """
    contract = get_contract(code, *[w3.eth.accounts[0]])
    return contract


def test_get_balance_ETH(w3, token_contract):
    url = 'https://some_url.com'  # mainnet
    token_address = ETH_NATIVE_ADDRESS
    value = 1337 * 10 ^ 18
    w3.eth.send_transaction({"to": token_contract.address, "value": value})
    assert token_contract.get_balance() == value

    t = Token(
        w3=w3,
        url=url,
        wallet_address=token_contract.address,
        token_address=token_address,
    )
    balance = t.get_balance()
    assert balance == f'{value / 10 ** 18}'


@pytest.mark.skip(reason='Call external service')
class TestCoinExternal(TestCase):

    def setUp(self):
        self.url = 'https://mainnet.infura.io/v3/9e4bc49c44c34ac7ae3e5c34fe5e1d62'  # mainnet

    def tearDown(self): pass

    def test_get_balance(self):
        wallet_address = '0x4e65175f05b4140a0747c29cce997cd4bb7190d4'  # my wallet
        token_address = '0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9'  # AAVE
        t = Token(
            url=self.url,
            wallet_address=wallet_address,
            token_address=token_address,
        )
        balance = t.get_balance()
        assert balance

    def test_get_symbol(self):
        wallet_address = '0x4e65175f05b4140a0747c29cce997cd4bb7190d4'  # my wallet
        token_address = '0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9'  # AAVE
        t = Token(
            url=self.url,
            wallet_address=wallet_address,
            token_address=token_address,
        )
        symbol = t.get_symbol()
        assert symbol == 'AAVE'

    def test_get_decimal(self):
        wallet_address = '0x4e65175f05b4140a0747c29cce997cd4bb7190d4'  # my wallet
        token_address = '0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9'  # AAVE
        t = Token(
            url=self.url,
            wallet_address=wallet_address,
            token_address=token_address,
        )
        decimal = t.get_decimal()
        assert decimal == 18

