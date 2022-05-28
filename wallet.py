#!/usr/bin/env python3

import web3
import os
from os import walk
import sys
import secrets
from docopt import docopt
from getpass import getpass
from constants import *
from helper import *

def print_hello_text():
    type_writer(BOLD + GRN + "\n   [ Mini Cool Wallet ] - by @terry.h \n" + CEND + "\n", 0.01)

def get_wallets_handler():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filenames = next(walk(dir_path), (None, None, []))[2]

    keypairs = [filename for filename in filenames if ".keypair" in filename ]

    if len(keypairs) == 0:
        type_writer(BOLD + CRED + "\n ❌ No Wallet" + CEND + "\n", 0.01)
        return

    type_writer(BOLD + CYELLOW + "\n > List Wallet:" + CEND + "\n", 0.01)

    for i, wallet_file in enumerate(keypairs):
        print(BOLD + CBLINK + "\n > Wallet " + str(i + 1) + ":" + CEND, end='')
        type_writer(BOLD + CYELLOW + get_wallet_address_from_file_name(wallet_file) + CEND, 0.01)

def new_wallet_handler():
    type_writer(BOLD + CYELLOW + "\n > Create New Wallet" + CEND , 0.01)
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    account = Account.from_key(private_key)
    print(BOLD + CBLINK + "\n > New Wallet: ", end='')

    type_writer(account.address + "\n", 0.01)
    type_writer("\n > Enter Password:" + CEND, 0.01)

    password = getpass("")
    
    type_writer(BOLD + CBLINK + "> Confirm Password:" + CEND, 0.01)

    confirm_password = getpass("")

    if password != confirm_password: 
        type_writer(BOLD + CRED + "\n ❌ Password does not match" + CEND, 0.01)
        return

    create_new_key(private_key, password)

    type_writer(BOLD + GRN + "\n   New Wallet Created !!! \n" + CEND + "\n", 0.01)


def transfer_handler():
    type_writer(BOLD + CYELLOW + "\n > Transfer" + CEND + "\n", 0.01)

def main():
    print_hello_text()

    arguments = docopt(doc, argv=None, help=True, options_first=False)
    if arguments["new"]: 
        new_wallet_handler()
    if arguments["list"]:
        get_wallets_handler()
    if arguments["transfer"]:
        transfer_handler()

    print("")

main()
