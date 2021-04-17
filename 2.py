import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.resize(400,400)
        pixmap = QPixmap("lion.jpg")
        self.lbl.setPixmap(QPixmap(pixmap))

        self.resize(400, 400)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = test()
    sys.exit(app.exec_())