from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QWidget, QHBoxLayout, QVBoxLayout, QFrame, QLabel, \
    QFormLayout, QTextBrowser, QMessageBox
import PyQt5.sip
from Py.dataservers import dataserver_th
from .vtoolmenu_info import MENU_INFO
from APP.UI.common import QSSadd
from .modAPI import DrawVtMenu, DrawRstatus
from APP.mianinit import MianInit

from .uimods.contentwid import dataload as dl

gbqss = QSSadd.readqss("./UI/qss/gb.qss")


class Left_Frame_0(QFrame):
    def __init__(self):
        super(Left_Frame_0, self).__init__()
        self.setObjectName("l_frame")
        self.setMaximumWidth(150)
        self.setMinimumWidth(150)
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet(gbqss)
        self.setContentsMargins(0, 0, 0, 0)
        box = QVBoxLayout()
        box.setContentsMargins(0, 0, 0, 0)
        self._menu = DrawVtMenu(MENU_INFO.__menu_info__, height_par=23)
        self._menu.addstyle(QSSadd.readqss("./UI/qss/vtoolmenu.qss"))
        self._menu.settopicon("./source/icon/plus1518%26.svg", "./source/icon/minus1518%26.svg")
        self.cre_menu = self._menu.create()
        box.addWidget(self.cre_menu)
        self.setLayout(box)


class Content_Frame_0(QFrame):

    def __init__(self):
        super(Content_Frame_0, self).__init__()
        self.setObjectName("r_frame")
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet(gbqss)
        self.box = QVBoxLayout()
        self.lab = QLabel()
        self.lab.setText("初始")
        self.box.addWidget(self.lab)
        self.setLayout(self.box)

    def rlay(self,n):
        self.movewid()
        self.newwid = n
        self.box.addWidget(self.newwid)
        self.setLayout(self.box)

    def movewid(self):
        print(self.box.count())

class Rside_Frame_0(QFrame):
    def __init__(self):
        super(Rside_Frame_0, self).__init__()
        self.setFixedWidth(280)
        self.setContentsMargins(0,0,0,0)
        # print("frame width %s" % self.size().width())
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Raised)
        self.setStyleSheet("background-color:white;border:0px;")
        self.box = QVBoxLayout()
        self.box.setContentsMargins(0,0,0,0)
        self.statusview = DrawRstatus(self.size().width())
        self.statusview_create = self.statusview.create()
        self.box.addWidget(self.statusview_create)
        self.box.addStretch()
        self.setLayout(self.box)


class M_window(QMainWindow):

    appname = "ANA SYS"

    def __init__(self):
        super(M_window, self).__init__()
        self.central_widget = QWidget()
        self.sta_bar = QStatusBar()
        self.left_frame = Left_Frame_0()
        self.content_frame = Content_Frame_0()
        self.rside_frame = Rside_Frame_0()
        self.sing = MianInit.dsr
        self.mainUI()
        self.dsr = dataserver_th.ServerRun()
        self.dataserverrun()

    def mainUI(self):
        self.setWindowTitle(M_window.appname)
        self.resize(900,600)
        # self.setWindowIcon(QIcon("./source/icon/mianwin5050.svg"))
        self.setCentralWidget(self.central_widget)
        box_0 = QHBoxLayout()
        box_0.setContentsMargins(0,0,0,0)

        box_0.addWidget(self.left_frame)
        box_0.addWidget(self.content_frame)
        box_0.addWidget(self.rside_frame)

        self.central_widget.setLayout(box_0)
        self.setstatus_bar()

        self.left_frame.cre_menu.item_0.update_.connect(self.onclickfun)
        self.left_frame.cre_menu.item_1.update_.connect(self.onclickfun)
        self.left_frame.cre_menu.item_2.update_.connect(self.onclickfun)

    def onclickfun(self, str_):
        print(str_)
        self.content_frame_upd(str_)


    def content_frame_upd(self,s):
        if s == "本地数据文件":
            self.new = dl.LocalLoad()
            self.content_frame.rlay(self.new)
        else:
            self.content_frame.lab.setText(s)

    def setstatus_bar(self):
        self.sta_bar.addWidget(QLabel("程序运行中    "))
        self.setStatusBar(self.sta_bar)

    def dataserverrun(self):
        self.dsr.statusfresh.connect(self.treefreshsolt)
        self.dsr.errsignal.connect(self.treefresherrsolt)
        self.dsr.start()
        self.dsr.settimer()
    #
    def treefreshsolt(self, tag, d):
        print(tag)
        print("d",d)
        if d:
            for i in range(self.rside_frame.statusview_create.viewcontent.topLevelItemCount()):#
                if self.rside_frame.statusview_create.viewcontent.topLevelItem(i).text(0) == "临时数据":
                    print(d["status"])
                    print(d["filesnum"])
                    if d["status"] == True:
                        for child_cow in range(self.rside_frame.statusview_create.viewcontent.topLevelItem(i).childCount()):
                            if self.rside_frame.statusview_create.viewcontent.topLevelItem(i).child(child_cow).text(0) == "TEMP":
                                self.rside_frame.statusview_create.viewcontent.topLevelItem(i).child(child_cow).setIcon(0,self.rside_frame.statusview_create.viewcontent.childicon_true)
                    else:
                        pass
                    if d["filesnum"] == None:
                        pass
                    else:
                        for child_cow in range(self.rside_frame.statusview_create.viewcontent.topLevelItem(i).childCount()):
                            if self.rside_frame.statusview_create.viewcontent.topLevelItem(i).child(child_cow).text(0) == "TEMP":
                                self.rside_frame.statusview_create.viewcontent.topLevelItem(i).child(child_cow).setText(2, str(d["filesnum"]))
                else:
                    pass

    def treefresherrsolt(self,d):
        print("d",d)
        if d['IOError']:
            for i in range(self.rside_frame.statusview_create.viewcontent.topLevelItemCount()):#
                if self.rside_frame.statusview_create.viewcontent.topLevelItem(i).text(0) == "临时数据":
                    for child_cow in range(self.rside_frame.statusview_create.viewcontent.topLevelItem(i).childCount()):
                        if self.rside_frame.statusview_create.viewcontent.topLevelItem(i).child(child_cow).text(0) == "TEMP":
                            self.rside_frame.statusview_create.viewcontent.topLevelItem(i).child(child_cow).setIcon(0,self.rside_frame.statusview_create.viewcontent.childicon_flase)
                    for child_cow in range(self.rside_frame.statusview_create.viewcontent.topLevelItem(i).childCount()):
                        if self.rside_frame.statusview_create.viewcontent.topLevelItem(i).child(child_cow).text(
                                0) == "TEMP":
                            self.rside_frame.statusview_create.viewcontent.topLevelItem(i).child(child_cow).setText(2,str("null"))
            QMessageBox.warning(self, "标题", d['IOError'], QMessageBox.Yes, QMessageBox.Yes)
        elif d['Error']:
            QMessageBox.warning(self, "标题", d['Error'], QMessageBox.Yes, QMessageBox.Yes)

