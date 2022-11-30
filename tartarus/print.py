#! /usr/bin/env python3
from tartarus import constants

class Print():
    def print_error(message: str):
        print(constants.CRED + "Error: " + constants.CEND, end='')
        print(message, end="", flush=True)
        pass

    def print_success(message:str):
        print(constants.GRN + "Success: " + constants.CEND, end='')
        print(message, end="", flush=True)
        pass

    def print_info(message: str):
        print(constants.CCYAN + "Info: " + constants.CEND, end='')
        print(message, end="", flush=True)
        pass

    def print_warning(message: str):
        print(constants.CYELLOW + "Warning: " + constants.CEND, end='')
        print(message, end="", flush=True)
        pass
