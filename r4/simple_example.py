#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui


class Example(QtGui.QGraphicsView):
    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Simple")

        self.init()

    def init(self):
        self.scene = QtGui.QGraphicsScene()
        self.scene.addText("ZetCode")

        self.setScene(self.scene)

app = QtGui.QApplication([])
ex = Example()
ex.show()
app.exec_()
