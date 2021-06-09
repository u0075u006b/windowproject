from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QTimerEvent, QWaitCondition
from sqlalchemy import *
import os
import random

data = {
    '远程数据库1': [('servertype', 'rds'), ('dbtype', 'MySQL'), ('ipadd', '192.168.0.1'), ('username', 'mysql1'), ('port', '2008'), ('password', '%12544')],
    '远程数据库2': [('servertype', 'rds'), ('dbtype', 'MySQL'), ('ipadd', '192.168.2.3'), ('username', 'mysql2'), ('port', '2008'), ('password', '%12544')],
    '本地数据库': [('servertype', 'locs'), ('dbtype', 'Sqlite'), ('ipadd', '127.0.0.1'), ('port', '30018'), ('username', 'mysql'), ('password', '%12544')],
    '临时数据': [('servertype', 'files'), ('dbtype', 'hdf'), ('filepath', 'temp')]
}


class SQLserver:
    servers = 0

    def __init__(self):
        pass

class Fileserver:

    def __init__(self,conf):
        self.conf = conf #conf is a list consisting tuples
        self.foldername = None
        self.usepath = None
        self.can_on = False
        self.filesuffix = None
        self.dataread = None
        self.datawrite = None
        self.parsing()
        self.createpath()

    def parsing(self):
        if self.conf:
            for _i in self.conf:
                if _i[0] == 'filepath':
                    self.foldername = _i[1]
                elif  _i[0] == 'dbtype':
                    self.filesuffix = ".h5"
                else:pass

    def createpath(self):
        if os.path.isdir(os.path.join(os.getcwd(), self.foldername)):
            self.usepath = os.path.join(os.getcwd(), self.foldername) #检查文件路径存在
            self.can_on = True
        else:
            pass

    def filenames(self, suffix=None):
        names = os.listdir(self.usepath)
        result = []
        if suffix:
            for name in names:
                if os.path.splitext(name)[1] == suffix:
                    result.append(name)
        else:
            result = names
        return result

    def checkfile(self):
        if self.can_on:
            try:
                __ls = os.listdir(self.usepath)
            except IOError as e:
                return e
            else:
                checks = self.filenames(suffix=self.filesuffix)
                return checks #checks is list

    def readdata(self):
        pass

    def writedata(self):
        pass

        # isinstance(us, BaseException)#检查是否为错误



class Dataserver(QThread):
    datarefresh = pyqtSignal(dict)
    errsignal = pyqtSignal(str)

    refresh_rds = {}
    refresh_locs = {}
    refresh_files = {}
    servers = []

    def __init__(self,inipr):
        super(Dataserver, self).__init__()
        self.th_on = True
        # self.cond = QWaitCondition()
        self.mutex = QMutex()
        self.congfig = inipr #par is dict
        self.createconnect()
        # self.rdstime = self.startTimer(5000)
        # self.locstime = self.startTimer(5000)


        self.filechecktime = None

    def createconnect(self):
        if self.congfig and type(data) == dict:


        # for i in d:
        #     # print(run.r.options(i))
        #     if i == "临时数据":
        #         print(run.r.get(i, "filepath"))

    def filescheck(self):


    def rds_sql(self):
        pass
    def loc_sql(self):
        pass
    """def redis(self):next version add"""

    def run(self):
        while self.th_on:
            if

    def timerEvent(self,e:QTimerEvent):
        if e.timerId() == self.filechecktime:

        # elif e.timerId() == self.locstime:
        #
        # elif e.timerId() == self.filetime:

