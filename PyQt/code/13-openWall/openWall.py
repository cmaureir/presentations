#!/usr/bin/env python

import os,sys
from PyQt4 import QtCore, QtGui, Qt
from design import *

class firstGUI(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.openbox = False
		self.modes = ['','-a','-t','-c']
		self.mode = 0
		self.currentImage = None
		self.ui.imageLabel.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("default.png")))
		# Buttons
		QtCore.QObject.connect(self.ui.examineButton, QtCore.SIGNAL("clicked()"), self.examineButtonAction)
		QtCore.QObject.connect(self.ui.applyButton, QtCore.SIGNAL("clicked()"), self.applyButtonAction)
		# Checkbox
		QtCore.QObject.connect(self.ui.optionComboBox, QtCore.SIGNAL("activated(int)"), self.optionAction)
		# Menus
		# Menu File
		QtCore.QObject.connect(self.ui.menuExamine, QtCore.SIGNAL("triggered()"), self.examineButtonAction)
		QtCore.QObject.connect(self.ui.menuAdjust, QtCore.SIGNAL("triggered()"), self.adjustWallOption)
		QtCore.QObject.connect(self.ui.menuTiled, QtCore.SIGNAL("triggered()"), self.tiledWallOption)
		QtCore.QObject.connect(self.ui.menuCentered, QtCore.SIGNAL("triggered()"), self.centeredWallOption)
		QtCore.QObject.connect(self.ui.menuOpenBox, QtCore.SIGNAL("triggered()"), self.openBoxOption)
		QtCore.QObject.connect(self.ui.menuApply, QtCore.SIGNAL("triggered()"), self.applyButtonAction)
		QtCore.QObject.connect(self.ui.menuQuit, QtCore.SIGNAL("triggered()"), self.close)
		# Menu Help
		QtCore.QObject.connect(self.ui.menuHelp, QtCore.SIGNAL("triggered()"), self.menuHelpAction)
		QtCore.QObject.connect(self.ui.menuAbout, QtCore.SIGNAL("triggered()"), self.menuAboutAction)

	def adjustWallOption(self):
		self.mode = 1

	def tiledWallOption(self):
		self.mode = 2

	def centeredWallOption(self):
		self.mode = 3

	def openBoxOption(self):
		if self.openbox:
			self.ui.openBoxCheckBox.setCheckState(0)
			self.openbox = False
		else:
			self.ui.openBoxCheckBox.setCheckState(2)
			self.openbox = True


	def menuHelpAction(self):
		QtGui.QMessageBox.about(self,
					"openWall Help",
					"-Select an image\n\
					-Select a mode (centered is default)\n\
					-Select if you want add this\n\
					wallpaper in you autostart.sh file\n\
					-Apply" )

	def menuAboutAction(self):
		QtGui.QMessageBox.about(self, "About openWall","Develop by:\n\
					\tCristian Maureira\n\
					\t <saint@archlinux.cl>\n\
					\nPlease contact me for any bug\n\
					or a new feature." )

	def examineButtonAction(self):
		self.currentImage=QtGui.QFileDialog.getOpenFileName(self,\
														"Choose a file",\
														".",\
														"Images (*.png *.xpm *.jpg *.jpeg)")

		if not self.currentImage.isNull():
			self.currentImage = self.currentImage.replace(" ","\ ").replace("(","\(").replace(")","\)")
			self.ui.wallpaperPathLine.setText(self.currentImage)
			img = QtGui.QPixmap.fromImage(QtGui.QImage(self.currentImage))
			img = img.scaled(320,200)
			self.ui.imageLabel.setPixmap(img)
			#print "[ERROR] The path of the image have invalid charactered, cannot display"

	def applyButtonAction(self):
		if self.currentImage:
			os.system("fbsetbg "+\
					str(self.modes[self.mode])+" "+\
					str(self.currentImage))
		else:
			print "[ERROR] There is no image selected"
	
	def optionAction(self):
		value = str(self.ui.optionComboBox.currentText())
		if value == "Tiled":
			self.mode = 2
		elif value == "Adjust":
			self.mode = 1
		elif value == "Centered":
			self.mode = 3
		elif value == "none":
			self.mode = 0
		print value

		
if  __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   myapp = firstGUI()
   myapp.show()
   sys.exit(app.exec_())


