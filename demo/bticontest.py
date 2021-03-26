from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from qtpy import QtCore


class Qbutton(QPushButton,QApplication):
    idType = QEvent.registerEventType()

    def __init__(self):
        super(Qbutton, self).__init__()
        self.setText("BUTTON")
        self.setFixedSize(120, 20)
        self.setIcon(QIcon("./icon/plus1518%26.svg"))
        self.setCheckable(True)
        self.setChecked(True)
        # self.installEventFilter(self)
        # self.installEventFilter(self)

    # def eventFilter(self, obj, event):
    #     print(event)
    # # def event(self, event):
    # #     if event.type() == event.ApplicationStateChange:
    # #     #     # print(QEvent.DynamicPropertyChange)
    # #         print("event")
    # #     #     print(self.isChecked())
    #     return super().eventFilter(obj,event)

class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self.resize(300,180)
        self.ui()

    def ui(self):
        box = QVBoxLayout()
        self.bt_0 = Qbutton()
        self.bt_0.toggled.connect(lambda : self.p(self.bt_0))
        self.bt_0.toggled.connect(lambda : self.p2(self.bt_0))
        box.addWidget(self.bt_0)
        self.bt_1 = Qbutton()
        self.bt_1.toggled.connect(lambda : self.p(self.bt_1))
        self.bt_1.toggled.connect(lambda : self.p2(self.bt_1))
        box.addWidget(self.bt_1)
        lab = QLabel(self)
        lab.setText("这是文本")
        lab.resize(200,90)
        lab.setStyleSheet("background-color:#C4C2C3;border-color:#808080;border-width:1px;border-style:solid;")
        box.addWidget(lab)
        self.setLayout(box)

    def p(self,b):
        print(b.isChecked())
    #
    def p2(self,b):
        if b.isChecked():
            b.setIcon(QIcon("./icon/plus1518%26.svg"))
        else:
            b.setIcon(QIcon("./icon/minus1518%26.svg"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    r = UI()
    r.show()
    sys.exit(app.exec_())