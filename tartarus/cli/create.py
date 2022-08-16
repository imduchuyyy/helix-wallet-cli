#! /usr/bin/env python3
import click
import os
from tartarus import wallet, config

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-o', '--keypair-file', 'keypair_file', help="keypair file name")
@click.option('-f', '--force', 'force', help="force overwrite wallet", is_flag=True)
@click.option('-k', '--private-key', 'private_key', help="private key")
def create_keypair(keypair_file: str, force: bool, private_key: str):
    """create new keypair"""
    if keypair_file is None and not force:
        keypair_path = config.get_keypair_path()
        if os.path.isfile(keypair_path):
            click.echo("Refusing to overwrite " + keypair_path+ " without --force flag")
            exit()

    if private_key is None:
        private_key = click.prompt('Private key (empty for none)', type=str, default="", show_default=False)

    password = click.prompt('Password', hide_input=True, type=str, default="", show_default=False)
    confirm = click.prompt('Confirm Password', hide_input=True, type=str, default="", show_default=False)

    if password != confirm:
        click.echo("Password mismatch")
        exit()

    wallet.create_keypair(keypair_file, private_key, password)
    
