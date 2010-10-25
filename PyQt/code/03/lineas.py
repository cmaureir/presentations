# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '03-lineas.ui'
#
# Created: Wed Oct 20 23:10:44 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Lines(object):
    def setupUi(self, Lines):
        Lines.setObjectName(_fromUtf8("Lines"))
        Lines.resize(264, 140)
        self.line = QtGui.QLineEdit(Lines)
        self.line.setGeometry(QtCore.QRect(20, 40, 151, 23))
        self.line.setObjectName(_fromUtf8("line"))
        self.button = QtGui.QPushButton(Lines)
        self.button.setGeometry(QtCore.QRect(180, 40, 71, 24))
        self.button.setObjectName(_fromUtf8("button"))
        self.label = QtGui.QLabel(Lines)
        self.label.setGeometry(QtCore.QRect(28, 80, 221, 31))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Lines)
        QtCore.QMetaObject.connectSlotsByName(Lines)

    def retranslateUi(self, Lines):
        Lines.setWindowTitle(QtGui.QApplication.translate("Lines", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.button.setText(QtGui.QApplication.translate("Lines", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Lines", "hola", None, QtGui.QApplication.UnicodeUTF8))

