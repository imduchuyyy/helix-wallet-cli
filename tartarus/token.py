#! /usr/bin/env python3
from tartarus import constants
from web3 import Web3
import web3

def to_checksum_address(address):
    return Web3.toChecksumAddress(address)

class Token():
    def __init__(self, url, wallet_address, token_address):
        provider = Web3.HTTPProvider(url)
        self.w3 = Web3(provider)
        self.wallet_address = to_checksum_address(wallet_address)
        self.token_address = to_checksum_address(token_address)

    def get_balance(self) -> str:
        if self.token_address == "0x0000000000000000000000000000000000000000":
            balance = str(float(self.w3.eth.get_balance(self.wallet_address)) / 10 ** 18)
        else:
            token = self.w3.eth.contract(address=self.token_address, abi=constants.ERC20_ABI)
            balance = str(token.functions.balanceOf(self.wallet_address).call() / 10 ** self.get_decimal())

        return balance
    
    def get_symbol(self) -> str:
        if self.token_address == "0x0000000000000000000000000000000000000000":
            return "ETH"
        else:
            token = self.w3.eth.contract(address=self.token_address, abi=constants.ERC20_ABI)
            return token.functions.symbol().call()

    def get_decimal(self) -> int:
        if self.token_address == "0x0000000000000000000000000000000000000000":
            return 18
        else:
            token = self.w3.eth.contract(address=self.token_address, abi=constants.ERC20_ABI)
            return token.functions.decimals().call()
