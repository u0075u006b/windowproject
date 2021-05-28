import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class FontDialogdemo(QWidget):
    def __init__(self,parent=None):
        super(FontDialogdemo, self).__init__(parent)

        #垂直布局
        layout=QVBoxLayout()

        #创建按钮，绑定自定义槽函数，添加到布局中
        self.fonButton=QPushButton('Choose Font')
        self.fonButton.clicked.connect(self.getFont)
        layout.addWidget(self.fonButton)

        #创建标签，添加dao到布局中
        self.FontLineEdit=QLabel('Hello 测试字体的例子')
        layout.addWidget(self.FontLineEdit)

        #设置主窗口布局及标题
        self.setLayout(layout)
        self.setWindowTitle("Font Dialog例子")

    def getFont(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.FontLineEdit.setFont(font)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=FontDialogdemo()
    demo.show()
    sys.exit(app.exec_())