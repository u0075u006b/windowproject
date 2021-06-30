import os
from PyQt5.QtCore import *
from .dataserver import Fileserver,SQLserver


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
    servers = []

    names = locals()

    def __init__(self, inipr):
        super(ServerRun, self).__init__()
        self.th_on = True
        self.statusFlg = True
        self.getdataFlg = False
        # self.cond = QWaitCondition()
        # self.mutex = QMutex()
        self.config = inipr  # pr is list->dict

        self.filetimer = None
        self.rdstimer = None
        self.locstimer = None

        self.createsrvs()

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

    def createsrvs(self):
        for con in self.config:
            if con['servertype'] == 'files':
                self.names[con['section']] = Fileserver(con)
                self.servers.append(self.names[con['section']])
            elif con['servertype'] == 'rds':
                self.names[con['section']] = SQLserver(con)
                self.servers.append(self.names[con['section']])
            elif con['servertype'] == 'locs':
                self.names[con['section']] = SQLserver(con)
                self.servers.append(self.names[con['section']])
            else:
                pass

    def statuscheck(self):
        rdic = {}
        for srv in self.servers:
            if srv.servertype == 'files':
                _r = srv.re_filelist()
                print("_r type:",type(_r))
                if isinstance(_r, list):
                    if _r :
                        rdic["status"] = True
                        rdic["filesnum"] = str(len(_r))
                        print("执行到这里1")
                        return rdic
                    elif _r == []:
                        rdic["status"] = True
                        rdic["filesnum"] = str(0)
                        print("执行到这里2")
                        return rdic
                    else:
                        rdic["status"] = False
                        rdic["filesnum"] = None
                        print("执行到这里3")
                        return rdic
                elif isinstance(_r, dict):
                    self.errsignal.emit(_r)
                    print("eee")
                else:
                    pass
            else:
                pass

    # def timestart(self,file=None,rds=None,locs=None):
    #     if isinstance(file,int):
    #         self.filetimer = self.startTimer(file)
    #     if isinstance(rds, int):
    #         self.rdstimer = self.startTimer(rds)
    #     if isinstance(locs, int):
    #         self.locstimer = self.startTimer(locs)

    def sendfilemsg(self,rus):
        if rus:
            self.statusfresh.emit(rus)

    def changegetdata(self):

        # for i in range(10):
        #     print("getdata:", i + 1)
        self.getdataFlg = False

    def run(self):
        if self.statusFlg:
            s = self.statuscheck()
            print("qthread statuscheck:", s)
            self.sendfilemsg(s)
        while self.th_on:
            if self.getdataFlg:
                self.changegetdata()

    def timerEvent(self, e=QTimerEvent):
        if e.timerId() == self.filetimer:
            print("file计时器运行",self.timetestcon)
            s = self.statuscheck()
            self.sendfilemsg(s)
        if e.timerId() == self.rdstimer:
            print("rds计时器运行")
        if e.timerId() == self.locstimer:
            print("locs计时器运行")
