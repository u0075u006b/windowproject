import sys
from PyQt5.QtWidgets import QApplication
from APP.UI.mainwindow import M_window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = M_window()
    run.show()
    sys.exit(app.exec_())
