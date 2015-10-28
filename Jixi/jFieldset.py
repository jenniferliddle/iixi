#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

class jFieldset(QtGui.QFrame):
    def __init__(self, title=''):
        super(jFieldset,self).__init__()
        self.setFrameShadow(QtGui.QFrame.Sunken)
        self.setFrameShape(QtGui.QFrame.Box)
        self.setMidLineWidth(3)

        vbox = QtGui.QVBoxLayout()

        if (title):
            font = QtGui.QFont("Helvetica [Cronyx]", 8)
            label = QtGui.QLabel(title)
            label.setFont(font)
            #label.setStyleSheet("QLabel { background-color : red; color : blue; }")
            vbox.addWidget(label, alignment = QtCore.Qt.AlignTop)

        self.grid = QtGui.QGridLayout()
        vbox.addLayout(self.grid)
        self.setLayout(vbox)
