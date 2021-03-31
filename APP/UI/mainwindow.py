from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QWidget, QHBoxLayout, QFrame, QLabel, \
    QFormLayout
from .vtoolmenu_info import MENU_INFO
from APP.UI.common import QSSadd
from .modAPI import DrawerVtMenu
from . import upsingle

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
        box = QFormLayout()
        box.setContentsMargins(0, 0, 0, 0)
        self._menu = DrawerVtMenu(MENU_INFO.__menu_info__, height_par=23)
        self._menu.addstyle(QSSadd.readqss("./UI/qss/vtoolmenu.qss"))
        self._menu.settopicon("./source/icon/plus1518%26.svg", "./source/icon/minus1518%26.svg")
        self.s = self._menu.create()
        box.addRow(self.s)
        self.setLayout(box)

    # def fun(self, str_):
    #     print("fun is:")
    #     print(str_)

class Right_Frame_0(QFrame):
    def __init__(self):
        super(Right_Frame_0, self).__init__()
        self.setObjectName("r_frame")
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet(gbqss)


class M_window(QMainWindow):
    appname = "ANA SYS"

    def __init__(self):
        super(M_window, self).__init__()
        self.central_widget = QWidget()
        self.sta_bar = QStatusBar()
        self.mainUI()

    def mainUI(self):
        self.setWindowTitle(M_window.appname)
        self.resize(900,600)
        self.setWindowIcon(QIcon("./source/icon/mianwin5050.svg"))
        self.setCentralWidget(self.central_widget)
        box_0 = QHBoxLayout()
        box_0.setContentsMargins(0,0,0,0)
        self.left_frame = Left_Frame_0()
        self.right_frame = Right_Frame_0()

        box_0.addWidget(self.left_frame)
        box_0.addWidget(self.right_frame)

        self.central_widget.setLayout(box_0)
        self.setstatus_bar()
        self.left_frame.s.itemc.update_.connect(self.fun)

    def fun(self,str_):
        print(str_)

    def setstatus_bar(self):
        self.sta_bar.addWidget(QLabel("程序运行中    "))
        self.setStatusBar(self.sta_bar)


