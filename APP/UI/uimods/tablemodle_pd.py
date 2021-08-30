from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from PyQt5.QtWidgets import QApplication, QTableView, QWidget, QVBoxLayout
import pandas as pd


class pandasModel(QAbstractTableModel):
    er_data = pd.DataFrame({' ': ['null']})

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        if isinstance(data,pd.DataFrame):
            self._data = data
        else:
            self._data = pandasModel.er_data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.TextAlignmentRole:
                return Qt.AlignCenter
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self._data.columns[col])
        return None


class TbView(QTableView):
    def __init__(self,model):
        super(TbView, self).__init__()
        self.setModel(model)
        self.setAlternatingRowColors(True)
        self.verticalHeader().hide()

        # self.setStyleSheet("QHeaderView::section {color: black;font:bold 10pt;background-color:rgb(250,250,250);}")

class WIN(QWidget):
    def __init__(self,model,size):
        super(WIN, self).__init__()
        self.resize(size[0],size[])
        self.lay = QVBoxLayout()
        self.tv = TbView(model)
        self.tv.resize(self.height(),self.width())
        self.lay.addWidget(self.tv)
        self.setLayout(self.lay)



def createtable(data,size):
    model = pandasModel(data)

