"""
vtoolmenu.py create object loop
"""
# for _i in range(len(self.btname)):
# top_obj = QListWidgetItem(self)
# self.btn = TopButton(top_obj, self.btname[_i],self.t_icon_fold,self.t_icon_unfold)
# self.btn.setObjectName("menu_0")
# # self.btn.setIcon(self.t_icon_fold)
# self.btn.setFixedHeight(self.__btheight)
# self.btn.setStyleSheet(self.__qss)
# self.setItemWidget(top_obj, self.btn)
# if self.itemlist[_i]:
#     sub_obj = QListWidgetItem(self)
#     self.btn.toggled.connect(sub_obj.setHidden)
#     self.itemc = ItemWidget(sub_obj, self.itemlist[_i],self.__qss,self.__itemper,self.__btheight)
#     self.setItemWidget(sub_obj, self.itemc)
#     sub_obj.setHidden(True)
# else:
#     pass


"""
event icon change
"""

# class button:
#     ...
# def event(self, event):
#     if event.type() == QEvent.MouseButtonPress:
#         if self.isChecked():
#             self.setIcon(self.icon_uf)
#         else:
#             self.setIcon(self.icon_f)
#     return super(TopButton, self).event(event)

"""
QTreewidget
"""

# def traverse(self):
#     """遍历"""
#     iterator = QTreeWidgetItemIterator(self)
#
#     while iterator.value():
#         item = iterator.value()
#         columnCount = item.columnCount()
#         for i in range(columnCount):
#             text = item.text(i)
#             if i == columnCount - 1:
#                 print(text)
#                 print(type(text))
#             else:
#                 print(text, end=' ')
#         iterator.__iadd__(1)