#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui


class Example(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.move(300, 300)
        self.setWindowTitle("Spanning")

        self.initUI()

    def initUI(self):
        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLineEdit(), 0, 0)
        grid.addWidget(QtGui.QLineEdit(), 0, 1)
        grid.addWidget(QtGui.QLineEdit(), 0, 2)
        grid.addWidget(QtGui.QLineEdit(), 0, 3)

        grid.addWidget(QtGui.QLineEdit(), 1, 0, 1, 2)
        grid.addWidget(QtGui.QLineEdit(), 2, 0, 1, 3)
        grid.addWidget(QtGui.QLineEdit(), 3, 0, 1, 4)

        self.setLayout(grid)

app = QtGui.QApplication([])
ex = Example()
ex.show()
app.exec_()
