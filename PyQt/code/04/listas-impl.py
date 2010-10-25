import sys
from PyQt4 import QtGui
from listas import *


class myGUI(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_Listas()
		self.ui.setupUi(self)
		self.lineas = []
		self.ui.addButton.clicked.connect(self.addButtonPressed)
		self.ui.delButton.clicked.connect(self.delButtonPressed)
		self.ui.closeButton.clicked.connect(self.close)

	def addButtonPressed(self):
		text = self.ui.line.text()
		self.lineas.append(text)
		self.ui.list.addItem(text)
		self.ui.line.setText('')	
	def delButtonPressed(self):
		item = self.ui.list.currentItem()
		text = item.text()
		j=0
		for i in self.lineas:
			if i == text:
				del self.lineas[j]
			j = j + 1
		self.ui.list.clear()
		for i in self.lineas:
			self.ui.list.addItem(i)

if  __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   myapp = myGUI()
   myapp.show()
   sys.exit(app.exec_())
