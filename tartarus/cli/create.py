#! /usr/bin/env python3
import click
import os
from getpass import getpass
from tartarus.wallet import Wallet
from tartarus.config import Config
from tartarus.print import Print
from tartarus.constants import PrintType

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

    Print()._out("Private key (default for new wallet): ")
    private_key = getpass("")
    
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
        new_address = wallet.create_wallet(private_key, password, True)

        Print(PrintType.SUCCESS)._out("Create new wallet with address " + new_address)
        print("")

