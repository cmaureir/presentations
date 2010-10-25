#!/usr/bin/env python

import os,sys
from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 321)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.applyButton = QtGui.QPushButton(self.centralwidget)
        self.applyButton.setGeometry(QtCore.QRect(360, 180, 121, 71))
        self.applyButton.setObjectName("applyButton")
        self.examineButton = QtGui.QPushButton(self.centralwidget)
        self.examineButton.setGeometry(QtCore.QRect(370, 30, 71, 24))
        self.examineButton.setObjectName("examineButton")
        self.wallpaperPathLine = QtGui.QLineEdit(self.centralwidget)
        self.wallpaperPathLine.setGeometry(QtCore.QRect(10, 30, 361, 25))
        self.wallpaperPathLine.setObjectName("wallpaperPathLine")
        self.imageLabel = QtGui.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(20, 70, 320, 200))
        self.imageLabel.setObjectName("imageLabel")
        self.openBoxCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.openBoxCheckBox.setGeometry(QtCore.QRect(370, 150, 82, 23))
        self.openBoxCheckBox.setObjectName("openBoxCheckBox")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(360, 120, 121, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.optionComboBox = QtGui.QComboBox(self.centralwidget)
        self.optionComboBox.setGeometry(QtCore.QRect(360, 80, 121, 24))
        self.optionComboBox.setObjectName("optionComboBox")
        self.optionComboBox.addItem(QtCore.QString())
        self.optionComboBox.addItem(QtCore.QString())
        self.optionComboBox.addItem(QtCore.QString())
        self.optionComboBox.addItem(QtCore.QString())
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 23))
        self.menubar.setObjectName("menubar")
        self.menuBarHelp = QtGui.QMenu(self.menubar)
        self.menuBarHelp.setObjectName("menuBarHelp")
        self.menuBarFile = QtGui.QMenu(self.menubar)
        self.menuBarFile.setObjectName("menuBarFile")
        self.menuMode = QtGui.QMenu(self.menuBarFile)
        self.menuMode.setObjectName("menuMode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuHelp = QtGui.QAction(MainWindow)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtGui.QAction(MainWindow)
        self.menuAbout.setObjectName("menuAbout")
        self.menuQuit = QtGui.QAction(MainWindow)
        self.menuQuit.setObjectName("menuQuit")
        self.menuExamine = QtGui.QAction(MainWindow)
        self.menuExamine.setObjectName("menuExamine")
        self.menuOpenBox = QtGui.QAction(MainWindow)
        self.menuOpenBox.setObjectName("menuOpenBox")
        self.menuAdjust = QtGui.QAction(MainWindow)
        self.menuAdjust.setObjectName("menuAdjust")
        self.menuTiled = QtGui.QAction(MainWindow)
        self.menuTiled.setObjectName("menuTiled")
        self.menuCentered = QtGui.QAction(MainWindow)
        self.menuCentered.setObjectName("menuCentered")
        self.menuApply = QtGui.QAction(MainWindow)
        self.menuApply.setObjectName("menuApply")
        self.menuBarHelp.addAction(self.menuHelp)
        self.menuBarHelp.addAction(self.menuAbout)
        self.menuMode.addAction(self.menuAdjust)
        self.menuMode.addAction(self.menuTiled)
        self.menuMode.addAction(self.menuCentered)
        self.menuBarFile.addAction(self.menuExamine)
        self.menuBarFile.addAction(self.menuMode.menuAction())
        self.menuBarFile.addAction(self.menuOpenBox)
        self.menuBarFile.addAction(self.menuApply)
        self.menuBarFile.addSeparator()
        self.menuBarFile.addAction(self.menuQuit)
        self.menubar.addAction(self.menuBarFile.menuAction())
        self.menubar.addAction(self.menuBarHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "openWall", None, QtGui.QApplication.UnicodeUTF8))
        self.applyButton.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.examineButton.setText(QtGui.QApplication.translate("MainWindow", "Examine", None, QtGui.QApplication.UnicodeUTF8))
        self.openBoxCheckBox.setText(QtGui.QApplication.translate("MainWindow", "autostart", None, QtGui.QApplication.UnicodeUTF8))
        self.optionComboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "none", None, QtGui.QApplication.UnicodeUTF8))
        self.optionComboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Adjust", None, QtGui.QApplication.UnicodeUTF8))
        self.optionComboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Tiled", None, QtGui.QApplication.UnicodeUTF8))
        self.optionComboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "Centered", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBarHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBarFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMode.setTitle(QtGui.QApplication.translate("MainWindow", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.menuQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExamine.setText(QtGui.QApplication.translate("MainWindow", "Examine", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOpenBox.setText(QtGui.QApplication.translate("MainWindow", "OpenBox", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdjust.setText(QtGui.QApplication.translate("MainWindow", "Adjust", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTiled.setText(QtGui.QApplication.translate("MainWindow", "Tiled", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCentered.setText(QtGui.QApplication.translate("MainWindow", "Centered", None, QtGui.QApplication.UnicodeUTF8))
        self.menuApply.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))

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
					"-Select an image\n-Select a mode (centered is default)\n-Select if you want add this\n  wallpaper in you autostart.sh file\n-Apply" )

	def menuAboutAction(self):
		QtGui.QMessageBox.about(self, "About openWall","Develop by:\n\tCristian Maureira\n\t <saint@archlinux.cl>\n\nPlease contact me for any bug\nor a new feature." )


	def examineButtonAction(self):
		self.currentImage=QtGui.QFileDialog.getOpenFileName(self,"Choose a file",".","Images (*.png *.xpm *.jpg *.jpeg)")
		if not self.currentImage.isNull():
			self.currentImage = self.currentImage.replace(" ","\ ").replace("(","\(").replace(")","\)")
			self.ui.wallpaperPathLine.setText(self.currentImage)
			print self.currentImage
			img = QtGui.QPixmap.fromImage(QtGui.QImage(self.currentImage))
			img = img.scaled(320,200)
			self.ui.imageLabel.setPixmap(img)
			#print "[ERROR] The path of the image have invalid charactered, cannot display"

	def applyButtonAction(self):
		if self.currentImage:
			os.system("fbsetbg "+str(self.modes[self.mode])+" "+str(self.currentImage))
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


