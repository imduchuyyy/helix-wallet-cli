#! /usr/bin/env python3
import click
from tartarus.config import Config 
from tartarus.wallet import Wallet 
from tartarus.print import Print

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def get_address():
    """get address"""
    config = Config()
    wallet = Wallet(config.get_keypair_path())

    if not wallet.is_wallet_exited():
        Print.print_error("Wallet not found, please create wallet first")
        print("")

        quit()

    address = wallet.get_address()

    Print.print_success(address)
    print("")
