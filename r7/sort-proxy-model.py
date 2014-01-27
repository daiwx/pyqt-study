#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

FIRST_COLUMN = 0


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle("Sorting")
        self.initData()
        self.initUI()

    def initData(self):
        names = []
        names.append("Jack")
        names.append("Tom")
        names.append("Lucy")
        names.append("Bill")
        names.append("Jane")

        self.model = QtGui.QStringListModel(names)
        self.filterModel = QtGui.QSortFilterProxyModel(self)
        self.filterModel.setSourceModel(self.model)

    def initUI(self):
        sortB = QtGui.QPushButton("Sort", self)
        sortB.move(250, 20)

        self.sortType = QtGui.QCheckBox("Ascending")
        self.sortType.move(250, 60)

        self.connect(sortB, QtCore.SIGNAL('clicked()'), self.sortItems)

        self.lv = QtGui.QListView(self)
        self.lv.setModel(self.filterModel)
        self.lv.setGeometry(20, 20, 200, 150)

    def sortItems(self):
        checked = self.sortType.isChecked()
        if checked:
            self.filterModel.sort(FIRST_COLUMN, QtCore.Qt.AscendingOrder)
        else:
            self.filterModel.sort(FIRST_COLUMN, QtCore.Qt.DescendingOrder)

app = QtGui.QApplication([])
ex = Example()
ex.show()
app.exec_()
