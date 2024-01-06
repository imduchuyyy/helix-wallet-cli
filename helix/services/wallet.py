#! /usr/bin/env python3
import os 
from eth_account import Account
import secrets
import json
from bip_utils import Bip44, Bip44Coins, Bip44Changes, Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum
from helix import config, constants, helper
from helix.print import Print
from helix.services.cryptography import Cryptography

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
    

    def create_wallet(self, mnemonic: str, password: str, is_override: bool) -> str:
        if len(mnemonic) < 1:
            mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
            mnemonic = " ".join(mnemonic.ToList())
        
        encrypted_mnemonic = Cryptography.encrypt_mnemonic(mnemonic, password)
        print(encrypted_mnemonic)
        # account = Account.from_key(private_key)
        # json_object = json.dumps(encrypted_key, indent = 4)
        # with open(self.keypair_path, "w+") as outfile:
        #     outfile.write(json_object)

        
        return ""
        # return account.address
    
    def sign_and_send_transaction(self, transaction: dict) -> str: 
        pass
