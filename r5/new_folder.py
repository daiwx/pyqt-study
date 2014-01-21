#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("New folder")

        self.initUI()

    def initUI(self):
        grid = QtGui.QGridLayout()

        grid.addWidget(QtGui.QLabel("Name: "), 0, 0)

        line = QtGui.QLineEdit()
        grid.addWidget(line, 0, 1, 1, 3)
        grid.setColumnStretch(1, 1)

        grid.addWidget(QtGui.QListView(), 1, 0, 2, 4)

        ok = QtGui.QPushButton("OK")
        cancel = QtGui.QPushButton("Cancel")

        grid.addWidget(ok, 3, 2)
        grid.addWidget(cancel, 3, 3)

        self.setLayout(grid)

app = QtGui.QApplication([])
ex = Example()
ex.show()
app.exec_()
