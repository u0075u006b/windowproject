import os


class SQLserver:  #

    def __init__(self, con):
        self.servername = con['section']
        self.servertype = con['servertype']
        self.dbtype_ = con['dbtype']
        self.ipadd = con['ipadd']
        self.user = con['username']
        self.port = con['port']
        self.key = con['password']


class Fileserver:
    can_suffix = [".h5", ".xls", ".xlsx", ".txt"]
    err_dic = {}

    def __init__(self, con):
        self.servername = con['section']
        self.servertype = con['servertype']
        self.dbtype_ = con['dbtype']
        self.user = con['username']
        self.filepath = os.path.join(os.getcwd(), con['filepath'])

    def checkfolderpath(self):
        if os.path.isdir(self.filepath):  # 检查文件路径存在
            return True
        else:
            return False

    def checksuffix(self,filename):
        if os.path.splitext(filename)[1] in self.can_suffix:
            return True
        else:
            return False
    # def checkfiletype(self):
    #     if self.dbtype_ == "hdf":
    #         self.filesuffix = ".h5"
    #     elif self.dbtype_ == "xls":
    #         self.filesuffix = ".xls"
    #     else:
    #         pass

    def re_filelist(self):
        if self.checkfolderpath():
            _result = []
            try:
                __files = os.listdir(self.filepath)
            except Exception as e:
                self.err_dic['unknowError'] = e
                return False, self.err_dic
            else:
                if __files:
                    for _file in __files:
                        if os.path.splitext(_file)[1] in self.can_suffix:
                            _result.append(_file)
                    return True, _result  # is list
                else:
                    return True, _result
        else:
            print("folderpath check is Flase")  # testing
            self.err_dic['IOError'] = "文件夹错误"
            return False, self.err_dic
        # isinstance(us, BaseException)#检查是否为错误


class DServers:
    servers = []
    names = locals()

    def __init__(self):
        pass

    @classmethod
    def inits(cls, con):
        if con is not None:
            for _c in con:
                if _c['servertype'] == 'files':
                    cls.names[_c['section']] = Fileserver(_c)
                    cls.servers.append(cls.names[_c['section']])
                    # if cls.names[_c['section']].checkfolderpath():  # "add folder check"
                    #     cls.servers.append(cls.names[_c['section']])
                    # else:
                    #     print("files错误")
                    #     pass
                elif _c['servertype'] == 'rds':
                    cls.names[_c['section']] = SQLserver(_c)
                    cls.servers.append(cls.names[_c['section']])
                elif _c['servertype'] == 'locs':
                    cls.names[_c['section']] = SQLserver(_c)
                    cls.servers.append(cls.names[_c['section']])
                else:
                    pass
        else:
            pass