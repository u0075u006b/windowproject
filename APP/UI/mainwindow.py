from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QPushButton, QApplication, QStyle, QFrame


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
