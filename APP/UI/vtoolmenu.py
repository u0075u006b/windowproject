from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QWidget, QHBoxLayout, QFrame, QLabel, QListWidget, \
    QFormLayout, QPushButton, QListWidgetItem,QCheckBox


class ItemWidget(QWidget):

    def __init__(self, item, factor):
        super(ItemWidget, self).__init__()
        self.item = item

        self.lay = QFormLayout(self)
        self.lay.setContentsMargins(3,5,0,5)
        self.lay.setSpacing(0)
        self.lay.setVerticalSpacing(3)
        self.bt1 = QPushButton("A")
        self.setStyleSheet('QPushButton {background-color:'
                           'qlineargradient(spread:pad, x1:0, x2:0, y1:0, y2:1, stop: 0 rgba(220,220,220,255),stop: 0.4 rgba(224,224,224,255),stop: 1 rgba(156,156,156,255));'
                           'border-color:#808080;border-width:1px;border-style:solid;} '
                           'QPushButton:pressed {background-color:#C4C2C3;border-color:#808080;border-width:1px;border-style:solid;}')
        self.bt1.setFixedHeight(20)
        self.lay.addWidget(self.bt1)
        # print(self.lay.sizeHint())
        self.bt2 = QPushButton("B")
        self.setStyleSheet('QPushButton {background-color:'
                           'qlineargradient(spread:pad, x1:0, x2:0, y1:0, y2:1, stop: 0 rgba(220,220,220,255),stop: 0.4 rgba(224,224,224,255),stop: 1 rgba(156,156,156,255));'
                           'border-color:#808080;border-width:1px;border-style:solid;} '
                           'QPushButton:pressed {background-color:#C4C2C3;border-color:#808080;border-width:1px;border-style:solid;}')
        self.bt2.setFixedHeight(20)
        self.lay.addWidget(self.bt2)
        # print(self.lay.sizeHint())

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(ItemWidget, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.lay.sizeHint().height()))


class TopButton(QPushButton):
    def __init__(self, item, name):
        super(TopButton, self).__init__()
        self.item = item
        self.setCheckable(True) # 设置可选中
        self.setChecked(True)
        self.setText(name)
        self.setIcon(QIcon("./source/icon/plus1518%26.svg"))

        self.setFixedHeight(24)
        self.setStyleSheet('QPushButton {background-color:'
                           'qlineargradient(spread:pad, x1:0, x2:0, y1:0, y2:1, stop: 0 rgba(255,255,255,255),stop: 0.4 rgba(240,240,240,255),stop: 1 rgba(180,180,180,255));'
                           'border-color:#808080;border-width:1px;border-style:solid;} '
                           'QPushButton:pressed {background-color:#C4C2C3;border-color:#808080;border-width:1px;border-style:solid;}')

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(TopButton, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))


class LeftItem(QListWidget):
    def __init__(self,btname,listname):
        super(LeftItem, self).__init__()
        self.btname = btname
        self.itemlist = listname
        self.setStyleSheet("border:0px")

        self.top = QListWidgetItem(self)
        self.btn = TopButton(self.top,self.btname)
        self.setItemWidget(self.top,self.btn)

        self.sub_item = QListWidgetItem(self)
        self.btn.toggled.connect(self.sub_item.setHidden)
        self.f = ItemWidget(self.sub_item, self.itemlist)
        self.setItemWidget(self.sub_item,self.f)
        self.sub_item.setHidden(True)

        self.top = QListWidgetItem(self)
        self.btn = TopButton(self.top,self.btname)
        self.setItemWidget(self.top,self.btn)

        self.sub_item = QListWidgetItem(self)
        self.btn.toggled.connect(self.sub_item.setHidden)
        self.f = ItemWidget(self.sub_item, self.itemlist)
        self.setItemWidget(self.sub_item,self.f)
        self.sub_item.setHidden(True)
