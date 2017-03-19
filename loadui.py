import sys,os

from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon,QPixmap


app = QApplication(sys.argv)
path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'good.ico')
app.setWindowIcon(QIcon(QPixmap(path)))

widget = loadUi('test.ui')
widget.show()
sys.exit(app.exec_())

