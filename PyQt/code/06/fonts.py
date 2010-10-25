# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fonts.ui'
#
# Created: Thu Oct 21 23:20:26 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_fonts(object):
    def setupUi(self, fonts):
        fonts.setObjectName(_fromUtf8("fonts"))
        fonts.resize(314, 207)
        self.fontComboBox = QtGui.QFontComboBox(fonts)
        self.fontComboBox.setGeometry(QtCore.QRect(80, 50, 201, 23))
        self.fontComboBox.setObjectName(_fromUtf8("fontComboBox"))
        self.label = QtGui.QLabel(fonts)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.font = QtGui.QLabel(fonts)
        self.font.setGeometry(QtCore.QRect(50, 130, 211, 41))
        self.font.setObjectName(_fromUtf8("font"))

        self.retranslateUi(fonts)
        QtCore.QMetaObject.connectSlotsByName(fonts)

    def retranslateUi(self, fonts):
        fonts.setWindowTitle(QtGui.QApplication.translate("fonts", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("fonts", "Selección de fuentes", None, QtGui.QApplication.UnicodeUTF8))
        self.font.setText(QtGui.QApplication.translate("fonts", "Este es un texto de prueba", None, QtGui.QApplication.UnicodeUTF8))

