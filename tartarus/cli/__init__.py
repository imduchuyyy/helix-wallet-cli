#!/usr/bin/env python3

import click
import os

from tartarus.cli.config import config_command
from tartarus.cli.address import get_address
from tartarus.cli.transfer import do_transfer
from tartarus.cli.create import create_keypair
from tartarus.cli.tornado import tornado_command

__version__ = "0.1.0"

@click.group()
@click.version_option(version = __version__)
@click.pass_context
def cli(ctx):
    """Tartarus wallet: Micro wallet by Terry"""
    pass

cli.add_command(config_command, "config")
cli.add_command(get_address, "address")
cli.add_command(do_transfer, "transfer")
cli.add_command(create_keypair, "create")
cli.add_command(tornado_command, "tornado")
