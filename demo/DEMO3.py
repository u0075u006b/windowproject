import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QWidget, QHBoxLayout, QFrame, QLabel, QListWidget, \
    QFormLayout, QPushButton, QListWidgetItem


class ItemWidget(QWidget):

    def __init__(self, item, factor):
        super(ItemWidget, self).__init__()
        self.item = item

        self.lay = QFormLayout(self)
        self.lay.setContentsMargins(0,5,0,5)
        self.lay.setSpacing(0)
        self.lay.setVerticalSpacing(3)
        self.bt1 = QPushButton("A")
        self.bt1.setFixedHeight(20)
        self.lay.addWidget(self.bt1)
        print(self.lay.sizeHint())#
        self.bt2 = QPushButton("B")
        self.bt2.setFixedHeight(20)
        self.lay.addWidget(self.bt2)
        print(self.lay.sizeHint())#



    def resizeEvent(self, event):
        # 解决item的高度问题
        super(ItemWidget, self).resizeEvent(event)
        print("-----------------------")
        print(self.height())
        self.item.setSizeHint(QSize(self.minimumWidth(), self.lay.sizeHint().height()))
        print("执行SIZESET")

    # def onClick(self):
    #     txt = self.sender().text()  # 获取发送信号的控件文本
    #     self.update_.emit(txt)


class TopButton(QPushButton):
    def __init__(self, item, name):
        super(TopButton, self).__init__()
        self.item = item
        self.setCheckable(True) # 设置可选中
        self.setChecked(True)
        self.setText(name)
        self.setFixedHeight(22)

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(TopButton, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))

class LeftItem(QListWidget):
    def __init__(self,btname,listname):
        super(LeftItem, self).__init__()
        self.btname = btname
        self.itemlist = listname

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
        self.f = ItemWidget(self.sub_item, self.itemlist)
        self.setItemWidget(self.sub_item,self.f)





        # self.sub_item = QListWidgetItem(self)
        # self.f = ItemWidget(self.sub_item, self.itemlist)
        # self.setItemWidget(self.sub_item,self.f)

        # self.f = QListWidget()
        # self.f_0 = QListWidgetItem(self.f)
        # self.sub_item_0 = QPushButton(self.itemlist[0])
        # self.f.setItemWidget(self.f_0,self.sub_item_0)
        #
        # self.f_1 = QListWidgetItem(self.f)
        # self.sub_item_1 = QPushButton(self.itemlist[1])
        # self.f.setItemWidget(self.f_1,self.sub_item_1)
        #
        # self.f_2 = QListWidgetItem(self.f)
        # self.sub_item_2 = QPushButton(self.itemlist[2])
        # self.f.setItemWidget(self.f_2,self.sub_item_2)
        # print(self.sub_item_2.size().height())
        #
        # self.sub_item.setSizeHint(QSize(self.minimumWidth(), self.sub_item_0.size().height()+self.sub_item_1.size().height()+self.sub_item_2.size().height()))


class Left_Frame_0(QFrame):
    def __init__(self):
        super(Left_Frame_0, self).__init__()
        self.setMaximumWidth(200)
        self.setMinimumWidth(200)
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet("background-color:rgba(255,255,255,255)")
        box = QFormLayout()
        t_item_0 = LeftItem("TOPBTT1",['bt1','bt2','bt3'])
        box.addRow(t_item_0)
        self.setLayout(box)


class Right_Frame_0(QFrame):
    def __init__(self):
        super(Right_Frame_0, self).__init__()
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet("background-color:rgba(200,200,200,255)")

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
        left_frame = Left_Frame_0()
        right_frame = Right_Frame_0()

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
    sys.exit(app.exec_())



'''
    def __init__(self, item, factor):
        super(ItemWidget, self).__init__()
        self.item = item
        self.l1 = QListWidgetItem(self)
        self.bt1 = QPushButton("A")
        self.setItemWidget(self.l1,self.bt1)
        self.l2 = QListWidgetItem(self)
        self.bt2 = QPushButton("B")
        self.setItemWidget(self.l2,self.bt2)
        print(self.width())


    def resizeEvent(self, event):
        # 解决item的高度问题
        super(ItemWidget, self).resizeEvent(event)
        print("-----------------------")
        print(self.height())
        self.item.setSizeHint(QSize(self.minimumWidth(), 60))
        print("执行SIZESET")
'''