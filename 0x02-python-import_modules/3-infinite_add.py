#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = 0
    for i in range(len(sys.argv) - 1):
        args += int(sys.argv[i + 1])
    print("{}".format(args))
