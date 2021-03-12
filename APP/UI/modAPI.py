
from APP.UI.common import QSSadd
from .uimods.vtoolmenu import *

class DrawerMenu():
    __qss = None

    def __init__(self,_titls, _par):
        self.titls = _titls #topname,subnamelist(dict)
        self.button_par = _par #button height(int)
        self.toplist = []
        self.sublist_l = []
        self.create()

    def create(self):
        if type(self.titls) is dict:
            for key in self.titls.keys():
                self.toplist.append(key)
            for val in self.titls.values():
                self.sublist_l.append(val)
            menuui = LeftItem(self.toplist, self.sublist_l)
            return menuui
        else:
            pass



    def restyle(self,style):
        self.__qss = style
