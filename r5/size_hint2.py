#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.move(300, 300)
        self.setWindowTitle("MinMax")

        self.initUI()

    def initUI(self):
        te = QtGui.QTextEdit()
        te.setMinimumSize(15, 15)
        te.setMaximumSize(350, 350)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(te)
        self.setLayout(layout)

app = QtGui.QApplication([])
ex = Example()
ex.show()
app.exec_()
