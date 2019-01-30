# -*- coding: utf-8 -*-import terms
import json
from terms import createAttributeTerm
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

app = QtWidgets.QApplication([])
dlg = uic.loadUi("test.ui")



def main():
    with open('data.json', 'r') as file:
        dlg.textEdit.setText(file.read())

if __name__ == "__main__":
    main()

def show_message(title, message):
    QMessageBox.information(None, title, message)

def GetParse():
    value_ids1 = []
    value_ids1 = dlg.lineEdit_3.text()
    result = [x.strip() for x in value_ids1.split(',')]
    return result

def Convert():
    dlg.lineEdit_2.setText(terms.createAttributeTerm(dlg.lineEdit.text(), GetParse()))

def CheckManuf():
    manuf = dlg.lineEdit_4.text()
    try:
        result = int(manuf)
    except ValueError:
        result = manuf
    return result

def CreateManuf():
    dlg.lineEdit_5.setText(terms.createManufacturerTerm(CheckManuf()))

def Compose():
    if not dlg.lineEdit_7.text() == "":
        dlg.textEdit.setText(terms.composeTerms(dlg.lineEdit_7.text(), str(dlg.lineEdit_5.text()), str(dlg.lineEdit_2.text())))
    else:
        show_message("Warning", "You have to define logic!")
    SaveToJSON()

def SaveToJSON():
    data = dlg.textEdit.toPlainText()
    with open('data.json','w') as file:
        file.write(data)




dlg.lineEdit_4.setFocus()

dlg.lineEdit.setPlaceholderText("Attribute ID")
dlg.lineEdit_3.setPlaceholderText("Attribute Value")
dlg.pushButton.clicked.connect(Convert)
dlg.lineEdit.returnPressed.connect(Convert)
dlg.lineEdit_3.returnPressed.connect(Convert)

dlg.lineEdit_4.setPlaceholderText("ID or name")
dlg.pushButton_2.clicked.connect(CreateManuf)
dlg.lineEdit_4.returnPressed.connect(CreateManuf)

dlg.lineEdit_7.setPlaceholderText("Must")
dlg.pushButton_3.clicked.connect(Compose)

dlg.lineEdit_2.setReadOnly(True)
dlg.lineEdit_5.setReadOnly(True)

dlg.show()
app.exec()
 

