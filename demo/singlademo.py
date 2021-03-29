import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *

class LfItem(QWidgetItem):
    def __init__(self):
        super(LfItem, self).__init__()


class LF(QWidget):
    def __init__(self):
        super(LF, self).__init__()


class Mwindow(QWidget):
    def __init__(self):
        super(Mwindow, self).__init__()
        self.setui()

    def setui(self):
        self.resize(800, 600)
        box = QHBoxLayout()
        l =
        box.addWidget()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Mwindow()
    run.show()
    sys.exit(app.exec_())
