import os
from tartarus import constants

def set_up():
    if not os.path.exists(constants.wallet_path):
        os.makedirs(constants.wallet_path)

    if not os.path.exists(constants.wallet_list_path):
        os.makedirs(constants.wallet_list_path)

set_up()
