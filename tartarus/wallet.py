#! /usr/bin/env python3
import os 
from eth_account import Account
import secrets
import json
from tartarus import config, constants, helper


def get_address(keypair_path: str = None) -> str:
    if not keypair_path:
        keypair_path = config.get_keypair_path()
    with open(keypair_path, "r") as f:
        keypair_encrypted = json.load(f)
    return keypair_encrypted["address"]


def get_keypair(keypair_path: str) -> dict:
    # get keypair from file
    try: 
        with open(keypair_path, "r") as f:
            keypair = json.load(f)

        return keypair
    except:
        print("Keypair not exit")


def get_private_key(password: str = '') -> str:
    keypair_path = config.get_keypair_path()
    with open(keypair_path, "r") as f:
        keypair_encrypted = json.load(f)
    try:
        private_key = Account.decrypt(keypair_encrypted, password)
        return private_key
    except Exception as e:
        helper.print_result(message="Wrong password")
        exit()


def print_address() -> None:
    keypair_path = config.get_keypair_path()
    with open(keypair_path, "r") as f:
        keypair_encrypted = json.load(f)

    helper.print_result("address", "0x" + keypair_encrypted["address"])
    

def create_keypair(keypair_file: str = None, private_key: str = '', password: str = '') -> None:
    if keypair_file is None:
        keypair_file = config.get_keypair_path()
    if len(private_key) < 32:
        private_key = "0x" + secrets.token_hex(32)

    account = Account.from_key(private_key)
    encrypted_key = Account.encrypt(private_key, password = password)
    json_object = json.dumps(encrypted_key, indent = 4)
    with open(keypair_file, "w+") as outfile:
        outfile.write(json_object)

    helper.print_result("New keypair for address", account.address)
