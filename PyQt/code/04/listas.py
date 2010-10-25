# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '04-listas.ui'
#
# Created: Wed Oct 20 23:10:45 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Listas(object):
    def setupUi(self, Listas):
        Listas.setObjectName(_fromUtf8("Listas"))
        Listas.resize(301, 300)
        self.list = QtGui.QListWidget(Listas)
        self.list.setGeometry(QtCore.QRect(20, 60, 256, 192))
        self.list.setObjectName(_fromUtf8("list"))
        self.line = QtGui.QLineEdit(Listas)
        self.line.setGeometry(QtCore.QRect(20, 20, 171, 23))
        self.line.setObjectName(_fromUtf8("line"))
        self.addButton = QtGui.QPushButton(Listas)
        self.addButton.setGeometry(QtCore.QRect(200, 20, 71, 24))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.delButton = QtGui.QPushButton(Listas)
        self.delButton.setGeometry(QtCore.QRect(20, 260, 100, 24))
        self.delButton.setObjectName(_fromUtf8("delButton"))
        self.closeButton = QtGui.QPushButton(Listas)
        self.closeButton.setGeometry(QtCore.QRect(199, 260, 71, 24))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))

        self.retranslateUi(Listas)
        QtCore.QMetaObject.connectSlotsByName(Listas)

    def retranslateUi(self, Listas):
        Listas.setWindowTitle(QtGui.QApplication.translate("Listas", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("Listas", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.delButton.setText(QtGui.QApplication.translate("Listas", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Listas", "Close", None, QtGui.QApplication.UnicodeUTF8))

