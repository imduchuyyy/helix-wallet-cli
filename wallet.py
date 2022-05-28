#!/usr/bin/env python3

import web3
from eth_account import Account
import os
import sys
import secrets
from docopt import docopt
from getpass import getpass
from constants import *
from helper import *
import json

def print_hello_text():
    type_writer(BOLD + GRN + "\n   [ Mini Cool Wallet ] - by @terry.h \n" + CEND + "\n", 0.01)

def get_address_handler():
    type_writer(BOLD + CYELLOW + "\n > Get Address" + CEND + "\n", 0.01)

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

    account_json = {
        "address": account.address,
        "encrypted_key": private_key
    }

    json_object = json.dumps(account_json, indent = 4)

    with open(account.address + ".keypair" + ".json", "w") as outfile:
        outfile.write(json_object)



def transfer_handler():
    type_writer(BOLD + CYELLOW + "\n > Transfer" + CEND + "\n", 0.01)

def main():
    print_hello_text()

    arguments = docopt(doc, argv=None, help=True, options_first=False)
    if arguments["new"]: 
        new_wallet_handler()
    if arguments["address"]:
        get_address_handler()
    if arguments["transfer"]:
        transfer_handler()

main()
