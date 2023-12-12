#!/usr/bin/env python3

import subprocess
import sys
import os
import re
import yaml


# MAIN ENTRY POINT main() -> 0 {{{1 
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
            checkMove(arg_list[1])
            pass

    # if no arguments given
    elif arg_len==1:
        errorMessage("no arguments given")

    # exhaustive switch
    else:
        errorMessage("no idea what just happened")

# }}}


# checkMove(the_arg) -> 0 {{{1
def checkMove(the_arg) -> int:

    # read the config file for all paths
    loc_conf = readConf()

    # format the directory path
    dl_path = os.path.expanduser(loc_conf["input"])

    # get all the metadata

    # make list of all files
    # in the download folder
    dl_list = os.listdir(dl_path)    

    # filter only the pdf files
    pdf_list = [x for x in dl_list if x[-3:]=="pdf"]

    # go through each of the files
    for each_pdf in pdf_list:

        # test the file path
        file_path = f"{dl_path}/{each_pdf}"

        # check the name has the right format
        name_check = nameFileCheck(each_pdf)
        
        # if its all good
        if name_check[0]:
           
            # find the right folder
            to_dir = each_pdf[0].upper()
            
            # full output path
            move_path = os.path.expanduser(f"{loc_conf['output']}/{to_dir}/")

            # are we moving?
            if the_arg=="move":
                the_symbol="<"
                moveTheFile(file_path, move_path)
            else:
                the_symbol="-"


            print(f"\033[32m[{to_dir}] {the_symbol} {each_pdf}\033[0m")

        else:
            if the_arg=="check":
                print(f"\033[31m[?] - {each_pdf}\033[0m")
            else:
                pass

        # check if its a file
        if os.path.isfile(file_path):
            pass
    return 0
# }}}


# errorMessage(the_message) -> 0 {{{1
def errorMessage(the_message) -> int:
    print(f"  [!] - ERROR: {the_message}")
    return 0
# }}}


# nameFileCheck(file_name) -> (Bool, int) {{{1
def nameFileCheck(file_name) -> tuple:

    good_format = bool(re.search("^[a-zA-z]+-\d{4}-.*pdf$", file_name))

    return (good_format,0)
# }}}


# readConf() -> dict {{{1
def readConf() -> dict:

    conf_path = os.path.expanduser("~/.config/vibman/vibman.yaml")

    with open(conf_path, "r") as fr:
        conf_dict = yaml.load(fr, Loader=yaml.FullLoader)

    return conf_dict
# }}}


# moveTheFile(from_path, to_path) -> 0 {{{1
def moveTheFile(from_path, to_path) -> int:
    # build the command
    command = ["mv", from_path, to_path]
    # EXECUTE
    subprocess.run(command) 
    return 0
# }}}


if __name__=="__main__":
    main()

