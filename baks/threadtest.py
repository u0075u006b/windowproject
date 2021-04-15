from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time


class ThreadOne(QThread):
    s1 = pyqtSignal(str)

    def __init__(self):
        super(ThreadOne, self).__init__()
        self.th_on = True

    def run(self):
        f = 30
        self.textnum = 0
        while f >0 and self.th_on:
            f = f -1
            self.textnum += 1
            self.textstr = str(self.textnum)
            self.siem(self.textstr)
            self.msleep(500)

    def siem(self,str):
        self.s1.emit(str)


class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self._connect1 = QTextBrowser(self)
        self._connect2 = QTextBrowser(self)
        self.bt1 = QPushButton(self)
        self.bt2 = QPushButton(self)
        self.bt3 = QPushButton(self)
        self.t1 = ThreadOne()
        self.ui()

    def ui(self):
        self.resize(300,220)
        self.bt1.setFixedSize(80,25)
        self.bt1.setText("RUN")
        self.bt2.setFixedSize(80,25)
        self.bt2.setText("STOP")
        self.bt2.move(0,27)
        self.bt3.setFixedSize(80,25)
        self.bt3.setText("PAUSE")
        self.bt3.move(0,54)
        self._connect1.setFixedSize(200,170)
        self._connect1.move(90,0)
        self._connect1.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self._connect2.setFixedSize(290,40)
        self._connect2.move(0,180)
        self._connect2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.bt1.clicked.connect(self.t1run)
        self.bt2.clicked.connect(self.t1stop)
        self.bt3.clicked.connect(self.t1pause)

        self.t1.s1.connect(self.addtext)
        self.t1.started.connect(lambda :print("启动了"))
        self.t1.finished.connect(lambda: print("结束了"))

    def t1run(self):
        print("1:",self.t1.isRunning())
        self.t1.th_on = True
        self.t1.start()
        print("2:",self.t1.isRunning())
        print(int(self.t1.currentThreadId()))

    def t1pause(self):
        self.t1.awit()
        print("t1pause:", self.t1.isRunning())

    def t1stop(self):
        self.t1.th_on = False
        self.t1.exit(0)
        print("t1end:",self.t1.isRunning())

    def addtext(self,_str):
        self._connect1.append(_str)
        self._connect2.append(str(self.t1.isRunning()))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    r = UI()
    r.show()
    sys.exit(app.exec_())