import sys
from PyQt4 import QtGui
from fonts import *

class myGUI(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_fonts()
		self.ui.setupUi(self)
		self.ui.fontComboBox.currentFontChanged.connect(self.changeFont)
		
	def changeFont(self):
		self.ui.font.setFont(self.ui.fontComboBox.currentFont())

if  __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   myapp = myGUI()
   myapp.show()
   sys.exit(app.exec_())
