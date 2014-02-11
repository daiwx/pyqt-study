#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore


class MyDelegate(QtGui.QStyledItemDelegate):
    def __init__(self):
        super(MyDelegate, self).__init__()

    def createEditor(self, parent, option, index):
        editor = QtGui.QSpinBox(parent)
        editor.setMinimum(0)
        editor.setMaximum(100)
        return editor

    def setEditorData(self, editor, index):
        model = index.model()
        role = QtCore.Qt.DisplayRole
        value = model.data(index, role)
        editor.setValue(int(value))

    def setModelData(self, editor, model, index):
        value = editor.value()
        model.setData(index, value)

    def updateEditorGeometry(self, editor, option, dummy):
        r = option.rect
        r.setHeight(30)
        editor.setGeometry(r)


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle("Delegate")

        self.initData()
        self.initUI()

    def initData(self):
        names = []
        names.append("0")
        names.append("1")
        names.append("2")
        names.append("3")
        names.append("4")

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
