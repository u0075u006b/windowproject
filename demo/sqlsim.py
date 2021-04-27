

"""
Sql simulation mod
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DIC:
    status = {
        "connect":True,
        "disconnected":False

    }
    name = {
        1:"RDS",
        2:"LOC"
    }
    ip = {
        "RDS":["192.168.0.1","10.17.12.1"],
        "LOC":["local_A","local_B"]
    }
    datahas = {
        "array":[100,200,300,400,500,600,700,800,900,1000]
    }

class SqlSon(QThread):

