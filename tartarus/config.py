#! /usr/bin/env python3
import os
import json
from tartarus import constants

default_config = {
    "keypair_path": constants.WALLET_PATH + "/wallet" + "/id.json",
    "url": "https://mainnet.infura.io/v3/9e4bc49c44c34ac7ae3e5c34fe5e1d62"
}

class Config():
    def __init__(self):
        config_path = os.path.join(constants.WALLET_PATH, "config.json")
        with open(config_path, "r") as f:
            self.config = json.load(f)

    def get_config(self):
        return self.config

    def set_config(self, url: str, keypair_file: str):
        config = self.config
        if url is not None:
            print(constants.BOLD + "URL: " + constants.CEND, end='')
            print(url)
            config["url"] = url
        if keypair_file is not None:
            print(constants.BOLD + "Keypair file: " + constants.CEND, end='')
            print(keypair_file)
            config["keypair_path"] = keypair_file

        config_path = os.path.join(constants.WALLET_PATH, "config.json")
        with open(config_path, "w+") as f:
            f.write(json.dumps(config, indent = 4))

        return True
        print(constants.BOLD + "Config updated" + constants.CEND, end='')


    def create_default_config(path: str) -> None:
        with open(path, "w+") as f:
            f.write(json.dumps(default_config, indent = 4))

    def check_config_exited():
        config_path = os.path.join(wallet_path, 'config.json')
        if not os.path.isfile(config_path):
            create_default_config(config_path)

    def is_wallet_exited() -> bool:
        config_path = os.path.join(wallet_path, self.config["keypair_path"])
        if not os.path.isfile(config_path):
            False
        else:
            True

    def get_keypair_path(self) -> str:
        return self.config["keypair_path"]

    def get_url(self) -> str:
        config = self.get_config()
        return self.config["url"]

    def print_config(self) -> None:
        keypair_path = self.config["keypair_path"]
        url = self.config["url"]

        print(constants.BOLD + "Keypair path: " + constants.CEND, end='')
        print(keypair_path)
        print(constants.BOLD + "RPC Url: " + constants.CEND, end='')
        print(url)
        pass

