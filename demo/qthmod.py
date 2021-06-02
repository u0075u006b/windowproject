from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QTimerEvent, QWaitCondition
import random


class Datasever(QThread):
    datarefresh = pyqtSignal(dict)
    refresh_rds = {}
    refresh_locs = {}
    refresh_files = {}

    def __init__(self,config):
        super(Datasever, self).__init__()
        self.th_on = True
        # self.cond = QWaitCondition()
        self.mutex = QMutex()
        self.congfig = config
        self.configset()
        self.rdstime = self.startTimer(5000)
        self.locstime = self.startTimer(5000)
        self.filetime = self.startTimer(10000)

    def configset(self):
        pass

    def hdfcheck(self):
        pass
    def rds_sql(self):
        pass
    def loc_sql(self):
        pass
    """def redis(self):next version add"""

    def run(self):

    def timerEvent(self,e:QTimerEvent):
        if e.timerId() == self.rdstime:

        elif e.timerId() == self.locstime:

        elif e.timerId() == self.filetime:


class DataSource(QThread):
    status = True

    def __init__(self):
        super(DataSource, self).__init__()
        # self.cond = QWaitCondition()
        # self.mutex = QMutex()
        self.th_on = True
        self.status = True

    def setstatus(self):
        self.status = bool(1-self.status)

    def run(self):
        while self.th_on:


