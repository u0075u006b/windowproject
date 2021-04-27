import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal
from PyQt5.QtWidgets import *

class DataS:
    dic1 = {
        'R1':[True,"192.168.1.1","800MB"],
        'R2':[False, None, "NULL"],
        'R3':[True, "127.0.0.1", "1000MB"],
    }


class Qthrun(QThread):
    s1 = pyqtSignal(str)

    def __init__(self):
        super(Qthrun, self).__init__()
        # self.dic = DataS.dic1
        self.on_flag = True

    def run(self):
        while self.on_flag is True:
            print("on_flag %s" % self.on_flag)
            self.sld = QSlider()
            self.sld.valueChanged()
            self.sleep(1)

    def p(self):
        print(self.on_flag)


class Qwin(QWidget):
    def __init__(self):
        super(Qwin, self).__init__()
        self.box = QFormLayout()
        self.w1 = QListWidget(self)
        self.btn_run = QPushButton()
        self.treewd = QTreeWidget()
        self.text = QTextBrowser()
        self.ui()

    def ui(self):
        self.resize(600,500)
        m_box = QVBoxLayout()
        bt_box = QHBoxLayout()

        self.btn_run.setText("QTHREAD Run")
        self.btn_run.setFixedSize(100,80)
        self.btn_run.setCheckable(True)
        self.btn_run.setStyleSheet("background-color:green;color:white")
        self.btn_run.clicked.connect(self.clkrun)

        self.btn_run.setText("QTHREAD Pause")
        self.btn_run.setFixedSize(100,80)
        self.btn_run.setCheckable(True)
        self.btn_run.setStyleSheet("background-color:green;color:white")

        bt_box.addWidget(self.btn_run)
        self.box.addRow(bt_box)

        self.box.addRow(m_box)



    #     self.item1 = QListWidgetItem(self.w1)
    #     self.w1.setItemWidget(self.item1,self.ckb)
    #     self.w1.addItem(self.item1)
    #
    #     self.ckw.setFrameShape(QFrame.Box)
    #     self.ckw.setFrameShadow(QFrame.Sunken)
    #     self.ckw.setText("本实例实现了在工具栏上设置字体,字号大小,加粗,斜体,下划线以及字体颜色等格式属性的功能,代码如下: # -*- coding: utf-8 -*- fromPyQt4.QtGuiimport* fro")
    #     self.item2 = QListWidgetItem(self.w1)
    #     self.item2.setSizeHint(QSize(180,300))
    #     self.w1.setItemWidget(self.item2,self.ckw)
    #     self.w1.addItem(self.item2)
    #     # self.ckb.setLayoutDirection(Qt.RightToLeft)
    #     self.box.addRow(self.w1)
    #     self.setLayout(self.box)
    #
    #     self.ckb.clicked.connect(self.clk)
    #
    #     # self.w1.setFixedWidth(180)
    # def clkrun(self):
    #     print("item is clicked")
    #     print(self.ckb.isChecked())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    r = Qwin()
    r.show()
    # f = QFont()
    app.setFont(QFont("Times New Roman, SimSun, SimSun-ExtB, YouYuan"))
    # f.setFamily("YouYuan")
    # print(f.family())
    print(app.font().family())
    sys.exit(app.exec_())