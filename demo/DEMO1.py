import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar, QFrame, QHBoxLayout, QWidget, QPushButton,QStyle
from PyQt5.QtGui import QIcon


class MainWin(QMainWindow):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setinitUI(self)


    def setinitUI(self, MWindow):
        MWindow.setWindowTitle('QSS TEST WINDOW')
        MWindow.resize(800,600)

        self.centralwidget = QWidget(MWindow)
        MWindow.setCentralWidget(self.centralwidget)
        hbox = QHBoxLayout(self.centralwidget)

        btn_1 = QPushButton("A")
        btn_1.setFixedSize(100,30)#固定尺寸
        btn_1.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap(27)))

        btn_2 = QPushButton("B")
        btn_2.setFixedSize(100, 30)
        btn_2.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap(27)))

        hbox.addWidget(btn_1)
        hbox.addWidget(btn_2)
        MWindow.setLayout(hbox)

        self.statusbar = MWindow.statusBar()
        self.statusbar.showMessage("程序运行重")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MainWin()
    m.show()
    sys.exit(app.exec_())


