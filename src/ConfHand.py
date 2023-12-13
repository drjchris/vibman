import os
import yaml

def readConf() -> dict:

    """
    Reads the configuration file in .conf/vibman
    """

    conf_path = os.path.expanduser("~/.config/vibman/vibman.yaml")

    with open(conf_path, "r") as fr:
        conf_dict = yaml.load(fr, Loader=yaml.FullLoader)

    return conf_dict
