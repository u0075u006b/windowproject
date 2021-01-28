# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwidow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.splitter_2)
        self.treeWidget_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_2.sizePolicy().hasHeightForWidth())
        self.treeWidget_2.setSizePolicy(sizePolicy)
        self.treeWidget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.treeWidget_2.setMidLineWidth(-4)
        self.treeWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.treeWidget_2.setProperty("showDropIndicator", True)
        self.treeWidget_2.setDragEnabled(False)
        self.treeWidget_2.setDragDropOverwriteMode(False)
        self.treeWidget_2.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.treeWidget_2.setAlternatingRowColors(False)
        self.treeWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.treeWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.treeWidget_2.setIndentation(20)
        self.treeWidget_2.setRootIsDecorated(True)
        self.treeWidget_2.setUniformRowHeights(False)
        self.treeWidget_2.setItemsExpandable(True)
        self.treeWidget_2.setAnimated(False)
        self.treeWidget_2.setAllColumnsShowFocus(False)
        self.treeWidget_2.setWordWrap(False)
        self.treeWidget_2.setHeaderHidden(True)
        self.treeWidget_2.setExpandsOnDoubleClick(True)
        self.treeWidget_2.setObjectName("treeWidget_2")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        brush_b = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush_b.setStyle(QtCore.Qt.SolidPattern)
        item_0.setBackground(0, brush_b)
        brush_f = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush_f.setStyle(QtCore.Qt.SolidPattern)
        item_0.setForeground(0, brush_f)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        brush = QtGui.QBrush(QtGui.QColor(191, 191, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item_0.setBackground(0, brush)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        brush = QtGui.QBrush(QtGui.QLinearGradient())
        brush.setStyle(QtCore.Qt.SolidPattern)
        item_0.setBackground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item_1.setFont(0, font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../素材/cycxtb/cycxtb 005.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item_1.setIcon(0, icon)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_1.setBackground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_1.setForeground(0, brush)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        self.treeWidget_2.header().setVisible(False)
        self.treeWidget_2.header().setCascadingSectionResizes(False)
        self.treeWidget_2.header().setDefaultSectionSize(100)
        self.treeWidget_2.header().setHighlightSections(False)
        self.treeWidget_2.header().setSortIndicatorShown(False)
        self.horizontalLayout.addWidget(self.splitter_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet("QToolBar{\n"
"background-color:rgb(241, 241, 241);\n"
"}")
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionone = QtWidgets.QAction(MainWindow)
        self.actionone.setCheckable(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../.designer/APP/icon/001.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionone.setIcon(icon1)
        self.actionone.setObjectName("actionone")
        self.actiontow = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../.designer/APP/icon/001.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiontow.setIcon(icon2)
        self.actiontow.setObjectName("actiontow")
        self.actionSTART = QtWidgets.QAction(MainWindow)
        self.actionSTART.setObjectName("actionSTART")
        self.actionONE = QtWidgets.QAction(MainWindow)
        self.actionONE.setObjectName("actionONE")
        self.actionTOW = QtWidgets.QAction(MainWindow)
        self.actionTOW.setObjectName("actionTOW")
        self.actionhow = QtWidgets.QAction(MainWindow)
        self.actionhow.setObjectName("actionhow")
        self.menuFile.addAction(self.actionSTART)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionONE)
        self.menuFile.addAction(self.actionTOW)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionhow)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.toolBar.addAction(self.actionone)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actiontow)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "1"))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("MainWindow", "项目C"))
        self.treeWidget_2.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(0).child(4).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("MainWindow", "项目B"))
        self.treeWidget_2.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(2).setText(0, _translate("MainWindow", "项目A"))
        self.treeWidget_2.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(3).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(3).child(1).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(4).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(4).child(0).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(5).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(5).child(0).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(6).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(6).child(0).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(7).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(7).child(0).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(8).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(8).child(0).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(8).child(1).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(8).child(2).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget_2.topLevelItem(9).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(10).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(11).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(12).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.topLevelItem(13).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionone.setText(_translate("MainWindow", "one"))
        self.actionone.setIconText(_translate("MainWindow", "one"))
        self.actionone.setToolTip(_translate("MainWindow", "one"))
        self.actiontow.setText(_translate("MainWindow", "tow"))
        self.actiontow.setToolTip(_translate("MainWindow", "tow"))
        self.actionSTART.setText(_translate("MainWindow", "START"))
        self.actionONE.setText(_translate("MainWindow", "ONE"))
        self.actionTOW.setText(_translate("MainWindow", "TOW"))
        self.actionhow.setText(_translate("MainWindow", "how"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Ui_MainWindow()
    demo.show()
    sys.exit(app.exec_())