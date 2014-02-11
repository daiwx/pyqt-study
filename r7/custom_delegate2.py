#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore


class MyDelegate(QtGui.QStyledItemDelegate):
    def __init__(self):
        super(MyDelegate, self).__init__()

    def paint(self, painter, option, index):
        painter.save()

        painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))

        if option.state & QtGui.QStyle.State_Selected:
            brush = QtGui.QBrush(QtGui.QColor("#66ff71"))
            painter.setBrush(brush)
        else:
            brush = QtGui.QBrush(QtCore.Qt.white)
            painter.setBrush(brush)

        painter.drawRect(option.rect)

        painter.setPen(QtGui.QPen(QtCore.Qt.blue))
        text = index.data(QtCore.Qt.DisplayRole)
        align = QtCore.Qt.AlignCenter
        painter.drawText(option.rect, align, text)

        painter.restore()


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle("Delegate")

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

    def initUI(self):
        lv = QtGui.QListView(self)
        lv.setModel(self.model)

        self.de = MyDelegate()
        lv.setItemDelegate(self.de)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(lv)
        self.setLayout(layout)

app = QtGui.QApplication([])
ex = Example()
ex.show()
app.exec_()
