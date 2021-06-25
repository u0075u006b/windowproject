from Py.ini_configparser import Config_Sec
from gobalvar import GobalVar


class MianInit:
    initargs = {
        "data_ini_path": "Py/config/datasources.ini"
    }

    def __init__(self):
        pass

    def sysinit(self):
        if GobalVar.var_dataserverini is None:
            datapar = Config_Sec(self.initargs["data_ini_path"])
            setval = GobalVar()
            setval.setval(datapar.r_itempar())
        else:
            pass