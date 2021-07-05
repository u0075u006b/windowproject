import os
from PyQt5.QtCore import *
from .dataserver import DServers


class ServerRun(QThread):
    """
    statusfresh {}
    """
    timetestcon = 0
    datarefresh = pyqtSignal(dict)
    errsignal = pyqtSignal(dict)
    statusfresh = pyqtSignal(dict)

    ckeck_times={"file_t":2000,"rds_t":5000,"locs_t":2000}

    refresh_rds = {}
    refresh_locs = {}
    refresh_files = {}
    servers = DServers.servers

    def __init__(self):
        super(ServerRun, self).__init__()
        self.th_on = True
        self.err_on = True
        self.statusFlg = True
        self.getdataFlg = False
        # self.cond = QWaitCondition()
        # self.mutex = QMutex()

        self.filetimer = None
        self.rdstimer = None
        self.locstimer = None

    def killtimer(self):
        print(self.filetimer)
        print(self.rdstimer)
        print(self.locstimer)
        if self.filetimer:
            self.killTimer(self.filetimer)
        if self.rdstimer:
            self.killTimer(self.rdstimer)
        if self.locstimer:
            self.killTimer(self.locstimer)
        else:
            pass

    def settimer(self,typ=None):
        if typ == "file":
            self.filetimer = self.startTimer(self.ckeck_times["file_t"])
        elif typ == "rds":
            self.rdstimer = self.startTimer(self.ckeck_times["rds_t"])
        elif typ == "locs":
            self.locstimer = self.startTimer(self.ckeck_times["locs_t"])
        else:
            self.filetimer = self.startTimer(self.ckeck_times["file_t"])
            self.rdstimer = self.startTimer(self.ckeck_times["rds_t"])
            self.locstimer = self.startTimer(self.ckeck_times["locs_t"])

    def statuscheck(self, _type):
        rdic = {}
        srv = None
        print(self.servers)
        if _type == "files":
            for s in self.servers:
                if s.servertype == 'files':
                    srv = s
                else:
                    continue
            __stat, _r = srv.re_filelist()
            print(_r)
            if __stat:
                if bool(_r):
                    rdic["status"] = True
                    rdic["filesnum"] = str(len(_r))
                    print("执行到这里1")
                    return rdic
                elif bool(_r) is False:
                    rdic["status"] = True
                    rdic["filesnum"] = str(0)
                    print("执行到这里2")
                    return rdic
                else:
                    pass
            else:
                rdic["status"] = False
                rdic["Ferr"] = _r
                print("执行到这里3")
                return rdic
        else:
            pass




    # def timestart(self,file=None,rds=None,locs=None):
    #     if isinstance(file,int):
    #         self.filetimer = self.startTimer(file)
    #     if isinstance(rds, int):
    #         self.rdstimer = self.startTimer(rds)
    #     if isinstance(locs, int):
    #         self.locstimer = self.startTimer(locs)

    def sendsingal(self,rus):
        if rus["status"]:
            self.statusfresh.emit(rus)
            self.err_on = True
        else:
            if self.err_on:
                self.errsignal.emit(rus["Ferr"])
                self.err_on = False

    def changegetdata(self):

        # for i in range(10):
        #     print("getdata:", i + 1)
        self.getdataFlg = False

    def run(self):
        if self.statusFlg:
            __result = self.statuscheck("files")
            print("qthread statuscheck:", __result)
            self.sendsingal(__result)

        while self.th_on:
            if self.getdataFlg:
                self.changegetdata()

    def timerEvent(self, e=QTimerEvent):
        if e.timerId() == self.filetimer:
            print("file计时器运行",self.timetestcon)
            __result = self.statuscheck("files")
            print("qthread statuscheck(timer):", __result)
            self.sendsingal(__result)
        if e.timerId() == self.rdstimer:
            print("rds计时器运行")
        if e.timerId() == self.locstimer:
            print("locs计时器运行")
