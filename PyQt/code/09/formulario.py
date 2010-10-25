# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '09-formulario.ui'
#
# Created: Wed Oct 20 23:10:52 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName(_fromUtf8("form"))
        form.resize(403, 188)
        self.title = QtGui.QLabel(form)
        self.title.setGeometry(QtCore.QRect(20, 20, 221, 16))
        self.title.setObjectName(_fromUtf8("title"))
        self.male = QtGui.QRadioButton(form)
        self.male.setGeometry(QtCore.QRect(20, 60, 103, 21))
        self.male.setObjectName(_fromUtf8("male"))
        self.female = QtGui.QRadioButton(form)
        self.female.setGeometry(QtCore.QRect(20, 90, 103, 21))
        self.female.setObjectName(_fromUtf8("female"))
        self.name = QtGui.QLineEdit(form)
        self.name.setGeometry(QtCore.QRect(220, 60, 171, 23))
        self.name.setObjectName(_fromUtf8("name"))
        self.nameLabel = QtGui.QLabel(form)
        self.nameLabel.setGeometry(QtCore.QRect(160, 60, 59, 21))
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.day = QtGui.QSpinBox(form)
        self.day.setGeometry(QtCore.QRect(220, 90, 51, 23))
        self.day.setObjectName(_fromUtf8("day"))
        self.fnacLabel = QtGui.QLabel(form)
        self.fnacLabel.setGeometry(QtCore.QRect(170, 90, 41, 21))
        self.fnacLabel.setObjectName(_fromUtf8("fnacLabel"))
        self.month = QtGui.QSpinBox(form)
        self.month.setGeometry(QtCore.QRect(270, 90, 51, 23))
        self.month.setObjectName(_fromUtf8("month"))
        self.year = QtGui.QSpinBox(form)
        self.year.setGeometry(QtCore.QRect(320, 90, 71, 23))
        self.year.setObjectName(_fromUtf8("year"))
        self.buttonBox = QtGui.QDialogButtonBox(form)
        self.buttonBox.setGeometry(QtCore.QRect(220, 140, 162, 25))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        form.setWindowTitle(QtGui.QApplication.translate("form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("form", "Formulario", None, QtGui.QApplication.UnicodeUTF8))
        self.male.setText(QtGui.QApplication.translate("form", "Hombre", None, QtGui.QApplication.UnicodeUTF8))
        self.female.setText(QtGui.QApplication.translate("form", "Mujer", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("form", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.fnacLabel.setText(QtGui.QApplication.translate("form", "F. nac", None, QtGui.QApplication.UnicodeUTF8))

