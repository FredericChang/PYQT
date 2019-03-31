# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog
#from layout_demo_LayoutManageaa import Ui_LayoutDemo
from MainForm2 import Ui_MainWindow
from ChildrenForm2 import Ui_ChildrenForm

#class LayoutDemo(QMainWindow, Ui_LayoutDemo):
class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        #super(LayoutDemo, self).__init__(parent)
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.child = ChildrenForm()
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)
        self.addWinAction.triggered.connect(self.childShow)

    def childShow(self):
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def openMsg(self):
        file,ok = QFileDialog.getOpenFileName(self,"Open","C:/","AllFiles (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)
    @pyqtSlot()
    def on_pushButton_clicked(self):
         print('Return_max:', self.doubleSpinBox_returns_max.text())
class ChildrenForm(QWidget, Ui_ChildrenForm):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainForm()
    #ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec_())

