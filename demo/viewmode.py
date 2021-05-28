import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal, QTimer, QTimerEvent, QWaitCondition, QMutex
from PyQt5.QtWidgets import *
from APP.UI.common import QSSadd

# class DataS:
#     dic_status = {
#         "hold": True,
#         "unhold": False
#     }
#     dic_ipadd = {
#         "rds": "192.168.0.1",
#         "locs": "127.0.0.1",
#         "dim": "Redis"
#     }
#     dic_datasize = {
#         "k_1": [100, 200, 300, 400, 500],
#         "k_2": [600, 700, 800, 900, 1000],
#         "k_3": [1100, 1200, 1300, 1400, 1500]
#     }


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

class DataStatus(QThread):
    isout = pyqtSignal(dict)
    d_status_hdf = {"STS":False,"ADD":"--","PING":0,"EXP":[0,0,0]}
    d_status_rdssql = {"STS":False,"ADD":"--","PING":-1,"EXP":[0,0,0]}
    d_status_locsql = {"STS":False,"ADD":"--","PING":-1,"EXP":[0,0,0]}

    def __init__(self):
        super(DataStatus, self).__init__()
        self.th_on = True
        # self.cond = QWaitCondition()
        # self.mutex = QMutex()

    def hdfcheck(self):
        pass
    def rds_sql(self):
        pass
    def loc_sql(self):
        pass
    """def redis(self):next version add"""

    def run(self):
        pass





class DStreeView(QTreeWidget):
    __top = [['本地数据库','IP地址','PING','DATAS'],['远程数据库','IP地址','PING','DATAS'],['临时文件','文件路径','files','DATAS']]
    __child_init = "-"
    __ini = {"本地数据库":"mysql1","远程数据库":"slit","临时数据":"HDF"}
    # [['远程','192.168.0.1','200MB','3K'],['本地','192.168.0.2','300MB','5M'],['临时','192.168.0.3','400MB','8T']]
    # testlist = ['400MB','500MB','600MB','700MB','800MB','900MB','1000MB','1100MB']
    testcount = 0

    def __init__(self, par):
        super(DStreeView, self).__init__()
        self.cow = self.__top
        self.widthsize = par
        self.setFixedHeight(160)
        print(self.widthsize)
        # print("widthsize is %s " % self.widthsize)
        self.setContentsMargins(0,0,0,0)
        self.setFrameShape(QFrame.WinPanel)
        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet("background-color:#FFFFF0;border:0px solid gray;border-top:1px solid gray;")
        # self.setFrameStyle("border-top: 3px solid gray;")
        self.setColumnCount(5)
        self.setColumnWidth(0, 25)
        self.setColumnWidth(1, (self.widthsize-25)/3)
        self.setColumnWidth(2, (self.widthsize-25)/4)
        self.setColumnWidth(3, (self.widthsize-25)/5)
        self.setColumnWidth(4, (self.widthsize-25)/4)
        #
        self.setHeaderLabels(["","a","b","c","d"])
        self.header().setDefaultAlignment(Qt.AlignCenter)
        self.header().setFixedHeight(20)
        self.header().setStyleSheet("border-width:0px 0px 1px 0px")
        # self.header().setSectionResizeMode(0,QHeaderView.Fixed)
        self.setHeaderHidden(True)  # headerhidden
        self.setIconSize(QSize(8, 8))
        self.fsize = QFont()
        self.fsize.setPointSize(9)
        self.addtopLevel()
        # self.horizontalScrollBar().setStyleSheet(QSSadd.readqss("./scrollbar.qss"))
        # self.horizontalScrollBar().setFixedHeight(20)

        print(self.topLevelItemCount())
        for i in range(self.topLevelItemCount()):
            for j in range(0,self.topLevelItem(i).columnCount()):
                child = QTreeWidgetItem()
                child.setText(0, self.__ini[self.topLevelItem(i).text(1)])
                child.setText(1, self.__ini[self.topLevelItem(i).text(1)])
                self.topLevelItem(i).addChild()



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

    def addtopLevel(self):
        for i in range(len(self.cow)):
            root = QTreeWidgetItem(self)
            root_icon = QIcon("./icon/Indicator_green.svg")
            root.setIcon(0, root_icon)
            root.setFont(1, self.fsize)
            root.setFont(2, self.fsize)
            root.setFont(3, self.fsize)
            root.setFont(4, self.fsize)

            root.setChildIndicatorPolicy(0)
            root.setText(1, self.cow[i][0])
            root.setText(2, self.cow[i][1])
            root.setText(3, self.cow[i][2])
            root.setText(4, self.cow[i][3])



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



class Viewone(QWidget):
    def __init__(self, par):
        super(Viewone, self).__init__()
        self.parsiz = par
        print(self.parsiz)
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
