#! /usr/bin/env python3
import click

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument("receiver", type=str)
@click.argument("amount", type=float)
@click.option('-t', '--token-address', 'token_address', help="Token Address", default="Native token", show_default=True)
def transfer_handler(receiver: str, amount: float, token_address: str):
    """config for wallet"""
