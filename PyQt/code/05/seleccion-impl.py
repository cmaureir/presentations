import sys
from PyQt4 import QtCore, QtGui
from seleccion import *


class myGUI(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_seleccion()
		self.ui.setupUi(self)
		self.ui.addButton.clicked.connect(self.applyFilter)		
		self.fill()

	def fill(self):
		self.nombres = ['Cristian',\
						'Ignacio',\
						'Gabriel',\
						'Christopher',\
						'Arnaldo',\
						'Jaime',\
						'Sergio',\
						'Yonathan']
		for i in self.nombres:
			self.ui.comboBox.addItem(i)
		self.personas = ['Yonathan Dossow',\
						 'Jaime Peldoza',\
						 'Jaime Oyarzun',\
						 'Arnaldo Garat',\
						 'Sergio Morales',\
						 'Gabriel Zamora',\
						 'Sergio Freire',\
						 'Gabriel Morales',\
						 'Cristian Morales',\
						 'Gabriel Perez',\
						 'Christopher Fernandez',\
						 'Ignacio Fernandes',\
						 'Jaime Oyarzun',\
						 'Christopher Oyarzun',\
						 'Ignacio Villacura']
		for i in self.personas:
			self.ui.list.addItem(i)

	def applyFilter(self):
		text = self.ui.comboBox.currentText()
		text = QtCore.QString(text)
		tmpList = []
		for i in self.personas:
			if text in QtCore.QString(i):
				tmpList.append(i)
		self.ui.list.clear()
		for i in tmpList:
			self.ui.list.addItem(i)

if  __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   myapp = myGUI()
   myapp.show()
   sys.exit(app.exec_())
