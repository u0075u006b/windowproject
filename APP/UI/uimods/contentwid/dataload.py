import sys

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QWidget, QGroupBox, QHBoxLayout, QLabel, QPushButton, QLineEdit, QFrame, QApplication, \
    QVBoxLayout


class LocalLoad(QWidget):
    def __init__(self):
        super(LocalLoad, self).__init__()
        self.groupbox = QGroupBox(self)

        # self.wid_0 = QWidget(self.groupbox)
        # self.horizontalLayout_0 = QHBoxLayout(self.wid_0)
        # self.label_0 = QLabel(self.wid_0)
        # self.line_0 = QFrame(self.wid_0)
        # self.pushButton_0_0 = QPushButton(self.wid_0)
        # self.pushButton_0_1 = QPushButton(self.wid_0)
        # self.lineEdit_0_0 = QLineEdit(self.wid_0)

        # self.wid_1 = QWidget(self.groupbox)
        # self.horizontalLayout_1 = QHBoxLayout(self.wid_1)
        # self.label_1 = QLabel(self.wid_1)
        # self.line_1 = QFrame(self.wid_1)
        # self.pushButton_1_0 = QPushButton(self.wid_1)
        # self.pushButton_1_1 = QPushButton(self.wid_1)
        # self.lineEdit_1_0 = QLineEdit(self.wid_1)

        self.setui()

    def setui(self):
        self.groupbox.setGeometry(QRect(30, 30, 661, 221))
        self.groupbox.setTitle("加载本地数据")
        self.vlay = QVBoxLayout(self.groupbox)

        self.wid = QWidget(self.groupbox)
        self.wid.setGeometry(QRect(50, 30, 511, 25))
        self.layo = QHBoxLayout(self.wid)
        self.lab = QLabel("HDF")
        self.lab.setFixedWidth(60)
        self.lab.setAlignment(Qt.AlignCenter)
        self.layo.addWidget(self.lab)
        self.line_0 = QFrame()
        self.line_0.setFixedHeight(12)
        self.line_0.setFrameShape(QFrame.VLine)
        self.line_0.setFrameShadow(QFrame.Sunken)
        self.layo.addWidget(self.line_0)
        self.bt1 = QPushButton("查找")
        self.layo.addWidget(self.bt1)
        self.ledit = QLineEdit()
        self.layo.addWidget(self.ledit)
        self.bt2 = QPushButton("打开")
        self.layo.addWidget(self.bt2)
        self.vlay.addWidget(self.wid)

        self.wid2 = QWidget(self.groupbox)
        self.wid2.setGeometry(QRect(50, 30, 511, 25))
        self.layo2 = QHBoxLayout(self.wid2)
        self.lab2 = QLabel("HDFCC")
        self.lab2.setFixedWidth(60)
        self.lab2.setAlignment(Qt.AlignCenter)
        self.layo2.addWidget(self.lab2)
        self.line_1 = QFrame()
        self.line_1.setFixedHeight(12)
        self.line_1.setFrameShape(QFrame.VLine)
        self.line_1.setFrameShadow(QFrame.Sunken)
        self.layo2.addWidget(self.line_1)
        self.bt2_1 = QPushButton("查找")
        self.layo2.addWidget(self.bt2_1)
        self.ledit2 = QLineEdit()
        self.layo2.addWidget(self.ledit2)
        self.bt2_2 = QPushButton("打开")
        self.layo2.addWidget(self.bt2_2)
        self.vlay.addWidget(self.wid2)

        self.groupbox.setLayout(self.vlay)
        # self.wid_0.setGeometry(QRect(50, 30, 511, 25))

        # self.horizontalLayout_0.setContentsMargins(0, 0, 0, 0)

        # self.label_0 = QLabel(self.wid_0)
        # self.label_0.setObjectName(u"label_2")
        # self.label_0.setText("HDFffffff")
        # self.label_0.setFixedWidth(12)
        #
        # self.horizontalLayout_0.addWidget(self.label_0)
        #
        # self.line_0 = QFrame(self.wid_0)
        # self.line_0.setObjectName(u"line_2")
        # self.line_0.setFrameShape(QFrame.VLine)
        # self.line_0.setFrameShadow(QFrame.Sunken)
        #
        # self.horizontalLayout_0.addWidget(self.line_0)
        #
        # self.pushButton_0_0 = QPushButton(self.wid_0)
        # self.pushButton_0_0.setObjectName(u"pushButton_3")
        #
        # self.horizontalLayout_0.addWidget(self.pushButton_0_0)
        #
        # self.lineEdit_0_0 = QLineEdit(self.wid_0)
        # self.lineEdit_0_0.setObjectName(u"lineEdit_2")
        #
        # self.horizontalLayout_0.addWidget(self.lineEdit_0_0)
        #
        # self.pushButton_0_1 = QPushButton(self.wid_0)
        # self.pushButton_0_1.setObjectName(u"pushButton_4")
        #
        # self.horizontalLayout_0.addWidget(self.pushButton_0_1)

        # self.wid_1.setGeometry(QRect(50, 70, 511, 25))
        #
        # self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        #
        # self.label_1 = QLabel(self.wid_1)
        # self.label_1.setObjectName(u"label_2")
        # self.label_1.setText("TXT")
        #
        # self.horizontalLayout_1.addWidget(self.label_1)

        # self.line_1 = QFrame(self.wid_0)
        # self.line_1.setObjectName(u"line_2")
        # self.line_1.setFrameShape(QFrame.VLine)
        # self.line_1.setFrameShadow(QFrame.Sunken)
        #
        # self.horizontalLayout_1.addWidget(self.line_1)
        #
        # self.pushButton_1_0 = QPushButton(self.wid_1)
        # self.pushButton_1_0.setObjectName(u"pushButton_3")
        #
        # self.horizontalLayout_1.addWidget(self.pushButton_1_0)
        #
        # self.lineEdit_1_0 = QLineEdit(self.wid_0)
        # self.lineEdit_1_0.setObjectName(u"lineEdit_2")
        #
        # self.horizontalLayout_1.addWidget(self.lineEdit_1_0)
        #
        # self.pushButton_1_1 = QPushButton(self.wid_0)
        # self.pushButton_1_1.setObjectName(u"pushButton_4")
        #
        # self.horizontalLayout_1.addWidget(self.pushButton_1_1)



