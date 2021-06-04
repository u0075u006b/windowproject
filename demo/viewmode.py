import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal, QTimer, QTimerEvent, QWaitCondition, QMutex
from PyQt5.QtWidgets import *
from APP.UI.common import QSSadd
from demo.dss_th import DataStatusTH
from demo.ini_configparser import Config_Sec


# class Th_dataserver(QThread):
#     dataout = pyqtSignal(str)
#
#     def __init__(self):
#         super(Th_dataserver, self).__init__()
#         self.data = DataS()
#         self.on_flag = True
#
#     def run(self):
#         while self.on_flag is True:
#             print("on_flag %s" % self.on_flag)
#             self.sld = QSlider()
#             self.sld.valueChanged()
#             self.sleep(1)
#
#
# class StatusView(QWidget):
#     def __init__(self):
#         super(StatusView, self).__init__()
#         self.box = QVBoxLayout()
#         self.set()
#
#     def set(self):
#         self.resize(600, 500)
#         m_box = QVBoxLayout()
#         bt_box = QHBoxLayout()
#
#         self.btn_run.setText("QTHREAD Run")
#         self.btn_run.setFixedSize(100, 80)
#         self.btn_run.setCheckable(True)
#         self.btn_run.setStyleSheet("background-color:green;color:white")
#         # self.btn_run.clicked.connect(self.clkrun)
#
#         self.btn_run.setText("QTHREAD Pause")
#         self.btn_run.setFixedSize(100, 80)
#         self.btn_run.setCheckable(True)
#         self.btn_run.setStyleSheet("background-color:green;color:white")
#
#         bt_box.addWidget(self.btn_run)
#         self.box.addRow(bt_box)
#
#         self.box.addRow(m_box)


# class ParenContainer(QFrame):
#     def __init__(self):
#         super(ParenContainer, self).__init__()
#         self.resize()



class DStreeView(QTreeWidget):

    toTHsingnal = pyqtSignal
    __ini_path = "./config/datasources.ini"
    __ini_cp = Config_Sec(__ini_path)
    __child_init = "-"

    __toplevel = [["远程数据库", "IPADD", "PING", "DT"], ["本地数据库", "IPADD", "PING", "DT"], ["临时数据", "fPATH", "files", "DT"]]

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
        if self.__ini_cp:
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
        __childinit = list(self.__ini_cp.r_item().values())
        print(self.__ini_cp.r_item())
        for i in range(len(__childinit)):
            for _tup in __childinit[i]:
                if _tup[0] == "servertype" and _tup[1] == "rds":
                    wrt = dict(__childinit[i])
                    for i in range(self.topLevelItemCount()):
                        if self.topLevelItem(i).text(0) == "远程数据库":
                            child = QTreeWidgetItem()
                            child.setText(0, wrt['username'])
                            child.setFont(0, self.fsize)
                            child.setIcon(0, self.childicon_flase)
                            child.setText(1, wrt['ipadd'])
                            child.setFont(1, self.fsize)
                            child.setText(2, self.__child_init)
                            child.setFont(2, self.fsize)
                            child.setText(3, wrt['dbtype'])
                            child.setFont(3, self.fsize)
                            self.topLevelItem(i).addChild(child)
                        else:
                            pass

                elif _tup[0] == "servertype" and _tup[1] == "locs":
                    wrt = dict(__childinit[i])
                    for i in range(self.topLevelItemCount()):
                        if self.topLevelItem(i).text(0) == "本地数据库":
                            child = QTreeWidgetItem()
                            child.setText(0, wrt['username'])
                            child.setFont(0, self.fsize)
                            child.setIcon(0, self.childicon_flase)
                            child.setText(1, wrt['ipadd'])
                            child.setFont(1, self.fsize)
                            child.setText(2, self.__child_init)
                            child.setFont(2, self.fsize)
                            child.setText(3, wrt['dbtype'])
                            child.setFont(3, self.fsize)
                            self.topLevelItem(i).addChild(child)
                        else:
                            pass

                elif _tup[0] == "servertype" and _tup[1] == "files":
                    wrt = dict(__childinit[i])
                    for i in range(self.topLevelItemCount()):
                        if self.topLevelItem(i).text(0) == "临时数据":
                            child = QTreeWidgetItem()
                            child.setText(0, wrt['servertype'])
                            child.setFont(0, self.fsize)
                            child.setIcon(0, self.childicon_flase)
                            child.setText(1, wrt['filepath'])
                            child.setFont(1, self.fsize)
                            child.setToolTip(1, wrt['filepath'])
                            child.setText(2, "-")
                            child.setFont(2, self.fsize)
                            child.setText(3, wrt['dbtype'])
                            child.setFont(3, self.fsize)
                            self.topLevelItem(i).addChild(child)
                        else:
                            pass



        # for i in range(self.topLevelItemCount()):
        #     print(self.topLevelItem(i).text(0))
        #     if self.topLevelItem(i).text(0) == "远程数据库":
        #         child = QTreeWidgetItem()
        #         for j in self.__ini_cp.r_item()["远程数据库"]:
        #             if j[0] == "username":
        #                 child.setText(0,j[1])
        #                 child.setFont(0, self.fsize)
        #                 child.setIcon(0,self.childicon)
        #             else:
        #                 pass
        #             if j[0] == "ipadd":
        #                 child.setText(1,j[1])
        #                 child.setFont(1, self.fsize)
        #             else:
        #                 pass
        #         child.setText(2, self.__child_init)
        #         child.setFont(2, self.fsize)
        #         child.setText(3, self.__child_init)
        #         child.setFont(3, self.fsize)
        #         self.topLevelItem(i).addChild(child)
        #     elif self.topLevelItem(i).text(0) == "本地数据库":
        #         child = QTreeWidgetItem()
        #         for j in self.__ini_cp.r_item()["本地数据库"]:
        #             if j[0] == "username":
        #                 child.setText(0,j[1])
        #                 child.setFont(0, self.fsize)
        #                 child.setIcon(0,self.childicon)
        #             else:
        #                 pass
        #             if j[0] == "ipadd":
        #                 child.setText(1,j[1])
        #                 child.setFont(1, self.fsize)
        #             else:
        #                 pass
        #         child.setText(2, self.__child_init)
        #         child.setFont(2, self.fsize)
        #         child.setText(3, self.__child_init)
        #         child.setFont(3, self.fsize)
        #         self.topLevelItem(i).addChild(child)
        #     elif self.topLevelItem(i).text(0) == "临时数据":
        #         child = QTreeWidgetItem()
        #         for j in self.__ini_cp.r_item()["临时数据"]:
        #             if j[0] == "filetype":
        #                 child.setText(0, j[1])
        #                 child.setFont(0, self.fsize)
        #             else:
        #                 pass
        #             if j[0] == "filepath":
        #                 child.setText(1, j[1])
        #                 child.setFont(1, self.fsize)
        #             else:
        #                 pass
        #         child.setText(2, self.__child_init)
        #         child.setFont(2, self.fsize)
        #         child.setText(3, self.__child_init)
        #         child.setFont(3, self.fsize)
        #         self.topLevelItem(i).addChild(child)
        #     else:
        #         pass
        #

        # self.horizontalScrollBar().setStyleSheet(QSSadd.readqss("./scrollbar.qss"))
        # self.horizontalScrollBar().setFixedHeight(20)

        # for i in range(self.topLevelItemCount()):
        #     for j in range(0,self.topLevelItem(i).columnCount()):
        #         child = QTreeWidgetItem()
        #         child.setText(0, self.__ini[self.topLevelItem(i).text(1)])
        #         child.setText(1, self.__ini[self.topLevelItem(i).text(1)])
        #         self.topLevelItem(i).addChild()



        # self.t1 = self.startTimer(10000)

    # def traverse(self,data):
    #     for i in range(self.topLevelItemCount()):
    #         if self.topLevelItem(i).text(0) == "本地":
    #             if self.topLevelItem(2).text(2) != data:
    #                 self.topLevelItem(2).setText(2,data)
    #                 if DStreeView.testcount == 7:
    #                     DStreeView.testcount = 0
    #                 else:
    #                     DStreeView.testcount += 1
    #             else:
    #                 pass
    #         else:
    #             pass





        # print("TREE width %s" % self.sizeHint().width())


    #
    # def timerEvent(self, e=QTimerEvent):
    #     if e.timerId() == self.t1:
    #
    #         data = DStreeView.testlist[DStreeView.testcount]
    #         print(data)
    #         for i in range(self.topLevelItemCount()):
    #             if self.topLevelItem(i).text(0) == "本地":
    #                 if self.topLevelItem(i).text(2) != data:
    #                     self.topLevelItem(i).setText(2, data)
    #                 else:
    #                     pass
    #             else:
    #                 pass
    #         if DStreeView.testcount < 7:
    #             DStreeView.testcount += 1
    #         else:
    #             DStreeView.testcount = 0

    # def timerEvent(self, event: QTimerEvent):
    #     if event.timerId() == self.t1:
    #         con = self.findItems("远程数据库", Qt.MatchExactly, 1)[0]
    #         print(con)
    #         con.setText(1, "近程数据库")


class Viewone(QWidget):
    def __init__(self, par):
        super(Viewone, self).__init__()
        self.parsiz = par
        # print(self.parsiz)
        self.box = QVBoxLayout()
        self.box.setContentsMargins(0, 0, 0, 0)
        self.lab = QLabel()
        self.lab.setText("DATA SERVER:")
        qlabfont = QFont()
        qlabfont.setPointSize(10)
        self.lab.setFont(qlabfont)
        self.viewcontent = DStreeView(self.parsiz)
        # r = self.viewcontent.findItems("192.168.0.1",Qt.MatchExactly,1)
        # print(r[0].t)
        # print(type(r))
        self.box.addWidget(self.lab)
        self.box.addWidget(self.viewcontent)
        self.box.addStretch()
        self.setLayout(self.box)

        # print(self.viewcontent.model().columnCount())
    def refresh(self):
        pass



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
        self.vc_0 = Viewone(self.size().width())
        self.box.addWidget(self.vc_0)
        self.setLayout(self.box)




class MainWin(QMainWindow):
    appname = "VIEWMODE"

    def __init__(self):
        super(MainWin, self).__init__()
        self.central_widget = QWidget()
        self.box_central = QHBoxLayout()
        self.r_sider = CustomizeFrame()
        self.mainui()


    def mainui(self):
        self.setWindowTitle(MainWin.appname)
        self.resize(800,600)
        self.central_widget.setStyleSheet("background-color:gainsboro")
        self.setCentralWidget(self.central_widget)

        self.box_central.addStretch()
        self.box_central.addWidget(self.r_sider)

        self.box_central.setContentsMargins(0, 0, 2, 0)
        self.central_widget.setLayout(self.box_central)
    #
    def viewrefresh(self):
        self.time = QTimer(self)


# class W1(QDialog):
#     def __init__(self):
#         super(W1, self).__init__()
#         self.resize(400,300)
#
#     def in

if __name__ == "__main__":
    app = QApplication(sys.argv)
    r = MainWin()
    r.show()

    # f = QFont()
    app.setFont(QFont("Times New Roman, SimSun, SimSun-ExtB, YouYuan"))
    # f.setFamily("YouYuan")
    # print(f.family())
    # print(app.font().family())

    sys.exit(app.exec_())
