#!/usr/bin/env python3

import sys
import os

# local imports
from src import TheTest
from src import FileHelpers
from src import CheckMove



def main():

    # get the list of arguments
    arg_list = sys.argv

    # arguments allowed
    good_args = ["check", "move"]

    # get length of arguments
    arg_len = len(arg_list)

    # check we have the right number of
    # argument coming into the script
    if arg_len>=2:

        # alert if more than one
        # argument is given
        if arg_len >2:
            errorMessage("too many arguments given, only first one used")

        # check argument given is
        # is part of the ones allowed
        if arg_list[1] not in good_args:
            errorMessage("Incorrect argument")
        else:
            CheckMove.checkMove(arg_list[1])
            pass

    # if no arguments given
    elif arg_len==1:
        errorMessage("no arguments given")

    # exhaustive switch
    else:
        errorMessage("no idea what just happened")



# errorMessage(the_message) -> 0 {{{1
def errorMessage(the_message) -> int:
    print(f"  [!] - ERROR: {the_message}")
    return 0
# }}}





if __name__=="__main__":
    main()

