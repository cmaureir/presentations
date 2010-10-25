import sys
from PyQt4.QtGui import QLabel,QApplication

app = QApplication(sys.argv)
label = QLabel("Hello World")
label.show()
sys.exit(app.exec_())
