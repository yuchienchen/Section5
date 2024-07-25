#!/usr/bin/env python3

import sys


def find_smallest_int(filename):
    """
    Implement the function find_smallest_int(filename) that takes
    as a parameter a filename (which is just a string) that refers
    to a file containing a single integer on each line, and returns
    the smallest unique positive integer in the file.
    """
    pass


# no need to edit code below this line
def main():
    args = sys.argv[1:]
    # to run from terminal:
    # python3 smallest_int.py filename
    if len(args) == 1:
        filename = args[0]
        result = find_smallest_int(filename)
        print(result)


if __name__ == "__main__":
    main()