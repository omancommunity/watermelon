import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from App.ui.main import MainWindow
import logging

logging.basicConfig(level=logging.INFO)


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)


def main():
    """
    # To Hide mouse cursor
    window.setCursor(Qt.BlankCursor)
    # To Show mouse cursor (parent's cursor is used)
    window.unsetCursor()
    """
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
    window.setCursor(Qt.BlankCursor)
    window.show()
    app.exec_()
    logging.info("Application start .... ")


if __name__ == '__main__':
    main()
