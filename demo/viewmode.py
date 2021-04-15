import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Qwin(QWidget):
    def __init__(self):
        super(Qwin, self).__init__()
        self.box = QFormLayout()
        self.w1 = QListWidget(self)
        self.w2 = QListWidget(self)
        self.ui(self)

    def ui(self):
        self.resize(200,500)
        self.w1.setFixedWidth(180)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    r = Qwin()
    r.show()
    sys.exit(app.exec_())