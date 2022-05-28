#!/usr/bin/env python3

import sys, time

def type_writer(message, delay_time):
    for char in message:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(delay_time)
