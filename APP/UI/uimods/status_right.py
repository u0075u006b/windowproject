import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal, QTimer, QTimerEvent, QWaitCondition, QMutex
from PyQt5.QtWidgets import *
from gobalvar import GobalVar
from mianinit import MianInit


class DStreeView(QTreeWidget):

    toTHsingnal = pyqtSignal

    __child_init = "-"

    __toplevel = [["远程数据库", "IPADD", "PING", "DT"], ["本地数据库", "IPADD", "PING", "DT"], ["临时数据", "fPATH", "files", "DT"]]

    __rootpath = os.getcwd()

    def __init__(self, par):
        super(DStreeView, self).__init__()
        self.widthsize = par
        self.setFixedHeight(160)
        # print(self.widthsize)
        # print("widthsize is %s " % self.widthsize)
        self.setContentsMargins(0,0,0,0)
        self.setFrameShape(QFrame.WinPanel)
        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet("QTreeWidget{background-color:#FFFFF0;border:0px solid gray;border-top:1px solid gray; border-bottom:1px solid gray;}"
                           "QTreeWidget::item{background-color:#FFFFF0;color:black;border-bottom:1px solid gray;}"
                           "QTreeWidget::children{background-color:#FFFFF0;color:green;border-bottom:1px solid gray;}"
                           )
        # self.setFrameStyle("border-top: 3px solid gray;")
        self.setColumnCount(4)
        self.setColumnWidth(0, 95)
        self.setColumnWidth(1, 75)
        self.setColumnWidth(2, 48)
        self.setColumnWidth(3, 50)


        self.header().setStretchLastSection(False)
        # self.header().setDefaultAlignment(Qt.AlignCenter)
        # self.header().setFixedHeight(20)
        # self.header().setStyleSheet("border-width:0px 0px 1px 0px")
        # self.header().setSectionResizeMode(0,QHeaderView.Fixed)
        self.setHeaderHidden(True)  # headerhidden
        self.setIconSize(QSize(6, 6))
        # self.setStyleSheet("QTreeView{font-size:9px;}")
        self.fsize = QFont()
        self.fsize.setPointSize(9)
        self.childicon_flase = QIcon("./icon/Indicator_red.svg")
        self.childicon_true = QIcon("./icon/Indicator_green.svg")
        # self.rooticon.addFile("./icon/Indicator_green.svg",QSize(8,8),mode=QIcon.Normal, state=QIcon.On)
        # self.rooticon.addFile("./icon/Indicator_red.svg", QSize(8, 8), mode=QIcon.Normal, state=QIcon.Off)
        self.init()

    def init(self):
        if GobalVar.var_dataserverini:
            self.addtopLevel()
            self.addchilds()
            self.expandAll()
        else:
            pass

    def addtopLevel(self):
        for i in range(len(self.__toplevel)):
            root = QTreeWidgetItem(self)
            root.setChildIndicatorPolicy(2)
            for j in range(len(self.__toplevel[i])):
                root.setFont(j, self.fsize)
                root.setText(j, self.__toplevel[i][j])

    def addchilds(self):
        __childinit = GobalVar.var_dataserverini

        for dic_i in __childinit:
            if dic_i["servertype"] == "rds":
                for i in range(self.topLevelItemCount()):
                    if self.topLevelItem(i).text(0) == "远程数据库":
                        child = QTreeWidgetItem()
                        child.setText(0, dic_i['username'])
                        child.setFont(0, self.fsize)
                        child.setIcon(0, self.childicon_flase)
                        child.setText(1, dic_i['ipadd'])
                        child.setFont(1, self.fsize)
                        child.setText(2, self.__child_init)
                        child.setFont(2, self.fsize)
                        child.setText(3, dic_i['dbtype'])
                        child.setFont(3, self.fsize)
                        self.topLevelItem(i).addChild(child)
                    else:
                        pass

            elif dic_i["servertype"] == "locs":
                for i in range(self.topLevelItemCount()):
                    if self.topLevelItem(i).text(0) == "本地数据库":
                        child = QTreeWidgetItem()
                        child.setText(0, dic_i['username'])
                        child.setFont(0, self.fsize)
                        child.setIcon(0, self.childicon_flase)
                        child.setText(1, dic_i['ipadd'])
                        child.setFont(1, self.fsize)
                        child.setText(2, self.__child_init)
                        child.setFont(2, self.fsize)
                        child.setText(3, dic_i['dbtype'])
                        child.setFont(3, self.fsize)
                        self.topLevelItem(i).addChild(child)
                    else:
                        pass

            elif dic_i["servertype"] == "files":
                for i in range(self.topLevelItemCount()):
                    if self.topLevelItem(i).text(0) == "临时数据":
                        child = QTreeWidgetItem()
                        child.setText(0, dic_i['username'])
                        child.setFont(0, self.fsize)
                        child.setIcon(0, self.childicon_true)
                        child.setText(1, str(os.path.join(self.__rootpath,dic_i['filepath'])))
                        child.setFont(1, self.fsize)
                        child.setToolTip(1, str(os.path.join(self.__rootpath,dic_i['filepath'])))
                        child.setText(2, "-")
                        child.setFont(2, self.fsize)
                        child.setText(3, dic_i['dbtype'])
                        child.setFont(3, self.fsize)
                        self.topLevelItem(i).addChild(child)
                    else:
                        pass


class Viewone(QWidget):
    # tothreadsin = pyqtSignal()
    __parsiz = None

    def __init__(self):
        super(Viewone, self).__init__()
        # print(self.parsiz)
        self.box = QVBoxLayout()
        self.box.setContentsMargins(0, 0, 0, 0)
        self.lab = QLabel()
        self.viewcontent = DStreeView(self.__parsiz)
        self.uiset()

    def uiset(self):
        self.lab.setText("DATA SERVER:")
        qlabfont = QFont()
        qlabfont.setPointSize(10)
        self.lab.setFont(qlabfont)
        self.box.addWidget(self.lab)
        self.box.addWidget(self.viewcontent)
        self.box.addStretch()
        self.setLayout(self.box)

        # self.refreshthread(GobalVar.var_dataserverini)

    def setpar(self,par):
        if par:
            self.__parsiz = par
"""
    def refreshthread(self,inipar):
        self.server = ServerRun(inipar)
        self.server.statusfresh.connect(self.treefreshsolt)
        self.server.start()
        self.server.settimer()

    def treefreshsolt(self,d):
        print(d)
        if d:
            for i in range(self.viewcontent.topLevelItemCount()):
                if self.viewcontent.topLevelItem(i).text(0) == "临时数据":
                    print(d["status"])
                    print(d["filesnum"])
                    if d["status"] == True:
                        for child_cow in range(self.viewcontent.topLevelItem(i).childCount()):
                            if self.viewcontent.topLevelItem(i).child(child_cow).text(0) == "TEMP":
                                self.viewcontent.topLevelItem(i).child(child_cow).setIcon(0, self.viewcontent.childicon_true)
                    else:
                        pass
                    if d["filesnum"] == None:
                        pass
                    else:
                        for child_cow in range(self.viewcontent.topLevelItem(i).childCount()):
                            if self.viewcontent.topLevelItem(i).child(child_cow).text(0) == "TEMP":
                                self.viewcontent.topLevelItem(i).child(child_cow).setText(2,str(d["filesnum"]))
                else:
                    pass
"""


class CustomizeFrame(QFrame):
    def __init__(self):
        super(CustomizeFrame, self).__init__()
        self.setFixedWidth(280)
        # print("frame width %s" % self.size().width())
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Raised)
        self.setStyleSheet("background-color:white;border-width:0px;")
        self.box = QVBoxLayout()
        self.box.setContentsMargins(0,0,0,0)
        self.vc_0 = Viewone()
        self.vc_0.setpar(self.size().width())
        self.box.addWidget(self.vc_0)
        self.setLayout(self.box)


