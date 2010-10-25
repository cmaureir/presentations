# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '08-tabs.ui'
#
# Created: Wed Oct 20 23:10:51 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_tabs(object):
    def setupUi(self, tabs):
        tabs.setObjectName(_fromUtf8("tabs"))
        tabs.resize(314, 234)
        self.tabWidget = QtGui.QTabWidget(tabs)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 291, 191))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.label1 = QtGui.QLabel(self.tab1)
        self.label1.setGeometry(QtCore.QRect(60, 40, 161, 71))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.label2 = QtGui.QLabel(self.tab2)
        self.label2.setGeometry(QtCore.QRect(70, 50, 161, 71))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.tabWidget.addTab(self.tab2, _fromUtf8(""))
        self.tab3 = QtGui.QWidget()
        self.tab3.setObjectName(_fromUtf8("tab3"))
        self.label3 = QtGui.QLabel(self.tab3)
        self.label3.setGeometry(QtCore.QRect(60, 40, 161, 71))
        self.label3.setObjectName(_fromUtf8("label3"))
        self.tabWidget.addTab(self.tab3, _fromUtf8(""))
        self.tab4 = QtGui.QWidget()
        self.tab4.setObjectName(_fromUtf8("tab4"))
        self.label4 = QtGui.QLabel(self.tab4)
        self.label4.setGeometry(QtCore.QRect(70, 40, 161, 71))
        self.label4.setObjectName(_fromUtf8("label4"))
        self.tabWidget.addTab(self.tab4, _fromUtf8(""))

        self.retranslateUi(tabs)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(tabs)

    def retranslateUi(self, tabs):
        tabs.setWindowTitle(QtGui.QApplication.translate("tabs", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("tabs", "Estamos en el Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QtGui.QApplication.translate("tabs", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("tabs", "Estamos en el Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QtGui.QApplication.translate("tabs", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setText(QtGui.QApplication.translate("tabs", "Estamos en el Tab 3", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QtGui.QApplication.translate("tabs", "Tab 3", None, QtGui.QApplication.UnicodeUTF8))
        self.label4.setText(QtGui.QApplication.translate("tabs", "Estamos en el Tab 4", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), QtGui.QApplication.translate("tabs", "Tab 4", None, QtGui.QApplication.UnicodeUTF8))

