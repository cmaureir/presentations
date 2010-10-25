# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '07-calendar.ui'
#
# Created: Wed Oct 20 23:10:49 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Calendar(object):
    def setupUi(self, Calendar):
        Calendar.setObjectName(_fromUtf8("Calendar"))
        Calendar.resize(375, 243)
        self.calendarWidget = QtGui.QCalendarWidget(Calendar)
        self.calendarWidget.setGeometry(QtCore.QRect(50, 20, 272, 150))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.lineEdit = QtGui.QLineEdit(Calendar)
        self.lineEdit.setGeometry(QtCore.QRect(50, 190, 271, 23))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Calendar)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        Calendar.setWindowTitle(QtGui.QApplication.translate("Calendar", "Form", None, QtGui.QApplication.UnicodeUTF8))

