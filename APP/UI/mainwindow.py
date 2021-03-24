from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QWidget, QHBoxLayout, QFrame, QLabel, \
    QFormLayout
from .vtoolmenu_info import MENU_INFO
from APP.UI.common import QSSadd
from .modAPI import DrawerVtMenu


class Left_Frame_0(QFrame):
    def __init__(self):
        super(Left_Frame_0, self).__init__()
        self.setMaximumWidth(150)
        self.setMinimumWidth(150)
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet("background-color:rgba(255,255,255,255)")
        self.setContentsMargins(0,0,0,0)
        box = QFormLayout()
        box.setContentsMargins(0,0,0,0)
        _menu = DrawerVtMenu(MENU_INFO.__menu_info__,height_par=23)
        _menu.addstyle(QSSadd.readqss("./UI/qss/vtoolmenu.qss"))
        _menu.settopicon("./source/icon/plus1518%26.svg", "./source/icon/minus1518%26.svg")
        s = _menu.create()
        box.addRow(s)
        self.setLayout(box)


class Right_Frame_0(QFrame):
    def __init__(self):
        super(Right_Frame_0, self).__init__()
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet("background-color:rgba(200,200,200,255)")

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
        left_frame = Left_Frame_0()
        right_frame = Right_Frame_0()

        box_0.addWidget(left_frame)
        box_0.addWidget(right_frame)

        self.central_widget.setLayout(box_0)
        self.setstatus_bar()

    def setstatus_bar(self):
        self.sta_bar.addWidget(QLabel("程序运行中    "))
        self.setStatusBar(self.sta_bar)
