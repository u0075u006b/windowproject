import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from demo.ini_configparser import Config_Sec
from demo.gobalvar import GobalVar


# def sysinit(**kwargs):
#     if GobalVar.var_dataserverini is None:
#         datapar = Config_Sec(kwargs["data_ini_path"])
#         GobalVar.var_dataserverini = datapar.r_itempar()
#     else:
#         pass
#
# if __name__ == "__main__":
#     initargs = {
#         "data_ini_path":"./config/datasources.ini"
#     }
#     sysinit(**initargs)
#     print(GobalVar.var_dataserverini)
#     print(GobalVar.var_dataserverini[1])



# class QT_one(QThread):
#     outsignal = pyqtSignal()
#
#
# class Mian(QWidget):
#     count = 0
#     addtxt = None
#
#     def __init__(self):
#         super(Mian, self).__init__()
#         self.resize(600,400)
#         self.t1 = None
#         self.run()
#
#     def run(self):
#         self.bt = QPushButton(self)
#         self.bt.resize(80,30)
#         self.bt.move(5,5)
#         self.bt.setText("按钮0")
#         # self.bt.clicked.connect(self.t1start)
#
#         self.bt2 = QPushButton(self)
#         self.bt2.resize(80,30)
#         self.bt2.move(5,40)
#         self.bt2.setText("按钮1")
#         # self.bt2.clicked.connect(self.t1stop)
#
#         self.txbrow = QTextBrowser(self)
#         self.txbrow.resize(self.size().width()-105,200)
#         self.txbrow.move(100,5)
#         self.txbrow.append("@ %s" %self.addtxt)
#
#
#         # self.bt3 = QPushButton(self)
#         # self.bt3.resize(80,30)
#         # self.bt3.move(5,75)
#         # self.bt3.setText("按钮2")
#         # self.bt3.clicked.connect(self.t1rstart)
#
#     # def t1start(self):
#     #     print("t1start")
#     #     # self.t1.start()
#     #     self.t1 = self.startTimer(1000)
#     #
#     # def t1stop(self):
#     #     print("t1stop")
#     #     # self.t1.startTimer(1000)
#     #     self.killTimer(self.t1)
#     #
#     # def t1rstart(self):
#     #     print("t1rstart")
#     #     self.t1 = self.startTimer(1000)
#     #
#     # def timershow(self):
#     #     self.count = self.count+1
#     #     print(self.count)
#     #
#     # def timerEvent(self,e=QTimerEvent):
#     #     if e.timerId() == self.t1:
#     #         self.count = self.count + 1
#     #         print(self.count)
#
# if  __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = Mian()
#     w.show()
#     sys.exit(app.exec_())


# from demo.ini_configparser import Config_Sec
#
# ini_path = "./config/datasources.ini"
# ini_cp = Config_Sec(ini_path)
# print(ini_cp.r.items())

# def fileNames(path, suffix=None):
#     names = os.listdir(path)
#     result = []
#     if suffix:
#         for name in names:
#             if os.path.splitext(name)[1] == suffix:
#                 result.append(name)
#     else:
#         result = names
#     return result
#
# # def run():
# #     path = os.path.join(os.getcwd(),"temp")
# #     print(os.path.isdir(path))
# #     try:
# #         ls = os.listdir(path)
# #     except IOError as e:
# #         return e
# #     else:
# #         return ls
# # us =run()
# # print(us)
# path = os.path.join(os.getcwd(),"temp")
# us = fileNames(path,suffix=".h5")
# print(us)
# print(isinstance(us,FileNotFoundError))
# print(type(us))

    # print(os.listdir(path))

# data = {
#     '远程数据库1': [('servertype', 'rds'), ('dbtype', 'MySQL'), ('ipadd', '192.168.0.1'), ('username', 'mysql1'), ('port', '2008'), ('password', '%12544')],
#     '远程数据库2': [('servertype', 'rds'), ('dbtype', 'MySQL'), ('ipadd', '192.168.2.3'), ('username', 'mysql2'), ('port', '2008'), ('password', '%12544')],
#     '本地数据库': [('servertype', 'locs'), ('dbtype', 'Sqlite'), ('ipadd', '127.0.0.1'), ('port', '30018'), ('username', 'mysql'), ('password', '%12544')],
#     '临时数据': [('servertype', 'files'), ('dbtype', 'hdf'), ('filepath', 'temp')],
#     '临时数据2': [('servertype', 'files'), ('dbtype', 'xls'), ('filepath', 'tempsded')]
# }
# server = []
# names = locals()
#
# class DATA:
#     filesuffix = None
#     temppath = None
#
#     def __init__(self,con):
#         self.con = con
#
#         self.pas()
#
#     def pas(self):
#         for i in self.con:
#             if i[0] == 'dbtype':
#                 if i[1] == 'hdf':
#                     self.filesuffix = ".h5"
#                 elif i[1] == 'xls':
#                     self.filesuffix = ".xls"
#             if i[0] == 'filepath':
#                 self.temppath = i[1]
#
#     def re(self):
#         return  self.filesuffix, self.temppath
#
# if data and type(data) == dict:
#    for key,value in data.items():
#        for i in value:
#            if i[0] == 'servertype' and i[1] == 'files':
#                names[key] = DATA(value)
#                server.append(names[key])
# else:
#     print(2)
#
# for i in server:
#     print(i)
#     print(i.filesuffix)
#     print(i.temppath)


#     for i in data.keys():
#         names[i] = data[i]
#         server.append(names[i])
# print(len(server))


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





    # def checkfiles(self):
    #     if self.can_on:
    #         if suffix:
    #             for name in names:
    #                 if os.path.splitext(name)[1] == suffix:
    #                     result.append(name)
    #         else:
    #             result = names
    #         return result
    #
    #
    # def filenames(self, suffix=None):
    #     names = os.listdir(self.usepath)
    #     result = []
    #     if suffix:
    #         for name in names:
    #             if os.path.splitext(name)[1] == suffix:
    #                 result.append(name)
    #     else:
    #         result = names
    #     return result
    #
    # def checkfile(self):
    #     if self.can_on:
    #         try:
    #             __ls = os.listdir(self.usepath)
    #         except IOError as e:
    #             return e
    #         else:
    #             checks = self.filenames(suffix=self.filesuffix)
    #             return checks  # checks is list
    #
    # def readdata(self):
    #     pass
    #
    # def writedata(self):
    #     pass

        # isinstance(us, BaseException)#检查是否为错误


class ServerRun(QThread):
    """
    statusfresh {}
    """
    datarefresh = pyqtSignal(dict)
    errsignal = pyqtSignal(str)
    statusfresh = pyqtSignal(dict)

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
        self.mutex = QMutex()
        self.config = inipr  # pr is list->dict

        self.filetimer = None
        self.rdstimer = None
        self.locstimer = None

        self.createsrvs()

        # self.rdstime = self.startTimer(5000)
        # self.locstime = self.startTimer(5000)
        # self.filechecktime = None

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

    def timestart(self,file=None,rds=None,locs=None):
        if isinstance(file,int):
            self.filetimer = self.startTimer(file)
        if isinstance(rds, int):
            self.rdstimer = self.startTimer(rds)
        if isinstance(locs, int):
            self.locstimer = self.startTimer(locs)

    def timstop(self):
        self.filetimer = None
        self.rdstimer = None
        self.locstimer = None

    def sendfilemsg(self,rus):
        if rus:
            self.statusfresh.emit(rus)

    def run(self):
        if self.th_on:
            if self.statusFlg:
                s = self.statuscheck()
                print(s)
                self.sendfilemsg(s)
                self.timestart(file=1000)

    def timerEvent(self, e=QTimerEvent):
        if e.timerId() == self.self.filetimer:
            self.sendfilemsg(self.statuscheck)