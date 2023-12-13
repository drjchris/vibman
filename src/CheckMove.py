import os

from src import FileHelpers
from src import ConfHand


# checkMove(the_arg) -> 0 {{{1
def checkMove(the_arg) -> int:

    # read the config file for all paths
    loc_conf = ConfHand.readConf()

    # makes sure the output file is there

    # format the directory path
    dl_path = os.path.expanduser(loc_conf["input"])

    # format the output directory
    out_path = os.path.expanduser(loc_conf["output"])

    # check to see if the output directory exists
    # if it doesn't, then create one.
    if the_arg=="move":
        if not os.path.isdir(out_path):
            FileHelpers.makeOutDirs(out_path)
            print("[i] - out directory NOT found. Created.")

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
        name_check = FileHelpers.nameFileCheck(each_pdf)
        
        # if its all good
        if name_check[0]:
           
            # find the right folder
            to_dir = each_pdf[0].upper()
            
            # full output path
            move_path = os.path.expanduser(f"{loc_conf['output']}/{to_dir}/")

            # are we moving?
            if the_arg=="move":
                the_symbol="<"
                FileHelpers.moveTheFile(file_path, move_path)
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
