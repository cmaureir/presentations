import sys
from PyQt4 import QtGui
from tabs import *


class myGUI(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_tabs()
		self.ui.setupUi(self)
		
if  __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   myapp = myGUI()
   myapp.show()
   sys.exit(app.exec_())
