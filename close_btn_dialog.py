#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMessageBox
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 按钮是一个QPushButton类的实例。构造方法的第一个参数是显示在button上的标签文本。第二个参数是父组件。父组件是Example组件，它继承了QWiget类。
        qbtn = QPushButton('Quit', self)
        # QCoreApplication类包含了主事件循环；它处理和转发所有事件。instance()方法给我们返回一个实例化对象。事件通信在两个对象之间进行：发送者和接受者。发送者是按钮，接受者是应用对象。
        #qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.clicked.connect(self.close) # 将接收者变成当前实例的
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)


        self.setGeometry(600, 500, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())