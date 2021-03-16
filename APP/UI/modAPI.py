
from APP.UI.common import QSSadd
from .uimods.vtoolmenu import *


class DrawerVtMenu():
    """
    1\need BUTTON STR from a dict
    2\need BUTTON height'sSIZEPPOLICY from a int
    3\need WIDGET-QSS
    """
    __qss = None
    __top_icon = []
    __sub_icon = None
    __ItemWidge_par = {"ItemWidget": [3, 5, 0, 5],"formspacing":0,"formVerticalSpacing":3}

    def __init__(self, _titls, _par):
        self.titls = _titls #topname,subnamelist(dict)
        self.button_par = _par #button height(int)
        self.toplist = []
        self.sublist_l = []
        self.create()

    def addstyle(self, style):
        if style:
            self.__qss = style
        else:
            pass

    def settopicon(self, i_0, i_1):
        self.__top_icon.append(i_0)
        self.__top_icon.append(i_1)

    def setsubicon(self, i_):
        self.__sub_icon = i_

    def create(self):
        if type(self.titls) is dict:
            for key in self.titls.keys():
                self.toplist.append(key)
            for val in self.titls.values():
                self.sublist_l.append(val)

            menuui = LeftItem(self.toplist, self.sublist_l)
            menuui.setqss(self.__qss)

            if bool(self.__top_icon) and bool(self.__sub_icon):
                __iconlist = [self.__top_icon,self.__sub_icon]
                menuui.seticon(__iconlist)
            elif bool(self.__top_icon):
                __iconlist = [self.__top_icon, None]
                menuui.seticon(__iconlist)
            else:
                pass

            menuui.setitemper(self.__ItemWidge_par)

            menuui.c_ui()
            return menuui
        else:
            pass
