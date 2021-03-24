from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QLabel, QListWidget, \
    QFormLayout, QPushButton, QListWidgetItem, QCheckBox


class ItemWidget(QWidget):
    def __init__(self, item, s_list, qss, par, hgt):
        super(ItemWidget, self).__init__()
        self.item = item
        self.list_ = s_list
        self.qss = qss
        self.par = par
        self.bthgt = hgt

        self.lay = QFormLayout(self)
        if "ItemWidget" in self.par.keys() and self.par["ItemWidget"]:
            mar_par = self.par["ItemWidget"]
            self.lay.setContentsMargins(mar_par[0],mar_par[1],mar_par[2],mar_par[3])
        else:
            pass

        if "formspacing" in self.par.keys() and self.par["formspacing"]:
            self.lay.setSpacing(self.par["formspacing"])
        else:
            pass

        if "formVerticalSpacing" in self.par.keys() and self.par["formVerticalSpacing"]:
            self.lay.setVerticalSpacing(self.par["formVerticalSpacing"])
        else:
            pass

        for _i in range(len(self.list_)):
            self.bt = QPushButton(self.list_[_i])
            self.bt.setObjectName("menu_1")
            self.setStyleSheet(self.qss)
            self.bt.setFixedHeight(self.bthgt-3)
            self.lay.addWidget(self.bt)

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(ItemWidget, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.lay.sizeHint().height()))


class TopButton(QPushButton):
    def __init__(self, item, name):
        super(TopButton, self).__init__()
        self.item = item
        self.setCheckable(True) # 设置可选中
        self.setChecked(True)
        self.setText(name)

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(TopButton, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))


class LeftItem(QListWidget):
    __qss = None
    __iconlist = None
    __itemper = None
    __btheight = None

    def __init__(self,btname,listname):
        super(LeftItem, self).__init__()
        self.btname = btname
        self.itemlist = listname
        self.setContentsMargins(0,0,0,0)
        self.setStyleSheet("border:0px")
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def c_ui(self):
        t_icon_fold = QIcon(self.__iconlist[0][0])
        t_icon_unfold = QIcon(self.__iconlist[0][1])
        for _i in range(len(self.btname)):
            top_obj = QListWidgetItem(self)
            btn = TopButton(top_obj, self.btname[_i])
            btn.setObjectName("menu_0")
            btn.setIcon(t_icon_fold)
            btn.setFixedHeight(self.__btheight)
            btn.setStyleSheet(self.__qss)
            self.setItemWidget(top_obj, btn)
            if self.itemlist[_i]:
                sub_obj = QListWidgetItem(self)
                btn.toggled.connect(sub_obj.setHidden)
                item = ItemWidget(sub_obj, self.itemlist[_i],self.__qss,self.__itemper,self.__btheight)
                self.setItemWidget(sub_obj, item)
                sub_obj.setHidden(True)
            else:
                pass

    def setqss(self, qss):
        self.__qss = qss

    def seticon(self,icon):
        self.__iconlist = icon

    def setitemper(self,per):
        self.__itemper = per

    def setbtheight(self,per):
        self.__btheight = per



