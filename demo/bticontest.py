from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from qtpy import QtCore


class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self.resize(300,180)
        bt = QPushButton(self)
        bt.setText("BUTTON")
        bt.setFixedSize(120,20)
        bt.move(10,10)
        bt.setIcon(QIcon("./icon/plus1518%26.svg"))
        bt
        lab = QLabel(self)
        lab.setText("这是文本")
        lab.resize(200,90)
        lab.setStyleSheet("background-color:#C4C2C3;border-color:#808080;border-width:1px;border-style:solid;")
        lab.move(10,40)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    r = UI()
    r.show()
    sys.exit(app.exec_())