import os
from PyQt5.QtCore import *


class SQLserver:  #

    def __init__(self,con):
        self.servername = con['section']
        self.servertype = con['servertype']
        self.dbtype_ = con['dbtype']
        self.ipadd = con['ipadd']
        self.user = con['username']
        self.port = con['port']
        self.key = con['password']


class Fileserver:
    def __init__(self,con):
        self.servername = con['section']
        self.servertype = con['servertype']
        self.dbtype_ = con['dbtype']
        self.user = con['username']
        self.filepath = os.path.join(os.getcwd(), con['filepath'])
        self.filesuffix = ""
        self.can_on = False # 运行标记
        self.checkfilepath()
        self.checkfiletype()

    def checkfilepath(self):
        if os.path.isdir(self.filepath): # 检查文件路径存在
            self.can_on = True
        else:
            pass

    def checkfiletype(self):
        if self.dbtype_ == "hdf":
            self.filesuffix = ".h5"
        elif self.dbtype_ == "xls":
            self.filesuffix = ".xls"
        else:
            pass

    def re_filelist(self):

        if self.can_on:
            files = os.listdir(self.filepath)
            result = []
            if files:
                for file in files:
                    if os.path.splitext(file)[1] == self.filesuffix:
                        result.append(file)
                return result #is list

        # isinstance(us, BaseException)#检查是否为错误

class ServerRun(QThread):
    """
    statusfresh {}
    """
    timetestcon = 0
    datarefresh = pyqtSignal(dict)
    errsignal = pyqtSignal(str)
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
                if _r :
                    rdic["status"] = True
                    rdic["filesnum"] = str(len(_r))
                    print("执行到这里1")
                    return rdic
                else:
                    rdic["status"] = False
                    rdic["filesnum"] = None
                    print("执行到这里2")
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
