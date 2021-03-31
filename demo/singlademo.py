import sys
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtWidgets import *
from qtpy import QtCore


class LfItem(QListWidget):
    update_ = pyqtSignal(str)

    def __init__(self):
        super(LfItem, self).__init__()
        it1 = QListWidgetItem(self)
        self.sub_bt1 = QPushButton("A")
        self.sub_bt1.clicked.connect(self.onclick)
        self.setItemWidget(it1,self.sub_bt1)

    def onclick(self):
        txt = self.sender().text()  # 获取发送信号的控件文本
        self.update_.emit(txt)

class LF(QWidget):
    def __init__(self):
        super(LF, self).__init__()
        self.setMaximumWidth(150)
        self.setMinimumWidth(150)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        box = QFormLayout()
        self.bt1 = QPushButton()
        self.bt1.setText("按钮")
        self.bt1.setFixedSize(80,23)
        box.addRow(self.bt1)

        self.item_1 = LfItem()
        box.addRow(self.item_1)

        self.bt2 = QPushButton()
        self.bt2.setText("按钮")
        self.bt2.setFixedSize(80,23)
        box.addRow(self.bt2)

        self.item_2 = LfItem()
        box.addRow(self.item_2)

        self.setLayout(box)


class RF(QWidget):
    def __init__(self):
        super(RF, self).__init__()
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)



class Mwindow(QWidget):
    def __init__(self):
        super(Mwindow, self).__init__()
        self.setui()

    def setui(self):
        self.resize(800, 600)
        box = QHBoxLayout()

        self.lf = LF()
        self.lf.setStyleSheet("border-color:#808080;border-width:1px;border-style:solid;")
        self.rf = RF()
        self.rf.setStyleSheet("background-color:yellow;border:1px")

        box.addWidget(self.lf)
        box.addWidget(self.rf)
        self.setLayout(box)
        self.lf.item_1.update_.connect(self.fun)

    def fun(self,str_):
        if str_ == "A":
            print("is A")
            self.rf.setStyleSheet("background-color:red;border:1px")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Mwindow()
    run.show()
    sys.exit(app.exec_())
