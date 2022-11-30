#! /usr/bin/env python3
import os 
from eth_account import Account
import secrets
import json
from tartarus import config, constants, helper
from tartarus.print import Print

class Wallet():
    def __init__(self, keypair_path: str):
        self.keypair_path = keypair_path

    def load_keypair_encrypted(self):
        with open(self.keypair_path, "r") as f:
            keypair_encrypted = json.load(f)

        return keypair_encrypted

    def is_wallet_exited(self) -> bool:
        if not os.path.isfile(self.keypair_path):
            return False
        else:
            return True

    def get_address(self):
        keypair_encrypted = self.load_keypair_encrypted()

        return "0x" + keypair_encrypted["address"]
    

    def create_wallet(self, private_key: str, password: str, is_override: bool) -> str:
        if len(private_key) < 32:
            private_key = "0x" + secrets.token_hex(32)

        account = Account.from_key(private_key)
        encrypted_key = Account.encrypt(private_key, password = password)
        json_object = json.dumps(encrypted_key, indent = 4)
        with open(self.keypair_path, "w+") as outfile:
            outfile.write(json_object)

        
        return account.address

def get_keypair(keypair_path: str) -> dict:
    try: 
        with open(keypair_path, "r") as f:
            keypair = json.load(f)

        return keypair
    except:
        print("Keypair not exit")

def print_address() -> None:
    keypair_path = config.get_keypair_path()
    with open(keypair_path, "r") as f:
        keypair_encrypted = json.load(f)

    helper.print_result("address", "0x" + keypair_encrypted["address"])
    

def create_keypair(keypair_file: str, private_key: str, password: str):
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
