#!/usr/bin/env python3

import sys, time
from eth_account import Account
import json

def type_writer(message, delay_time):
    for char in message:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(delay_time)

def create_new_key(private_key, password):
    account = Account.from_key(private_key)
    encrypted_key = Account.encrypt(private_key, password = password)

    json_object = json.dumps(encrypted_key, indent = 4)

    with open(account.address + ".keypair" + ".json", "w") as outfile:
        outfile.write(json_object)

def get_wallet_address_from_file_name(name):
    return name.split(".")[0]
