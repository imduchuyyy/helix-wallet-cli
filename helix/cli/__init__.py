#!/usr/bin/env python3

import click
from helix.cli.config import config_command
from helix.cli.info import info_command
from helix.cli.create import create_wallet
from helix.cli.tornado import tornado_command
from helix.cli.transfer import transfer_handler
from helix.cli.balance import balance_handler

__version__ = "0.1.0"

@click.group()
@click.version_option(version = __version__)
@click.pass_context
def cli(ctx):
    """Helix wallet: By developer for developers"""
    pass

cli.add_command(config_command, "config")
cli.add_command(info_command, "info")
cli.add_command(create_wallet, "create")
cli.add_command(tornado_command, "tornado")
cli.add_command(transfer_handler, "transfer")
cli.add_command(balance_handler, "balance")
