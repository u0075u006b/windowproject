import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar, QFrame, QListWidget,QListWidgetItem,QHBoxLayout, QWidget, QPushButton, QStyle, \
    QFormLayout, QLabel


from PyQt5.QtGui import QIcon




class MainWin(QMainWindow):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setinitUI(self)

    def leftFrame(self):
        #创建FRAME
        leftframe = QFrame(self.centralwidget)
        leftframe.resize(600,130)
        leftframe.setMaximumWidth(130)
        leftframe.setStyleSheet("background-color:green;border:0px")

        l_layout = QFormLayout(self)

        btn_1 = QPushButton("A")
        btn_1.setFixedSize(100,30)#固定尺寸
        btn_1.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap(27)))
        btn_1.clicked.connect(lambda : self.onClick(btn_1.text()))

        btn_2 = QPushButton("B")
        btn_2.setFixedSize(100, 30)
        btn_2.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap(27)))
        btn_2.clicked.connect(lambda : self.onClick(btn_2.text()))

        l_layout.addWidget(btn_1)
        l_layout.addWidget(btn_2)
        leftframe.setLayout(l_layout)
        return leftframe

    def onClick(self,text):
        if text=="A":
            print(text)
            print(self.m_rightframe0.isVisible())
            self.m_rightframe0.setHidden(True)
            self.m_rightframe2.setHidden(True)
            self.m_rightframe1.setVisible(True)
        elif text=="B":
            print(self.m_rightframe0.isVisible())
            self.m_rightframe0.setHidden(True)
            self.m_rightframe1.setHidden(True)
            self.m_rightframe2.setVisible(True)


    def rightFrame_0(self):
        rightframe_0 = QFrame(self.centralwidget)
        rightframe_0.setFrameShape(QFrame.StyledPanel)
        return rightframe_0

    def rightFrame_1(self):
        rightframe_1 = QFrame(self.centralwidget)
        rightframe_1.setStyleSheet("background-color:yellow;border:0px")
        labelis = QLabel("这是rightFrame_1")
        rightframebox = QHBoxLayout(rightframe_1)
        rightframebox.addWidget(labelis)
        rightframe_1.setLayout(rightframebox)
        return rightframe_1

    def rightFrame_2(self):
        rightframe_2 = QFrame(self.centralwidget)
        rightframe_2.setStyleSheet("background-color:yellow;border:0px")
        labelis = QLabel("这是rightFrame_2")
        rightframebox = QHBoxLayout(rightframe_2)
        rightframebox.addWidget(labelis)
        rightframe_2.setLayout(rightframebox)
        return rightframe_2


    def setinitUI(self, MWindow):
        MWindow.setWindowTitle('QSS TEST WINDOW')
        MWindow.resize(800,600)

        self.centralwidget = QWidget(MWindow)
        MWindow.setCentralWidget(self.centralwidget)
        hbox = QHBoxLayout(self.centralwidget)

        self.m_rightframe0 = self.rightFrame_0()
        self.m_rightframe1 = self.rightFrame_1()
        self.m_rightframe1.setHidden(True)
        self.m_rightframe2 = self.rightFrame_2()
        self.m_rightframe2.setHidden(True)
        self.m_leftframe = self.leftFrame()

        hbox.addWidget(self.m_leftframe)
        hbox.addWidget(self.m_rightframe0)
        hbox.addWidget(self.m_rightframe1)
        hbox.addWidget(self.m_rightframe2)

        MWindow.setLayout(hbox)


        self.statusbar = MWindow.statusBar()
        self.statusbar.showMessage("程序运行中")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MainWin()
    m.show()
    sys.exit(app.exec_())


