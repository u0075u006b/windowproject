from Py.ini_configparser import Config_Sec
from gobalvar import GobalVar
from Py.dataservers.dataserver import DServers



class MianInit:
    initargs = {
        "data_ini_path": "Py/config/datasources.ini"
    }
    dsr = None

    def __init__(self):
        pass

    def sysinit(self):
        if GobalVar.var_dataserverini is None:
            datapar = Config_Sec(self.initargs["data_ini_path"])
            setval = GobalVar()
            setval.setval(datapar.r_itempar())
        else:
            pass

    @staticmethod
    def dataservers_init():
        if not DServers.servers:
            DServers.inits(GobalVar.var_dataserverini)
        for s in DServers.servers:
            print(s)