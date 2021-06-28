import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
from APP.UI.mainwindow import M_window
from APP.mianinit import MianInit



def data_server_th(obj):
    obj.thrun()


def init():
    sys_init = MianInit()
    sys_init.sysinit()


if __name__ == "__main__":
    init()
    app = QApplication(sys.argv)
    f = QFont("pingfangSC")
    app.setFont(f)
    # print(app.font().family())
    run = M_window()

    run.show()

    # data_server_th(run)

    sys.exit(app.exec_())
