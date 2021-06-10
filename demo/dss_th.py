from PyQt5.QtCore import QThread,pyqtSignal,QTimerEvent


class DataStatusTH(QThread):
    isout = pyqtSignal(dict)


    def __init__(self):
        super(DataStatusTH, self).__init__()
        self.th_on = True
        # self.cond = QWaitCondition()
        # self.mutex = QMutex()

    def hdfcheck(self):
        pass
    def rds_sql(self):
        pass
    def loc_sql(self):
        pass
    """def redis(self):next version add"""

    def run(self):
        pass