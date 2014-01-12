#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()

        self.move(300, 300)
        self.setWindowTitle("Stretch factor")

        self.initUI()

    def initUI(self):
        b1 = QtGui.QPushButton("Button")
        b2 = QtGui.QPushButton("Button")
        b3 = QtGui.QPushButton("Button")

        hbox = QtGui.QHBoxLayout()

        hbox.addWidget(b1)
        hbox.addWidget(b2)
        hbox.addWidget(b3)

        hbox.setStretchFactor(b1, 1)
        hbox.setStretchFactor(b2, 5)
        hbox.setStretchFactor(b3, 8)

        self.setLayout(hbox)

app = QtGui.QApplication([])
ex = Example()
ex.show()
app.exec_()
