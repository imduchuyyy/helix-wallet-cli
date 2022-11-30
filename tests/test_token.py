from unittest import TestCase
import pytest as pytest
from unittest.mock import MagicMock, patch

from tartarus.constants import ETH_NATIVE_ADDRESS
from tartarus.token import Token


def setUpModule(): pass


def tearDownModule(): pass


class TestCoin(TestCase):

    def setUp(self):
        self.url = 'https://some_url.com'  # mainnet

    def tearDown(self): pass

    @patch('tartarus.token.Token.build_w3', MagicMock())
    @patch('tartarus.token.Token.get_balance_native', MagicMock(return_value=311308790340449818330))
    def test_get_balance_ETH(self):
        wallet_address = '0x4e65175f05b4140a0747c29cce997cd4bb7190d4'
        token_address = ETH_NATIVE_ADDRESS
        t = Token(
            url=self.url,
            wallet_address=wallet_address,
            token_address=token_address,
        )
        balance = t.get_balance()
        assert balance == '311.3087903404498'

    @patch('tartarus.token.Token.build_w3', MagicMock())
    @patch('tartarus.token.Token.get_balance_non_native', MagicMock(return_value=311308790340449818330))
    @patch('tartarus.token.Token.get_decimal', MagicMock(return_value=19))
    def test_get_balance_non_native(self):
        wallet_address = '0x4e65175f05b4140a0747c29cce997cd4bb7190d4'
        token_address = '0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9'  # AAVE
        t = Token(
            url=self.url,
            wallet_address=wallet_address,
            token_address=token_address,
        )
        balance = t.get_balance()
        assert balance == '31.13087903404498'


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

