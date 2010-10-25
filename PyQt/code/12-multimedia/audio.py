import sys
from PyQt4 import QtGui
from PyQt4.phonon import Phonon

app = QtGui.QApplication(sys.argv)
url="AirbeatProject-AirbeatOne.mp3"
w = QtGui.QWidget()
audio = Phonon.createPlayer(Phonon.MusicCategory,
							Phonon.MediaSource(url))
w.setMinimumSize(100,100)
w.show()
audio.play()
sys.exit(app.exec_())
