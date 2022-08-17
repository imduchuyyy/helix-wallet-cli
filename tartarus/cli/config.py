#! /usr/bin/env python3
import click
from tartarus import config, constants

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def get_config():
    """Get config"""
    config.print_config()

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-u', '--url', 'url', help="RPC URL")
@click.option('-k', '--keypair-file', 'keypair_file', help="Keypair file name")
def set_config(url: str, keypair_file: str):
    """Set config"""
    if url is None and keypair_file is None: 
        with click.Context(set_config) as ctx:
            click.echo(set_config.get_help(ctx))

@click.group()
def config_command():
    """config for wallet"""
    pass

config_command.add_command(get_config, "get")
config_command.add_command(set_config, "set")
