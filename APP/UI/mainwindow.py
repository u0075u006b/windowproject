from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QPushButton, QApplication, QStyle, QFrame,QFormLayout

class LeftWidget(QWidget):

    top = ['BUTTON 1', 'BUTTON 2', 'BUTTON 3']
    tab_1 = ['bt1_1', 'bt1_2', 'bt1_3']
    tab_2 = ['bt2_1', 'bt2_2', 'bt2_3']
    tab_3 = ['bt3_1', 'bt3_2', 'bt3_3']

    def __init__(self, item, factor):
        super().__init__()
        self.item = item
        layout = QFormLayout(self)
        self.button1 = QPushButton(factor[0])
        layout.addRow(self.button1)
        self.button1.clicked.connect(self.onClick)
        if len(factor) >= 3:
            self.button2 = QPushButton(factor[1])
            self.button3 = QPushButton(factor[2])
            layout.addRow(self.button2)
            layout.addRow(self.button3)
            self.button2.clicked.connect(self.onClick)
            self.button3.clicked.connect(self.onClick)
            if len(factor) >= 4:
                self.button4 = QPushButton(factor[3])
                layout.addRow(self.button4)
                self.button4.clicked.connect(self.onClick)

    def onClick(self):
        txt = self.sender().text()  # 获取发送信号的控件文本
        self.update_.emit(txt)

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(LeftWidget, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))



class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setinitUI()

    def leftFrame(self):
        #创建FRAME
        leftframe = QFrame(self.centralwidget)
        leftframe.resize(600,130)
        leftframe.setMaximumWidth(130)
        leftframe.setStyleSheet("background-color:green;border:0px")
        return leftframe

    def rightFrame(self):
        rightframe = QFrame(self.centralwidget)
        rightframe.setStyleSheet("background-color:yellow;border:0px")
        return rightframe

    def setinitUI(self):
        self.setWindowTitle('QSS TEST WINDOW')
        self.resize(800, 600)

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        hbox = QHBoxLayout(self.centralwidget)

        self.m_leftframe = self.leftFrame()
        self.m_rightframe = self.rightFrame()


        hbox.addWidget(self.m_leftframe)
        hbox.addWidget(self.m_rightframe)
        self.setLayout(hbox)

        self.statusbar = self.statusBar()
        self.statusbar.showMessage("程序运行中")
