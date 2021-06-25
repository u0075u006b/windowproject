import configparser


class Config_Sec:
    __sec_list = []
    __itempar_list = []
    dic = {}

    def __init__(self, filepath):
        self.filepath = filepath
        self.__cf = configparser.ConfigParser()
        self.__cf.read(self.filepath, encoding="utf-8")
        self.r = self.__cf

    def r_sec(self):
        for i in self.__cf.sections():
            self.__sec_list.append(i)
        return self.__sec_list

    def r_itempar(self):
        for i in self.__cf.sections():
            dic = {}
            dic["section"] = i
            for item in self.__cf.items(i):
                dic[item[0]] = item[1]
            self.__itempar_list.append(dic)
        return self.__itempar_list


