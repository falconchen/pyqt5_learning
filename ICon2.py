#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys,os

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon,QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Hello Icon')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'good.ico')
    app.setWindowIcon(QIcon(QPixmap(path)))
    ex = Example()
    sys.exit(app.exec_())