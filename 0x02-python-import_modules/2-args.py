#!/usr/bin/python3
import sys

if __name__ == "__main__":
    
    argvs = len(sys.argv) - 1
    if argvs == 0:
        print("0 arguments.")
    elif argvs == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argvs))
    for i in range(argvs):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
