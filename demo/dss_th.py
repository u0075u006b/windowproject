from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class Min(QWidget):

    def __init__(self):
        super(Min, self).__init__()
        self.resize(800,600)
        self.bt1 = QPushButton("A")
        self.bt2 = QPushButton("A")
        self.bt3 = QPushButton("A")
        self.setui()

    def setui(self):
        self.box = QHBoxLayout()
        self.bt1.resize(40,20)
        self.bt2.resize(40, 20)
        self.bt3.resize(40, 20)
        self.box.addWidget(self.bt1)
        self.box.addWidget(self.bt2)
        self.box.addWidget(self.bt3)
        self.box.addStretch()
        self.setLayout(self.box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    r = Min()
    r.show()
    sys.exit(app.exec_())