import os,sys
from PyQt4 import QtCore, QtGui, Qt
from formulario import *


class myGUI(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_form()
		self.ui.setupUi(self)

		self.sex , self.name = None, None
		self.day, self.month, self.year = None, None, None
		self.ui.male.clicked.connect(self.changeRadioMale)
		self.ui.female.clicked.connect(self.changeRadioFemale)
		self.ui.name.textChanged.connect(self.changeName)
		self.ui.day.valueChanged.connect(self.changeDay)
		self.ui.month.valueChanged.connect(self.changeMonth)
		self.ui.year.valueChanged.connect(self.changeYear)
		self.ui.buttonBox.accepted.connect(self.answer)
		self.ui.buttonBox.rejected.connect(self.close)
		self.ui.year.setMaximum(2010)

	def changeRadioMale(self):
		self.sex = "Hombre"

	def changeRadioFemale(self):
		self.sex = "Mujer"

	def changeName(self):
		#print "name change to : "+ self.ui.name.text()
		self.name = self.ui.name.text()

	def changeDay(self):
		self.day = self.ui.day.value()

	def changeMonth(self):
		self.month = self.ui.month.value()

	def changeYear(self):
		self.year = self.ui.year.value()

	def answer(self):
		info = "Name: "+self.name+\
			   "\nSexo: "+self.sex+\
			   "\nF. nac: "+str(self.day)+"/"+\
				str(self.month)+"/"+str(self.year)
		w = QtGui.QMessageBox.question(self,\
									'Informacion',\
									info,QtGui.QMessageBox.Yes,\
									QtGui.QMessageBox.No)
		if w == QtGui.QMessageBox.Yes:
			self.close

if  __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   myapp = myGUI()
   myapp.show()
   sys.exit(app.exec_())
