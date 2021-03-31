from PyQt5.QtCore import Qt, QSize, QEvent, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListWidget, \
    QFormLayout, QPushButton, QListWidgetItem
from APP.UI import upsingle


class ItemWidget(QWidget):
    update_ = pyqtSignal(str)

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
            self.bt.clicked.connect(self.onclick)
            self.setStyleSheet(self.qss)
            self.bt.setFixedHeight(self.bthgt-3)
            self.lay.addWidget(self.bt)

    def onclick(self):
        txt = self.sender().text()  # 获取发送信号的控件文本
        self.update_.emit(txt)

    # def fun(self,str_):
    #     print("fun is:")
    #     print(str_)

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(ItemWidget, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.lay.sizeHint().height()))


class TopButton(QPushButton):
    def __init__(self, item, name,icon_f,icon_uf):
        super(TopButton, self).__init__()
        self.item = item
        self.icon_f = icon_f
        self.icon_uf = icon_uf
        self.setIcon(self.icon_f)
        self.setCheckable(True) # 设置可选中
        self.setChecked(True)
        self.setText(name)

    def event(self, event):
        if event.type() == QEvent.MouseButtonPress:
            if self.isChecked():
                self.setIcon(self.icon_uf)
            else:
                self.setIcon(self.icon_f)
        return super(TopButton, self).event(event)

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
        self.t_icon_fold = QIcon(self.__iconlist[0][0])
        self.t_icon_unfold = QIcon(self.__iconlist[0][1])
        for _i in range(len(self.btname)):
            top_obj = QListWidgetItem(self)
            self.btn = TopButton(top_obj, self.btname[_i],self.t_icon_fold,self.t_icon_unfold)
            self.btn.setObjectName("menu_0")
            # self.btn.setIcon(self.t_icon_fold)
            self.btn.setFixedHeight(self.__btheight)
            self.btn.setStyleSheet(self.__qss)
            self.setItemWidget(top_obj, self.btn)
            if self.itemlist[_i]:
                sub_obj = QListWidgetItem(self)
                self.btn.toggled.connect(sub_obj.setHidden)
                self.itemc = ItemWidget(sub_obj, self.itemlist[_i],self.__qss,self.__itemper,self.__btheight)
                self.setItemWidget(sub_obj, self.itemc)
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



