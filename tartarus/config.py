#! /usr/bin/env python3
import os
import json
from .constants import *

default_config = {
        "keypair_path": wallet_path + "/wallet" + "/id.json",
        "url": "https://mainnet.infura.io/v3/9e4bc49c44c34ac7ae3e5c34fe5e1d62"
        }

def create_default_config(path: str) -> None:
    with open(path, "w+") as f:
        f.write(json.dumps(default_config, indent = 4))

def check_config_exited():
    config_path = os.path.join(wallet_path, 'config.json')
    if not os.path.isfile(config_path):
        create_default_config(config_path)

def get_config() -> dict:
    config_path = os.path.join(wallet_path, "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)

    return config

def get_keypair_path() -> str:
    config = get_config()
    return config["keypair_path"]

def get_url() -> str:
    config = get_config()
    return config["url"]

def print_config() -> None:
    check_config_exited()
    config = get_config()
    keypair_path = config["keypair_path"]
    url = config["url"]

    print(BOLD + "Keypair path: " + CEND, end='')
    print(keypair_path)
    print(BOLD + "RPC Url: " + CEND, end='')
    print(url)
    pass

