import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from APP.UI.common import QSSadd

menulist = ["A","B","C"]

class M_window(QMainWindow,QWidget):
    update_ = pyqtSignal(str)
    appname = "ANA SYS"

    def __init__(self):
        super(M_window, self).__init__()
        self.update_.connect(self.fun)
        self.central_widget = QWidget()
        self.sta_bar = QStatusBar()
        self.mainUI()

    def mainUI(self):
        self.setWindowTitle(M_window.appname)
        self.resize(900,600)
        # self.setWindowIcon(QIcon("./source/icon/mianwin5050.svg"))
        self.setCentralWidget(self.central_widget)
        box_0 = QHBoxLayout()
        self.leftwidget = QWidget()
        self.leftwidget.setFixedWidth(100)
        self.leftwidget.setStyleSheet("background-color:#C4C2C3;")
        leftlay = QFormLayout()
        for _i in menulist:
            bt = QPushButton(_i)
            bt.setObjectName(_i)
            bt.setIcon(QIcon("./icon/plus1518%26.svg"))
            bt.clicked.connect(self.onClick)
            leftlay.addRow(bt)
        self.leftwidget.setLayout(leftlay)
        self.rightwidget = QWidget()
        self.rightwidget.setStyleSheet("background-color:white;")

        box_0.addWidget(self.leftwidget)
        box_0.addWidget(self.rightwidget)

        self.central_widget.setLayout(box_0)
        self.setstatus_bar()

    def onClick(self):
        txt = self.sender().objectName()  # 获取发送信号的控件文本
        self.update_.emit(txt)

    def fun(self,str_):
        print("fun is:")
        print(str_)
        # f_la = QHBoxLayout()
        # self.rmlayitems(str_,f_la)

        self.rmlay(str_)

    def setstatus_bar(self):
        self.sta_bar.addWidget(QLabel("程序运行中    "))
        self.setStatusBar(self.sta_bar)

    # def rmlay(self,s):
    #     _str = s
    #     if _str == "A":
    #         self.rightwidget.setStyleSheet("background-color:red;")
    #         if self.rightwidget.layout() is not None:
    #             print(self.rightwidget.layout())
    #             print(self.rightwidget.layout().count())
    #             for i in range(self.rightwidget.layout().count()):
    #                 self.rightwidget.layout().itemAt(i).widget().deleteLater()
    #             QObjectCleanupHandler().add(self.rightwidget.layout())
    #             print("------------------------")
    #             print(self.rightwidget.layout())
    #             s = QObjectCleanupHandler().isEmpty()
    #             print(s)
    #
    #             # for i in range(0,self.rightwidget.layout().count()):
    #             #     print(self.rightwidget.layout().itemAt(i).widget())
    #             _la = QVBoxLayout()
    #             for i in range(2):
    #                 tx = QLabel(_str)
    #                 tx.setStyleSheet('color:white;font:bold 50px;')
    #                 _la.addWidget(tx)
    #             self.rightwidget.setLayout(_la)
    #             self.rightwidget.update()
    #         else:
    #             print(self.rightwidget.layout())
    #             _la = QHBoxLayout()
    #             for i in range(3):
    #                 tx = QLabel(_str)
    #                 tx.setStyleSheet('color:white;font:bold 50px;')
    #                 _la.addWidget(tx)
    #             self.rightwidget.setLayout(_la)
    #
    #     elif _str == "B":
    #         self.rightwidget.setStyleSheet("background-color:yellow;")
    #
    #     elif _str == "C":
    #         self.rightwidget.setStyleSheet("background-color:blue;")
    #
    #     else:
    #         pass

    def rmlay(self,s):
        _str = s
        if _str == "A":
            self.rightwidget.setStyleSheet("background-color:red;")

        elif _str == "B":
            self.rightwidget.setStyleSheet("background-color:yellow;")

        elif _str == "C":
            self.rightwidget.setStyleSheet("background-color:blue;")

        else:
            pass

    def rmlayitems(self,s,lay):
        _str = s
        _la = lay
        if _str=="A":
            self.rightwidget.setStyleSheet("background-color:red;")

        elif _str=="B":
            self.rightwidget.setStyleSheet("background-color:yellow;")

        elif _str=="C":
            self.rightwidget.setStyleSheet("background-color:blue;")
        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = M_window()
    run.show()
    sys.exit(app.exec_())


"""
        if _str=="A":
            self.rightwidget.setStyleSheet("background-color:red;")
            print(self.rightwidget.layout())
            if self.rightwidget.layout() is not None:
                print(self.rightwidget.layout().count())
            else:
                pass

            for i in range(3):
                tx = QLabel(_str)
                tx.setStyleSheet('color:white;font:bold 50px;')
                _la.addWidget(tx)
            self.rightwidget.setLayout(_la)
        elif _str=="B":
            self.rightwidget.setStyleSheet("background-color:yellow;")
            print(self.rightwidget.layout())

            _la = self.rightwidget.layout()
            print(_la.count())
            for i in range(_la.count()):
                _la.itemAt(i).widget().deleteLater()
            for i in range(3):
                tx = QLabel(_str)
                tx.setStyleSheet('color:white;font:bold 50px;')
                _la.addWidget(tx)
            self.rightwidget.setLayout(_la)
        elif _str=="C":
            self.rightwidget.setStyleSheet("background-color:blue;")
            print(self.rightwidget.layout())
            _la = self.rightwidget.layout()
            print(_la.count())
            for i in range(_la.count()):
                _la.itemAt(i).widget().deleteLater()
            for i in range(3):
                tx = QLabel(_str)
                tx.setStyleSheet('color:white;font:bold 10px;')
                _la.addWidget(tx)
            self.rightwidget.setLayout(_la)
        else:
            pass
"""

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerNtmHMD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *
#
#
# class Ui_Form(object):
#     def setupUi(self, Form):
#         if not Form.objectName():
#             Form.setObjectName(u"Form")
#         Form.resize(1027, 752)
#         self.groupBox = QGroupBox(Form)
#         self.groupBox.setObjectName(u"groupBox")
#         self.groupBox.setGeometry(QRect(30, 60, 661, 121))
#         self.layoutWidget = QWidget(self.groupBox)
#         self.layoutWidget.setObjectName(u"layoutWidget")
#         self.layoutWidget.setGeometry(QRect(50, 70, 511, 25))
#         self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
#         self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
#         self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
#         self.label_2 = QLabel(self.layoutWidget)
#         self.label_2.setObjectName(u"label_2")
#
#         self.horizontalLayout_2.addWidget(self.label_2)
#
#         self.line_2 = QFrame(self.layoutWidget)
#         self.line_2.setObjectName(u"line_2")
#         self.line_2.setFrameShape(QFrame.VLine)
#         self.line_2.setFrameShadow(QFrame.Sunken)
#
#         self.horizontalLayout_2.addWidget(self.line_2)
#
#         self.pushButton_3 = QPushButton(self.layoutWidget)
#         self.pushButton_3.setObjectName(u"pushButton_3")
#
#         self.horizontalLayout_2.addWidget(self.pushButton_3)
#
#         self.lineEdit_2 = QLineEdit(self.layoutWidget)
#         self.lineEdit_2.setObjectName(u"lineEdit_2")
#
#         self.horizontalLayout_2.addWidget(self.lineEdit_2)
#
#         self.pushButton_4 = QPushButton(self.layoutWidget)
#         self.pushButton_4.setObjectName(u"pushButton_4")
#
#         self.horizontalLayout_2.addWidget(self.pushButton_4)
#
#         self.widget = QWidget(self.groupBox)
#         self.widget.setObjectName(u"widget")
#         self.widget.setGeometry(QRect(50, 30, 511, 25))
#         self.horizontalLayout = QHBoxLayout(self.widget)
#         self.horizontalLayout.setObjectName(u"horizontalLayout")
#         self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
#         self.label = QLabel(self.widget)
#         self.label.setObjectName(u"label")
#
#         self.horizontalLayout.addWidget(self.label)
#
#         self.line = QFrame(self.widget)
#         self.line.setObjectName(u"line")
#         self.line.setFrameShape(QFrame.VLine)
#         self.line.setFrameShadow(QFrame.Sunken)
#
#         self.horizontalLayout.addWidget(self.line)
#
#         self.pushButton = QPushButton(self.widget)
#         self.pushButton.setObjectName(u"pushButton")
#
#         self.horizontalLayout.addWidget(self.pushButton)
#
#         self.lineEdit = QLineEdit(self.widget)
#         self.lineEdit.setObjectName(u"lineEdit")
#
#         self.horizontalLayout.addWidget(self.lineEdit)
#
#         self.pushButton_2 = QPushButton(self.widget)
#         self.pushButton_2.setObjectName(u"pushButton_2")
#
#         self.horizontalLayout.addWidget(self.pushButton_2)
#
#
#         self.retranslateUi(Form)
#
#         QMetaObject.connectSlotsByName(Form)
#     # setupUi
#
#     def retranslateUi(self, Form):
#         Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#         self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u52a0\u8f7d\u672c\u5730\u6570\u636e", None))
#         self.label_2.setText(QCoreApplication.translate("Form", u"Txt ", None))
#         self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u52a0\u8f7d\u8def\u5f84", None))
#         self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u663e\u793a", None))
#         self.label.setText(QCoreApplication.translate("Form", u"HDF5", None))
#         self.pushButton.setText(QCoreApplication.translate("Form", u"\u52a0\u8f7d\u8def\u5f84", None))
#         self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u663e\u793a", None))
#     # retranslateUi
#
#
#
#
#
#
