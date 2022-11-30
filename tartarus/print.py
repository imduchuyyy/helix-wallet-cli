#! /usr/bin/env python3
from tartarus import constants
from tartarus.constants import PrintType


class Print(object):

    def __init__(self, type_print: str = PrintType.INFO, **kwargs) -> None:
        self.type_print = type_print

    def _get_color_print(self):
        if self.type_print == PrintType.ERROR:
            return constants.CRED
        elif self.type_print == PrintType.INFO:
            return constants.CCYAN
        elif self.type_print == PrintType.SUCCESS:
            return constants.GRN
        elif self.type_print == PrintType.WARNING:
            return constants.CYELLOW
        else:
            return constants.WHITE

    def _out(self, title: str = '', message: str = '') -> None:
        color_print = self._get_color_print()
        print_fmt = f'{color_print}{self.type_print.upper()}{constants.CEND} - '
        if title:
            print_fmt += f'{title} - '

        print(print_fmt, end='')
        print(message, end="", flush=True)
