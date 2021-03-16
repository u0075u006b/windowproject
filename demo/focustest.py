import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QWidget, QHBoxLayout, QFrame, QLabel, QListWidget, \
    QFormLayout, QPushButton, QListWidgetItem



class Mwindow(QMainWindow):
    appname = "主程序"

    def __init__(self):
        super(Mwindow, self).__init__()
        self.central_widget = QWidget()
        self.sta_bar = QStatusBar()
        self.mainUI()

    def mainUI(self):
        self.setWindowTitle("ana SYS")
        self.resize(800,600)
        self.setCentralWidget(self.central_widget)
        box_0 = QHBoxLayout()
        left_frame = QWidget()
        left_frame.setObjectName("left_frame")
        left_frame.setFocusPolicy(Qt.StrongFocus)
        left_frame.setStyleSheet("background-color:rgba(255,255,255,255);border-color:red;border-width:1px;border-style:solid;")
        l_box = QFormLayout()
        lab_0 = QLabel("a")
        lab_1 = QLabel("b")
        lab_2 = QLabel("c")
        l_box.addRow(lab_0)
        l_box.addRow(lab_1)
        l_box.addRow(lab_2)
        left_frame.setLayout(l_box)
        right_frame = QWidget()
        right_frame.setObjectName("right_frame")
        right_frame.setFocusPolicy(Qt.StrongFocus)
        right_frame.setStyleSheet("background-color:rgba(255,255,255,255);border-color:red;border-width:1px;border-style:solid;")

        box_0.addWidget(left_frame)
        box_0.addWidget(right_frame)

        self.central_widget.setLayout(box_0)
        self.setstatus_bar()

    def setstatus_bar(self):
        self.sta_bar.addWidget(QLabel("程序运行中"))
        self.setStatusBar(self.sta_bar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = Mwindow()
    m.show()
    print(m.focusPolicy())
    sys.exit(app.exec_())


