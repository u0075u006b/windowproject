import configparser


class Config_Sec:
    __sec_list = []
    __item_dict = {}


    def __init__(self,filepath):
        # f_path = "./config/datasources.ini"
        self.filepath = filepath
        self.__cf = configparser.ConfigParser()
        self.__cf.read(self.filepath, encoding="utf-8")
        self.r=self.__cf

    def r_sec(self):
        for i in self.__cf.sections():
            self.__sec_list.append(i)
        return self.__sec_list

    def r_item(self):
        for i in self.__cf.sections():
            self.__item_dict[i] = self.__cf.items(i)
        return self.__item_dict




# f_path = "./config/datasources.ini"
# run = Config_Sec(f_path)
# # print(run.r_sec())
# # print(run.r_item())
# d = run.r_sec()
# print(d)
# for i in d:
#     # print(run.r.options(i))
#     # print(run.r.get(i,"servertype"))
#     print(run.r.items(i))
# print(list(run.r_item().values()))

# for i in range(3):
#     print(d["远程数据库"][i][0])
#



# f_path = "./config/datasources.ini"
# __cf = configparser.ConfigParser()
# __cf.read(f_path, encoding="utf-8")
# dic = {}
# for i in __cf.sections():
#     print(i)
#     dic[i] = __cf.items(i)
# print(dic)
