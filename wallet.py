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

def check_wallet():
    if not is_exist_wallet():
        type_writer(BOLD + CRED + "\tNo Wallet Found" + CEND + "\n", 0.01)
        return False
    return True


def print_hello_text():
    print(BOLD + CCYAN + "\t\t\t\t----------------------------------------" + CEND)
    print(BOLD + CCYAN + "\t\t\t\t-                                      -" + CEND)
    print(BOLD + CCYAN + "\t\t\t\t-  [" + CEND, end="")
    type_writer(BOLD + GRN + "Mini Cool Wallet" + CEND, 0.03)
    print(BOLD + CCYAN + "] - by" + CEND, end="")
    type_writer(BOLD + CRED + "@Terry.h" + CEND, 0.03)
    print(BOLD + CCYAN + " -" + CEND)
    print(BOLD + CCYAN + "\t\t\t\t-                                      -" + CEND)
    print(BOLD + CCYAN + "\t\t\t\t----------------------------------------" + CEND)

def get_wallet_handler():
    try:
        wallet = get_wallet_encrypt()
        checksum_address = to_checksum_address("0x" + wallet["address"])
        print(BOLD + CYELLOW + "\tWallet Address: ", end='')
        type_writer(BOLD + GRN + checksum_address  + CEND + "\n", 0.01)
    except:
        type_writer(BOLD + CRED + "\tNo Wallet Found" + CEND + "\n", 0.01)
        return


def new_wallet_handler():
    type_writer(BOLD + CYELLOW + "\tCreate New Wallet\n" + CEND , 0.01)
    priv = secrets.token_hex(32) 
    private_key = "0x" + priv
    account = Account.from_key(private_key)
    print(BOLD + CBLINK + "\t\tNew Wallet: ", end='')

    type_writer(account.address, 0.01)

    print("\n\t\t> Enter Password: " + CEND, end='')
    password = getpass("")

    print(BOLD + CBLINK + "\n\t\t> Confirm Password: " + CEND, end='')
    confirm_password = getpass("")

    if password != confirm_password: 
        type_writer(BOLD + CRED + "\n\tPassword does not match\n" + CEND, 0.01)
        return

    create_new_key(private_key, password)

    type_writer(BOLD + GRN + "\n\tNew Wallet Created !!! \n" + CEND + "\n", 0.01)

def print_token_info(token_info):
    type_writer(BOLD + CYELLOW + "\n\t\tToken Found:" + CEND + "\n", 0.01)
    print("\t\t\tToken Address: ", end="")
    type_writer(BOLD + GRN + token_info["address"] + CEND + "\n", 0.01)
    print("\t\t\tToken Name: ", end="")
    type_writer(BOLD + GRN + token_info["name"] + CEND + "\n", 0.01)
    print("\t\t\tToken Symbol: ", end="")
    type_writer(BOLD + GRN + token_info["symbol"] + CEND + "\n", 0.01)
    print("\t\t\tToken Decimals: ", end="")
    type_writer(BOLD + GRN + token_info["decimals"] + CEND + "\n", 0.01)
    print("\t\t\tBalance: ", end="")
    if float(token_info["balance"]) > 0: 
        type_writer(BOLD + GRN + token_info["balance"] + CEND + "\n", 0.01)
    else: 
        type_writer(BOLD + CRED + token_info["balance"] + CEND + "\n", 0.01)

def unlock_wallet(wallet):
    is_correct_password = False

    while not is_correct_password: 
        print(BOLD + CYELLOW + "\n\t\t> Enter password: " + CEND , end='')
        password = getpass("")
        try:
            key = decrypt_wallet(wallet, password)
            is_correct_password = True
        except:
            type_writer(BOLD + CRED + "\t\tWrong password" + CEND, 0.01)

    return key


def transfer_handler():
    if not check_wallet():
        return
    type_writer(BOLD + CYELLOW + "\tTransfer Token" + CEND, 0.01)

    print(BOLD + CYELLOW + "\n\t\t> Token Address (Default is Native token): " + CEND, end='')
    token_address = input()

    wallet = get_wallet_encrypt()

    type_writer(BOLD + CYELLOW +   "\n\t\tFetching Token Info ... " + CEND , 0.01)
    checksum_address = to_checksum_address("0x" + wallet["address"])

    try:
        token_info = get_token_info(checksum_address, token_address)
        print_token_info(token_info)
    except: 
        print(BOLD + CRED + "\n\t\tToken Not Found")
        return


    print(BOLD + CYELLOW + "\n\t\t> Receiver Address: " + CEND, end='')
    receiver_address = input()

    print(BOLD + CYELLOW + "\t\t> Amount: " + CEND , end='')
    amount = input()

    key = unlock_wallet(wallet)

    try:
        if len(token_address) == 0:
            hash = transfer_eth(checksum_address, key, receiver_address, float(amount))
        else:
            hash = transfer_token(token_info, checksum_address, key, receiver_address, float(amount))
        print(BOLD + GRN + "\n\t\t\tTransaction Success: ", end="")
        type_writer(BOLD + GRN + str(hash.hex()) + CEND + "\n", 0.01)
    except Exception as e:
        print(BOLD + CRED + "\n\t\t\tTransaction Fail: ", end="")
        type_writer(BOLD + CRED + str(e) + CEND + "\n", 0.01)


def main():
    print_hello_text()

    if not check_wallet():
        new_wallet_handler()

    while True:
        print (BOLD + CYELLOW + ">> " + CEND, end="")
        action = input()

        if action == "address":
            get_wallet_handler()
        elif action == "reset":
            new_wallet_handler()
        elif action == "transfer":
            transfer_handler()
        elif len(action) > 0:
            print(BOLD + CYELLOW + doc, end="")

    print("")

main()
