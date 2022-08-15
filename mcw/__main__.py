#! /usr/bin/env python3

"""
MCW: Create micro wallet
"""

import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

module_name = "Micro cool wallet: Micro wallet by Terry"
__version__ = "0.1.0"

if __name__ == "__main__":
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 6):
        print("Mcs requires Python 3.6+\nYou are using Python %s, which is not supported by Mcs" % (python_version))
        sys.exit(1)

    version_string = f"%(prog)s {__version__}\n"

    if sys.version_info < (3, 6):
        print("Sherlock requires Python 3.6+\nYou are using Python %s, which is not supported by Sherlock" % (python_version))
        sys.exit(1)

    parser = ArgumentParser(prog='PROG',formatter_class=RawDescriptionHelpFormatter, description=f"{module_name} (Version {__version__})")

    parser.add_argument("--version",
                        action="version", version=version_string,
                        help="Display version information and dependencies.")

    sub_parsers = parser.add_subparsers()

    parser_config = sub_parsers.add_parser('config', help='Config for wallet')

    parser_wallet = sub_parsers.add_parser('wallet', help='Access wallet')
    parser_tornado = sub_parsers.add_parser('tornado', help='Use tornado')
    parser_address = sub_parsers.add_parser('address', help='Get address')
    parser_transfer = sub_parsers.add_parser('transfer', help='Transfer token')

    args = parser.parse_args()
