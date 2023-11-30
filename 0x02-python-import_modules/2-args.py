#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1  # Subtract 1 to exclude the script name itself

    print(
        "Number of argument{}: {}".format("s" if num_args != 1 else "", num_args),
        end=""
    )
    
    print(
        "{}".format("s" if num_args != 1 else ":") if num_args != 0 else ".",
        end="\n\n"
    )

    if num_args > 0:
        for i in range(num_args):
            print("{}: {}".format(i + 1, argv[i + 1]))
