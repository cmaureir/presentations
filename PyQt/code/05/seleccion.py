# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '05-seleccion.ui'
#
# Created: Wed Oct 20 23:10:47 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_seleccion(object):
    def setupUi(self, seleccion):
        seleccion.setObjectName(_fromUtf8("seleccion"))
        seleccion.resize(306, 266)
        self.comboBox = QtGui.QComboBox(seleccion)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 181, 24))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.addButton = QtGui.QPushButton(seleccion)
        self.addButton.setGeometry(QtCore.QRect(210, 20, 71, 24))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.list = QtGui.QListWidget(seleccion)
        self.list.setGeometry(QtCore.QRect(20, 50, 261, 192))
        self.list.setObjectName(_fromUtf8("list"))

        self.retranslateUi(seleccion)
        QtCore.QMetaObject.connectSlotsByName(seleccion)

    def retranslateUi(self, seleccion):
        seleccion.setWindowTitle(QtGui.QApplication.translate("seleccion", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("seleccion", "Go", None, QtGui.QApplication.UnicodeUTF8))

