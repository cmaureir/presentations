import sys
from PyQt4 import QtGui
from PyQt4.phonon import Phonon

app = QtGui.QApplication(sys.argv)
url="qt.flv"
w = QtGui.QWidget()
player = Phonon.VideoPlayer(Phonon.VideoCategory,w)
player.load(Phonon.MediaSource(url))
w.setMinimumSize(400,400)
topLayout = QtGui.QVBoxLayout(w)
topLayout.addWidget(player)
w.setLayout(topLayout)
w.show()
player.play()
sys.exit(app.exec_())
