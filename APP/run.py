import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
from APP.UI.mainwindow import M_window




if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = M_window()
    run.show()
    f = QFont("pingfangSC")
    app.setFont(f)
    print(app.font().family())
    sys.exit(app.exec_())
