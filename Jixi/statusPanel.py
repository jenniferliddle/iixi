from PyQt4 import QtGui, QtCore
from Jixi.jFieldset import jFieldset

class statusPanel(jFieldset):
    def __init__(self):
        super(statusPanel, self).__init__('Status')

        self.grid.addWidget(QtGui.QLabel('Active State:'),0,0, 1, 2)
        self.grid.addWidget(QtGui.QLabel('Last Comment:'),1,0, 1, 2)
        self.grid.addWidget(QtGui.QLabel('Work Position'),3,0, 1, 2)
        self.grid.addWidget(QtGui.QLabel('Machine Position'),3,2, 1, 2)

        self.grid.addWidget(QtGui.QLabel('X:'),4,0)
        self.grid.addWidget(QtGui.QLabel('Y:'),5,0)
        self.grid.addWidget(QtGui.QLabel('Z:'),6,0)

        self.grid.addWidget(QtGui.QLabel('X:'),4,2)
        self.grid.addWidget(QtGui.QLabel('Y:'),5,2)
        self.grid.addWidget(QtGui.QLabel('Z:'),6,2)
