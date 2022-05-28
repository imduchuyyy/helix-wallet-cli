#!/usr/bin/env python3

from web3 import Web3
import os, time
from os import walk
import sys
import secrets
from docopt import docopt
from getpass import getpass
from constants import *
from helper import *

def print_hello_text():
    print(BOLD + GRN + "\n   [ Mini Cool Wallet ] - by @terry.h \n" + CEND)

def get_wallet_handler():
    try:
        wallet = get_wallet_encrypt()
        checksum_address = to_checksum_address("0x" + wallet["address"])
        print(BOLD + CBLINK + "Wallet Found: ", end='')
        type_writer(BOLD + CYELLOW + checksum_address  + CEND + "\n", 0.01)
    except:
        type_writer(BOLD + CRED + "\n ❌ No Wallet" + CEND + "\n", 0.01)
        return


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

def print_token_info(token_info):
    type_writer(BOLD + CYELLOW + "\n > Token Found:" + CEND + "\n", 0.01)
    print("       > Token Address: ", end="")
    type_writer(BOLD + CYELLOW + token_info["address"] + CEND + "\n", 0.01)
    print("       > Token Name: ", end="")
    type_writer(BOLD + CYELLOW + token_info["name"] + CEND + "\n", 0.01)
    print("       > Token Symbol: ", end="")
    type_writer(BOLD + CYELLOW + token_info["symbol"] + CEND + "\n", 0.01)
    print("       > Token Decimals: ", end="")
    type_writer(BOLD + CYELLOW + token_info["decimals"] + CEND + "\n", 0.01)
    print("       > Balance: ", end="")
    if float(token_info["balance"]) > 0: 
        type_writer(BOLD + CYELLOW + token_info["balance"] + CEND + "\n", 0.01)
    else: 
        type_writer(BOLD + CRED + token_info["balance"] + CEND + "\n", 0.01)

def unlock_wallet(wallet):
    is_correct_password = False

    while not is_correct_password: 
        type_writer(BOLD + CYELLOW + "\n > Enter password: " + CEND , 0.01)
        password = getpass("")
        try:
            key = decrypt_wallet(wallet, password)
            is_correct_password = True
        except:
            type_writer(BOLD + CRED + "❌ Wrong password" + CEND, 0.01)

    return key


def transfer_handler():
    type_writer(BOLD + CYELLOW + "> Transfer Token" + CEND + "\n", 0.01)

    type_writer(BOLD + CYELLOW + "\n > Token Address (Default is Native token): " + CEND , 0.01)
    token_address = input()

    wallet = get_wallet_encrypt()

    type_writer(BOLD + CCYAN + "\n > Fetching Token Info ... " + CEND , 0.01)
    checksum_address = to_checksum_address("0x" + wallet["address"])
    token_info = get_token_info(checksum_address, token_address)

    print_token_info(token_info)

    type_writer(BOLD + CYELLOW + "\n > Receiver Address: " + CEND , 0.01)
    receiver_address = input()

    type_writer(BOLD + CYELLOW + "> Amount: " + CEND , 0.01)
    amount = input()

    key = unlock_wallet(wallet)


    try:
        if len(token_address) == 0:
            hash = transfer_eth(checksum_address, key, receiver_address, float(amount))
        else:
            hash = transfer_token(token_info, checksum_address, key, receiver_address, float(amount))
        print(BOLD + GRN + "\n       Transaction Success: ", end="")
        type_writer(BOLD + GRN + str(hash.hex()) + CEND + "\n", 0.01)
    except e:
        print(e)
        type_writer(BOLD + CRED + "\n       ❌ Transaction Fail" + CEND, 0.01)


def main():
    print_hello_text()

    arguments = docopt(doc, argv=None, help=True, options_first=False)
    if arguments["new"]: 
        new_wallet_handler()
    if arguments["address"]:
        get_wallet_handler()
    if arguments["transfer"]:
        transfer_handler()

    print("")

main()
