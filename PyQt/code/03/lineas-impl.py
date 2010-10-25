import sys
from PyQt4 import QtGui
from lineas import *

class myGUI(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_Lines()
		self.ui.setupUi(self)
		self.ui.button.clicked.connect(self.buttonChange)
	def buttonChange(self):
		text = self.ui.line.text()
		self.ui.label.setText(text)	
		self.ui.line.setText('')
if  __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   myapp = myGUI()
   myapp.show()
   sys.exit(app.exec_())
