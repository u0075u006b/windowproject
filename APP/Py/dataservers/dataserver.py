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
    err_dic= {}

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
            self.err_dic['IOError'] = "文件夹错误"
            return self.err_dic

    def checkfiletype(self):
        if self.dbtype_ == "hdf":
            self.filesuffix = ".h5"
        elif self.dbtype_ == "xls":
            self.filesuffix = ".xls"
        else:
            pass

    def re_filelist(self):
        if self.can_on:
            _result = []
            try:
                __files = os.listdir(self.filepath)
                if __files:
                    for _file in __files:
                        if os.path.splitext(_file)[1] == self.filesuffix:
                            _result.append(_file)
                    return _result #is list
                else:
                    self.checkfilepath()
                    if self.can_on:
                        return _result
            except IOError:
                print("ioerrr")
                self.err_dic['IOError'] = "文件夹错误"
                return self.err_dic
            except Exception:
                self.err_dic['Error'] = "未知错误"
                return self.err_dic
            else:
                pass


        # isinstance(us, BaseException)#检查是否为错误
