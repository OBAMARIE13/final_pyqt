import sys
import os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.uic import loadUiType



FORM_CLASS,_ = loadUiType(os.path.join(os.path.dirname("__file__"), "ui/carte_d_identite.ui"))

class Listes(QtWidgets.QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def getDatas(self):
        db = sqlite3.connect(os.path.join(os.path.dirname("__file__"),"database.db"))
        c = db.cursor()
        command = """ SELECT * FROM regist  """
        resultat = c.execute(command)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(resultat):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
