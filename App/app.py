import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from App.ui.main import MainWindow
import logging
logging.basicConfig(level=logging.WARNING)


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)



def main():
    """
    To Hide mouse cursor
    fb.setCursor(Qt.BlankCursor)

    and To Show mouse cursor (parent's
    cursor is used) fb.unsetCursor()
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    fb = App()
    fb.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
    fb.setCursor(Qt.BlankCursor)
    fb.show()
    app.exec_()




if __name__ == '__main__':
    main()
