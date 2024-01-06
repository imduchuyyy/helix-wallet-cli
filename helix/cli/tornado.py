#!/usr/bin/env python3
import click

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def deposit():
    """deposit to tornado cash"""
    pass

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def withdraw():
    """withdraw from tornado cash"""
    pass

@click.group()
def tornado_command():
    """tornado cash"""
    pass

tornado_command.add_command(deposit, "deposit")
tornado_command.add_command(withdraw, "withdraw")
