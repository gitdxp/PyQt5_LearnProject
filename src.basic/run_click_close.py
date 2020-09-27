import sys
import click_close
from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QMainWindow()
    ui = click_close.Ui_MainWindow()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())
