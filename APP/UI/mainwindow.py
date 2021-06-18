from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QWidget, QHBoxLayout, QVBoxLayout, QFrame, QLabel, \
    QFormLayout, QPushButton
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
        box = QFormLayout()
        self.lab = QLabel()
        self.lab.setText("初始")
        box.addWidget(self.lab)
        self.setLayout(box)


class Rside_Frame_0(QFrame):
    def __init__(self):
        super(Rside_Frame_0, self).__init__()
        self.setObjectName("rside_frame")
        self.setMaximumWidth(300)
        self.setMinimumWidth(300)
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet(gbqss)


        # _box = QFormLayout(self)
        # _box.setContentsMargins(0,0,0,0)
        # _box.setSpacing(0)
        # self.wd = QPushButton()
        # self.wd.setCheckable(True)
        # self.wd.setChecked(True)
        # self.wd.setFixedHeight(20)
        # self.wd.setText("ceshi")
        # _box.addRow(self.wd)
        # self.s_obj = QLabel()
        #
        # self.s_obj.resize(250,250)
        # self.s_obj.setText("zjedwodasbg,wondbueo\n,woidwho,\nweodeda!!!")
        # self.s_obj.setHidden(True)
        # _box.addRow(self.s_obj)
        # self.wd.toggled.connect(self.s_obj.setHidden)
        #
        # self.wd = QPushButton()
        # self.wd.setCheckable(True)
        # self.wd.setFixedHeight(20)
        # self.wd.setText("ceshi")
        # _box.addRow(self.wd)
        # self.s_obj = QLabel()
        #
        # self.s_obj.resize(250,250)
        # self.s_obj.setText("zjedwodasbg,wondbueo\n,woidwho,\nweodeda!!!")
        # self.s_obj.setHidden(True)
        # _box.addRow(self.s_obj)
        # self.wd.toggled.connect(self.s_obj.setHidden)
        #
        # self.setLayout(_box)


class M_window(QMainWindow):
    appname = "ANA SYS"

    def __init__(self):
        super(M_window, self).__init__()
        self.central_widget = QWidget()
        self.sta_bar = QStatusBar()
        self.left_frame = Left_Frame_0()
        self.right_frame = Right_Frame_0()
        self.rside_frame = Rside_Frame_0()
        self.mainUI()

    def mainUI(self):
        self.setWindowTitle(M_window.appname)
        self.resize(900,600)
        # self.setWindowIcon(QIcon("./source/icon/mianwin5050.svg"))
        self.setCentralWidget(self.central_widget)
        box_0 = QHBoxLayout()
        box_0.setContentsMargins(0,0,0,0)

        box_0.addWidget(self.left_frame)
        box_0.addWidget(self.right_frame)
        box_0.addWidget(self.rside_frame)

        self.central_widget.setLayout(box_0)
        self.setstatus_bar()

        self.left_frame.s.item_0.update_.connect(self.fun)
        self.left_frame.s.item_1.update_.connect(self.fun)
        self.left_frame.s.item_2.update_.connect(self.fun)

    def fun(self,str_):
        print(str_)
        self.right_frame.lab.setText(str_)

    def setstatus_bar(self):
        self.sta_bar.addWidget(QLabel("程序运行中    "))
        self.setStatusBar(self.sta_bar)


