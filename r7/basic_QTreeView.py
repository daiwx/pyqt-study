#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 400, 350)
        self.setWindowTitle("QFileSystemModel")

        self.initUI()

    def initUI(self):
        self.model = QtGui.QFileSystemModel()
        homedir = QtCore.QDir.home().path()
        self.model.setRootPath(homedir)

        tv = QtGui.QTreeView(self)
        tv.setModel(self.model)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(tv)
        self.setLayout(layout)

app = QtGui.QApplication([])
ex = Example()
ex.show()
app.exec_()
