import sys
import fengexian
from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QMainWindow()
    ui = fengexian.Ui_MainWindow()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())
