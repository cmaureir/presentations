import sys
from PyQt4 import QtGui

class DragDrop(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.resize(180, 60)
        edit = QtGui.QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(20, 20)
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
if  __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	icon = DragDrop()
	icon.show()
	sys.exit(app.exec_())
