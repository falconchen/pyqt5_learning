import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication,QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(550, 350)
        self.center()
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry() #我们获得主窗口的一个矩形特定几何图形。这包含了窗口的框架。

        cp = QDesktopWidget().availableGeometry().center()#我们算出相对于显示器的绝对值。并且从这个绝对值中，我们获得了屏幕中心点。

        #qpoint设置xy 轴：https://doc.qt.io/qt-5/qpoint.html
        #print(cp.y())
        #cp.setY(0)
        qr.moveCenter(cp) ##我们的矩形已经设置好了它的宽和高。现在我们把矩形的中心设置到屏幕的中间去。矩形的大小并不会改变。
        self.move(qr.topLeft()) #我们移动了应用窗口的左上方的点到qr矩形的左上方的点，因此居中显示在我们的屏幕上。





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())