import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal
from PyQt5.QtWidgets import *


class DataS:
    dic_status = {
        "hold": True,
        "unhold": False
    }
    dic_ipadd = {
        "rds": "192.168.0.1",
        "locs": "127.0.0.1",
        "dim": "Redis"
    }
    dic_datasize = {
        "k_1": [100, 200, 300, 400, 500],
        "k_2": [600, 700, 800, 900, 1000],
        "k_3": [1100, 1200, 1300, 1400, 1500]
    }


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
    datalist = [['1','192.168.0.1','200MB','3K'],['2','192.168.0.2','300MB','5M'],['3','192.168.0.3','400MB','8T']]

    def __init__(self, par):
        super(DStreeView, self).__init__()
        self.cow = self.datalist
        self.widthsize = par
        print("widthsize is %s " % self.widthsize)
        self.setContentsMargins(0,0,0,0)
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Plain)
        self.setColumnCount(4)
        self.setColumnWidth(0,self.widthsize/4)
        self.setColumnWidth(1,self.widthsize/4)
        self.setColumnWidth(2,self.widthsize/4)
        self.setColumnWidth(3,self.widthsize/4)

        self.setHeaderLabels(["a","b","c","d"])
        self.setIconSize(QSize(8,8))
        fsize = QFont()
        fsize.setPointSize(9)
        for i in range(len(self.cow)):
            root = QTreeWidgetItem(self)
            root.setFont(0,fsize)
            root.setFont(1, fsize)
            root.setFont(2, fsize)
            root.setFont(3, fsize)
            root.setChildIndicatorPolicy(0)
            root.setText(0, DStreeView.datalist[i][0])
            root_icon = QIcon(QApplication.style().standardIcon(0))
            root.setIcon(0, root_icon)
            root.setText(1, DStreeView.datalist[i][1])
            root.setText(2, DStreeView.datalist[i][2])
            root.setText(3, DStreeView.datalist[i][3])
        print("TREE width %s" % self.sizeHint().width())


class Viewone(QWidget):
    def __init__(self, par):
        super(Viewone, self).__init__()
        self.parsiz = par
        self.box = QVBoxLayout()
        self.box.setContentsMargins(0, 0, 0, 0)
        self.lab = QLabel()
        self.lab.setText("DATA SERVER:")
        qlabfont = QFont()
        qlabfont.setPointSize(10)
        self.lab.setFont(qlabfont)
        self.viewcontent = DStreeView(self.parsiz)
        self.box.addWidget(self.lab)
        self.box.addWidget(self.viewcontent)
        self.box.addStretch()
        self.setLayout(self.box)


class CustomizeFrame(QFrame):
    def __init__(self):
        super(CustomizeFrame, self).__init__()
        self.setFixedWidth(200)
        print("frame width %s" % self.size().width())
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
