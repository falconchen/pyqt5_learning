#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	w.resize(250,350)
	w.move(300,300)
	w.setWindowTitle("Hello PyQt")
	w.show()
	sys.exit(app.exec_())
