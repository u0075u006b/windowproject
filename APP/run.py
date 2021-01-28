import sys
from PyQt5.QtWidgets import QApplication
from APP.UI.mainwindow import MainWin


if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = MainWin()
    run.show()
    sys.exit(app.exec_())
