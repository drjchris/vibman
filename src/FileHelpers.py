import string
import re
import subprocess

def makeDirs(out_path) -> None:

    "Function for checking and creating output directory"

    # make the global out path
    os.makedirs(out_path)

    # now go through all the letters
    # of the alphabet and create those dirs
    for letters in string.ascii_uppercase:
        os.makedirs(f"{out_path}/{letters}")

    return None



def nameFileCheck(file_name) -> tuple:
    
    """
    checks if the input file is formatted correctly
    """

    good_format = bool(re.search("^[a-zA-z]+-\d{4}-.*pdf$", file_name))

    return (good_format,0)


def moveTheFile(from_path, to_path) -> int:

    """
    Moves files from a to b
    """

    # build the command
    command = ["mv", from_path, to_path]
    # EXECUTE
    subprocess.run(command) 

    return 0
