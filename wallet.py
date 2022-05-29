#!/usr/bin/env python3

from web3 import Web3
import os, time
from os import walk
import sys
import secrets
from getpass import getpass
from constants import *
from helper import *

def check_wallet():
    if not is_exist_wallet():
        type_writer(BOLD + CRED + "\tWallet Not Found" + CEND + "\n", NORMAL_TEXT_TIME)
        return False
    return True


def print_header_text():
    print(BOLD + CCYAN + "\t\t\t----------------------------------------" + CEND)
    print(BOLD + CCYAN + "\t\t\t-                                      -" + CEND)
    print(BOLD + CCYAN + "\t\t\t-  " + CEND, end="")
    type_writer(GRN + "[ Mini Cool Wallet ]" + CEND, HEADER_TEXT_TIME)
    type_writer(BOLD + CCYAN+ "- by " + CEND, HEADER_TEXT_TIME)
    type_writer(CRED + "@Terry.h" + CEND, HEADER_TEXT_TIME)
    print(BOLD + CCYAN + " -" + CEND)
    print(BOLD + CCYAN + "\t\t\t-                                      -" + CEND)
    print(BOLD + CCYAN + "\t\t\t----------------------------------------" + CEND)

def print_footer_text():
    type_writer(BOLD + CCYAN + "\tDonate ♥ " + CEND, FOOTER_TEXT_TIME)
    type_writer(BOLD + CRED + "0x094C569ed04f3d93Ac8656e5cf2522381E24D57D" + CEND, FOOTER_TEXT_TIME)

def get_wallet_handler():
    try:
        wallet = get_wallet_encrypt()
        checksum_address = to_checksum_address("0x" + wallet["address"])
        print(BOLD + CYELLOW + "\tWallet Address: " + CEND, end='')
        type_writer(GRN + checksum_address  + CEND + "\n", NORMAL_TEXT_TIME)
    except:
        type_writer(BOLD + CRED + "\tNo Wallet Found" + CEND + "\n", NORMAL_TEXT_TIME)
        return


def new_wallet_handler():
    type_writer(BOLD + CYELLOW + "\tCreate New Wallet\n" + CEND , NORMAL_TEXT_TIME)
    priv = secrets.token_hex(32) 
    private_key = "0x" + priv
    account = Account.from_key(private_key)
    print(BOLD + CBLINK + "\t\tNew Wallet: " + CEND, end='')

    type_writer(account.address, NORMAL_TEXT_TIME)

    print(BOLD + CYELLOW + "\n\t\t> " + CEND + BOLD + CBLINK + "Enter Password: ", end='')
    password = getpass("")

    print(BOLD + CYELLOW + "\n\t\t> " + CEND + BOLD + CBLINK + "Confirm Password: ", end='')
    confirm_password = getpass("")

    if password != confirm_password: 
        type_writer(BOLD + CRED + "\n\tPassword does not match\n" + CEND, NORMAL_TEXT_TIME)
        return

    create_new_key(private_key, password)

    type_writer(BOLD + GRN + "\n\tNew Wallet Created !!! \n" + CEND + "\n", NORMAL_TEXT_TIME)

def print_token_info(token_info):
    type_writer(BOLD + CYELLOW + "\n\t\tToken Found:" + CEND + "\n", NORMAL_TEXT_TIME)
    print(BOLD + "\t\t\tToken Address: " + CEND, end="")
    type_writer(GRN + token_info["address"] + CEND + "\n", NORMAL_TEXT_TIME)
    print(BOLD + "\t\t\tToken Name: " + CEND, end="")
    type_writer(GRN + token_info["name"] + CEND + "\n", NORMAL_TEXT_TIME)
    print(BOLD + "\t\t\tToken Symbol: " + CEND, end="")
    type_writer(GRN + token_info["symbol"] + CEND + "\n", NORMAL_TEXT_TIME)
    print(BOLD + "\t\t\tToken Decimals: " + CEND, end="")
    type_writer(GRN + token_info["decimals"] + CEND + "\n", NORMAL_TEXT_TIME)
    print(BOLD + "\t\t\tBalance: " + CEND, end="")
    if float(token_info["balance"]) > 0: 
        type_writer(GRN + token_info["balance"] + CEND + "\n", NORMAL_TEXT_TIME)
    else: 
        type_writer(CRED + token_info["balance"] + CEND + "\n", NORMAL_TEXT_TIME)

def unlock_wallet(wallet):
    is_correct_password = False

    while not is_correct_password: 
        print(BOLD + CYELLOW + "\n\t\t> " + CEND + BOLD + CBLINK + "Enter Password: " + CEND, end='')
        password = getpass("")
        try:
            key = decrypt_wallet(wallet, password)
            is_correct_password = True
        except:
            type_writer(BOLD + CRED + "\t\tWrong password" + CEND, NORMAL_TEXT_TIME)

    return key


def transfer_handler():
    if not check_wallet():
        return
    type_writer(BOLD + CYELLOW + "\tTransfer Token" + CEND, NORMAL_TEXT_TIME)

    print(BOLD + CYELLOW + "\n\t\t> " + CEND + BOLD + CBLINK + "Token Address (Default is Native token): " + CEND, end='')
    token_address = input()

    wallet = get_wallet_encrypt()

    type_writer(BOLD + CYELLOW +   "\n\t\tFetching Token Info ... " + CEND , NORMAL_TEXT_TIME)
    checksum_address = to_checksum_address("0x" + wallet["address"])

    try:
        token_info = get_token_info(checksum_address, token_address)
        print_token_info(token_info)
    except: 
        print(BOLD + CRED + "\n\t\tToken Not Found")
        return


    print(BOLD + CYELLOW + "\n\t\t> " + CEND + BOLD + CBLINK + "Receiver Address: " + CEND, end='')
    receiver_address = input()

    print(BOLD + CYELLOW + "\n\t\t> " + CEND + BOLD + CBLINK + "Amount: " + CEND, end='')
    amount = input()

    key = unlock_wallet(wallet)

    try:
        if len(token_address) == 0:
            hash = transfer_eth(checksum_address, key, receiver_address, float(amount))
        else:
            hash = transfer_token(token_info, checksum_address, key, receiver_address, float(amount))
        print(BOLD + GRN + "\n\t\t\tTransaction Success: " + CEND, end="")
        type_writer(GRN + str(hash.hex()) + CEND + "\n", NORMAL_TEXT_TIME)
    except Exception as e:
        print(BOLD + CRED + "\n\t\t\tTransaction Fail: " + CEND, end="")
        type_writer(CRED + str(e) + CEND + "\n", NORMAL_TEXT_TIME)


def main():
    print_header_text()
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
        elif action == "exit":
            break
        elif len(action) > 0:
            print(BOLD + CYELLOW + doc, end="")

    print_footer_text()
    print("")
    
main()
