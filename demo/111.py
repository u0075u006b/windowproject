import os


from demo.ini_configparser import Config_Sec

ini_path = "./config/datasources.ini"
ini_cp = Config_Sec(ini_path)
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

data = {
    '远程数据库1': [('servertype', 'rds'), ('dbtype', 'MySQL'), ('ipadd', '192.168.0.1'), ('username', 'mysql1'), ('port', '2008'), ('password', '%12544')],
    '远程数据库2': [('servertype', 'rds'), ('dbtype', 'MySQL'), ('ipadd', '192.168.2.3'), ('username', 'mysql2'), ('port', '2008'), ('password', '%12544')],
    '本地数据库': [('servertype', 'locs'), ('dbtype', 'Sqlite'), ('ipadd', '127.0.0.1'), ('port', '30018'), ('username', 'mysql'), ('password', '%12544')],
    '临时数据': [('servertype', 'files'), ('dbtype', 'hdf'), ('filepath', 'temp')],
    '临时数据2': [('servertype', 'files'), ('dbtype', 'xls'), ('filepath', 'tempsded')]
}
server = []
names = locals()

class DATA:
    filesuffix = None
    temppath = None

    def __init__(self,con):
        self.con = con

        self.pas()

    def pas(self):
        for i in self.con:
            if i[0] == 'dbtype':
                if i[1] == 'hdf':
                    self.filesuffix = ".h5"
                elif i[1] == 'xls':
                    self.filesuffix = ".xls"
            if i[0] == 'filepath':
                self.temppath = i[1]

    def re(self):
        return  self.filesuffix, self.temppath

if data and type(data) == dict:
   for key,value in data.items():
       for i in value:
           if i[0] == 'servertype' and i[1] == 'files':
               names[key] = DATA(value)
               server.append(names[key])
else:
    print(2)

for i in server:
    print(i)
    print(i.filesuffix)
    print(i.temppath)


#     for i in data.keys():
#         names[i] = data[i]
#         server.append(names[i])
# print(len(server))