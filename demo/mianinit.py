from demo.ini_configparser import Config_Sec
from demo.gobalvar import GobalVar


class MianInit:
    initargs = {
        "data_ini_path": "./config/datasources.ini"
    }

    def __init__(self):
        pass

    def sysinit(self):
        if GobalVar.var_dataserverini is None:
            datapar = Config_Sec(self.initargs["data_ini_path"])
            GobalVar.var_dataserverini = datapar.r_itempar()
        else:
            pass