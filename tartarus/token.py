#! /usr/bin/env python3
from tartarus import constants
from web3 import Web3
from tartarus.constants import ETH_NATIVE_ADDRESS


def to_checksum_address(address):
    return Web3.toChecksumAddress(address)


class Token(object):
    def __init__(self, url, wallet_address, token_address, **kwargs) -> None:
        self.w3 = kwargs.get("w3", None)
        self.wallet_address = to_checksum_address(wallet_address)
        self.token_address = to_checksum_address(token_address)

        self._build_w3(url)

    def _build_w3(self, url) -> None:
        if self.w3 is None:
            self.w3 = Web3(Web3.HTTPProvider(url))

    def get_balance(self) -> str:
        if self.token_address == ETH_NATIVE_ADDRESS:
            balance = self.w3.eth.get_balance(self.wallet_address)
            balance = str(float(balance) / 10 ** 18)
        else:
            token = self.w3.eth.contract(address=self.token_address, abi=constants.ERC20_ABI)
            balance = token.functions.balanceOf(self.wallet_address).call()
            balance = str(balance / 10 ** self.get_decimal())
        return balance

    def get_symbol(self) -> str:
        if self.token_address == ETH_NATIVE_ADDRESS:
            return "ETH"
        else:
            token = self.w3.eth.contract(address=self.token_address, abi=constants.ERC20_ABI)
            return token.functions.symbol().call()

    def get_decimal(self) -> int:
        if self.token_address == ETH_NATIVE_ADDRESS:
            return 18
        else:
            token = self.w3.eth.contract(address=self.token_address, abi=constants.ERC20_ABI)
            return token.functions.decimals().call()
