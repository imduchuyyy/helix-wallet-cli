#! /usr/bin/env python3
import click
import os
from getpass import getpass
from helix.services.wallet import Wallet
from helix.config import Config
from helix.print import Print
from helix.constants import PrintType

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def create_wallet():
    """create new keypair"""
    config = Config()
    wallet = Wallet(config.get_keypair_path())

    if wallet.is_wallet_exited():
        Print(PrintType.WARNING)._out("Wallet existed, do you want to override (y/n): ")
        is_override = input()

        if is_override != 'y':
            quit()

    Print()._out("Mnemonic (default for new wallet): ")
    mnemonic = getpass("")
    
    Print()._out("Password (len >= 6): ")
    password = getpass("")

    while len(password) < 6:
        Print()._out("Password (len >= 6): ")
        password = getpass("")

    Print()._out("Confirm password: ")
    confirm_password = getpass("")

    if confirm_password != password:
        Print(PrintType.ERROR)._out("Password mismatch")
    else:
        new_address = wallet.create_wallet(mnemonic, password, True)

        Print(PrintType.SUCCESS)._out("Create new wallet with address " + new_address)
        print("")

