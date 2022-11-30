#! /usr/bin/env python3
import json
import os
import click
from tartarus import constants
from tartarus.config import Config
from tartarus.print import Print

config = Config()

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def get_config():
    """Get config"""
    config_data = config.get_config()

    Print.print_success("URL: " + config_data["url"])
    print("")
    Print.print_success("Keypair Path: " + config_data["keypair_path"])
    print("")


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-u', '--url', 'url', help="RPC URL")
@click.option('-k', '--keypair-file', 'keypair_file', help="Keypair file name")
def set_config(url: str, keypair_file: str):
    """Set config"""
    if url is None and keypair_file is None: 
        with click.Context(set_config) as ctx:
           click.echo(set_config.get_help(ctx))
    else:
        success = config.set_config(url, keypair_file)

        if success:
            Print.print_success("Config updated")
            print("")

@click.group()
def config_command():
    """config for wallet"""
    pass

config_command.add_command(get_config, "get")
config_command.add_command(set_config, "set")
