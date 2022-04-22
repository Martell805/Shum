import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from QT.MW import Ui_Starter
from old_mains.DynamicMain import dynamic_main


# Это программа для удобного запуска


class Starter(Ui_Starter, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.create_btn.clicked.connect(self.create)

    def create(self):
        w.hide()
        dynamic_main(self.n.value(), self.m.value(), 1.3, 1/15, self.wl.value(), self.ts.value(), '', False, False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Starter()
    w.show()
    sys.exit(app.exec_())
