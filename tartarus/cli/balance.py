#! /usr/bin/env python3
import click
from tartarus.config import Config
from tartarus.constants import ETH_NATIVE_ADDRESS
from tartarus.wallet import Wallet 
from tartarus.print import Print
from tartarus.token import Token

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-t', '--token-address', 'token_address', help="Token address", default="Native token", show_default=True)
def balance_handler(token_address: str):
    """get balance"""
    config = Config()
    wallet = Wallet(config.get_keypair_path())

    if not wallet.is_wallet_exited():
        Print.print_error("Wallet not found, please create wallet first")
        print("")

        quit()

    if token_address == "Native token":
        token_address = ETH_NATIVE_ADDRESS

    token = Token(config.get_url(), wallet.get_address(), token_address)

    balance = token.get_balance()
    symbol = token.get_symbol()
    Print._out(message=balance + " " + symbol)
    print("")
