import sys
from PyQt4 import QtGui
from calendar import *


class myGUI(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_Calendar()
		self.ui.setupUi(self)
		self.ui.calendarWidget.clicked.connect(self.changeDate)		
	
	def changeDate(self):
		self.ui.lineEdit.setText(self.ui.calendarWidget.selectedDate().toString())

if  __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   myapp = myGUI()
   myapp.show()
   sys.exit(app.exec_())
