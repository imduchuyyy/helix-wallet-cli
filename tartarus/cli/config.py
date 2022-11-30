#! /usr/bin/env python3
import json
import os
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

    config_json = config.get_config()
    if url is not None:
        print(constants.BOLD + "RPC Url: " + constants.CEND, end='')
        print(url)
        config_json["url"] = url
    if keypair_file is not None:
        print(constants.BOLD + "Keypair path: " + constants.CEND, end='')
        print(keypair_file)
        config_json["keypair_path"] = keypair_file

    config_path = os.path.join(constants.wallet_path, "config.json")
    with open(config_path, "w+") as f:
        f.write(json.dumps(config_json, indent = 4))

    print(constants.BOLD + "Config updated" + constants.CEND, end='')


@click.group()
def config_command():
    """config for wallet"""
    pass


config_command.add_command(get_config, "get")
config_command.add_command(set_config, "set")
