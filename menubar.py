import sys,os
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication,QToolBar,QMenu
from PyQt5.QtGui import QIcon,QPixmap


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):



        exitAction = QAction(QIcon('mac/filenew.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip(r'退出应用')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False) #(Mac OS菜单栏不同，为获得类似效果我们可以在代码中添加下面一行：menubar.setNativeMenuBar(False)), 在mac 当设置为True时子菜单不可设置设置图标
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        
        testMenu = menubar.addMenu('&Open')
        testMenu.addAction("&Open1...")
        testMenu.addSeparator()
        testMenu.addAction("&Open2...")
        testMenu.addAction(exitAction)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())