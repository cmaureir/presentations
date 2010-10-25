import os,sys
from PyQt4 import QtCore, QtGui, Qt
from menu import *

class myGUI(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.actionTest.triggered.connect(self.testAction)
		self.ui.actionExit.triggered.connect(self.close)
		self.ui.actionAbout.triggered.connect(self.aboutAction)
	def testAction(self):
		print "test"
	def aboutAction(self):
		print "about"
if  __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = myGUI()
	myapp.show()
	sys.exit(app.exec_())
