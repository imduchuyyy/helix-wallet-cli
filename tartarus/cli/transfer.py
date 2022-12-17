#! /usr/bin/env python3
import click
from tartarus.config import Config 
from tartarus.wallet import Wallet 
from tartarus.print import Print
from tartarus.token import Token
from tartarus.constants import ETH_NATIVE_ADDRESS, PrintType

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument("receiver", type=str)
@click.argument("amount", type=float)
@click.option('-t', '--token-address', 'token_address', help="Token Address", default="Native token", show_default=True)
def transfer_handler(receiver: str, amount: float, token_address: str):
    """config for wallet"""
    config = Config()
    wallet = Wallet(config.get_keypair_path())

    if not wallet.is_wallet_exited():
        Print(PrintType.ERROR)._out("Wallet not found, please create wallet first")
        print("")

        quit()

    if token_address == "Native token":
        token_address = ETH_NATIVE_ADDRESS  

    token = Token(config.get_url(), wallet.get_address(), token_address)
    transaction = token.create_transfer_transaction(receiver, amount)
    print(transaction)
