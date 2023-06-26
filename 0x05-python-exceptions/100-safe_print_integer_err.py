#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        print("Exception: {}".format(TypeError), file=sys.stderr)
        return False
    except ValueError:
        print("Exception: {}".format(ValueError), file=sys.stderr)
        return False
