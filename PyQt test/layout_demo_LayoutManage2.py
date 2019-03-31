# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from layout_demo_LayoutManageaa import Ui_LayoutDemo

class LayoutDemo(QMainWindow, Ui_LayoutDemo):
    def __init__(self, parent=None):
        super(LayoutDemo, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
         print('Return_max:', self.doubleSpinBox_returns_max.text())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec_())

