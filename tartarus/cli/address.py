#! /usr/bin/env python3
import click
from tartarus import wallet

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def get_address():
    """get address"""
    wallet.print_address()
