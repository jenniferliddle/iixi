from PyQt4 import QtGui, QtCore
from Jixi.jFieldset import jFieldset
import re

class statusPanel(jFieldset):
    def __init__(self):
        super(statusPanel, self).__init__('Status')

        self.statew = QtGui.QLabel()
        self.grid.addWidget(QtGui.QLabel('Active State:'),0,0, 1, 2)
        self.grid.addWidget(self.statew,0,2,1,2)
        self.grid.addWidget(QtGui.QLabel('Last Comment:'),1,0, 1, 2)
        self.grid.addWidget(QtGui.QLabel('Work Position'),3,0, 1, 2)
        self.grid.addWidget(QtGui.QLabel('Machine Position'),3,2, 1, 2)

        self.grid.addWidget(QtGui.QLabel('X:'),4,0)
        self.grid.addWidget(QtGui.QLabel('Y:'),5,0)
        self.grid.addWidget(QtGui.QLabel('Z:'),6,0)

        self.grid.addWidget(QtGui.QLabel('X:'),4,2)
        self.grid.addWidget(QtGui.QLabel('Y:'),5,2)
        self.grid.addWidget(QtGui.QLabel('Z:'),6,2)

    def update(self, txt):
        # txt is the status message
        # format <Idle,MPos:0.000,0.000,0.000,WPos:0.000,0.000,0.000>
        txt = txt[1:-1]   # strip angle brackets
        state = re.split(',',txt)[0]
        self.statew.setText(state)
