#!/usr/bin/env python3

import sys, time, os
from os import walk
from eth_account import Account
import json
from web3 import Web3
import web3
from .constants import *

provider = Web3.HTTPProvider('https://mainnet.infura.io/v3/9e4bc49c44c34ac7ae3e5c34fe5e1d62')
w3 = Web3(provider)

def type_writer(message, delay_time):
    for char in message:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(delay_time)

    time.sleep(0.1)

def create_new_key(private_key, password):
    account = Account.from_key(private_key)
    encrypted_key = Account.encrypt(private_key, password = password)

    json_object = json.dumps(encrypted_key, indent = 4)

    with open(".keypair" + ".json", "w") as outfile:
        outfile.write(json_object)

def decrypt_wallet(wallet, password):
    decrypt_key = Account.decrypt(wallet, password)

    return decrypt_key

def get_wallet_encrypt():
    with open(".keypair.json", 'r') as openfile:
        wallet = json.load(openfile)
    return wallet

def get_wallet_address_from_file_name(name):
    return name.split(".")[0]

def get_wallet_by_index(index):
    wallets = get_wallets_list()
    return wallets[index - 1]

def to_checksum_address(address):
    return Web3.toChecksumAddress(address)


def get_token_info(wallet_address, token_address):
    token_info = {}

    if len(token_address) == 0:
        token_info["address"] = ETH_NATIVE_ADDRESS
        token_info["name"] = "Ethereum"
        token_info["symbol"] = "ETH"
        token_info["decimals"] = "18"
        token_info["balance"] = str(float(w3.eth.get_balance(wallet_address)) / 10 ** 18)

    else:
        token = w3.eth.contract(address=to_checksum_address(token_address), abi=ERC20_ABI)

        token_info["address"] = token_address
        token_info["name"] = str(token.functions.name().call())
        token_info["symbol"] = str(token.functions.symbol().call())
        token_info["decimals"] = str(token.functions.decimals().call())
        token_info["balance"] = str(token.functions.balanceOf(wallet_address).call() / 10 ** int(token_info["decimals"]))

    return token_info

def transfer_token(token_info, address, private_key, receiver_address, amount):
    token = w3.eth.contract(address=to_checksum_address(token_info["address"]), abi=ERC20_ABI)
    amount = int(amount * (10 ** int(token_info["decimals"])))
    nonce = w3.eth.getTransactionCount(address)

    transaction = token.functions.transfer(to_checksum_address(receiver_address), amount).buildTransaction({'nonce': nonce, 'gas': 70000, 'gasPrice': w3.toWei('10', 'gwei'),})

    signed_txn = w3.eth.account.signTransaction(transaction, private_key=private_key)
    w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    return signed_txn.hash

def transfer_eth(address, private_key, receiver_address, amount):
    nonce = w3.eth.getTransactionCount(address)
    tx = {
        'nonce': nonce,
        'to': to_checksum_address(receiver_address),
        'value': w3.toWei(amount, 'ether'),
        'gas': 2000000,
        'gasPrice': w3.toWei('10', 'gwei')
    }

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    return tx_hash

def is_exist_wallet():
    return os.path.exists(".keypair.json")

def print_result(title: str, message: str):
    print(BOLD + title + ": " + CEND, end='')
    print(message)
