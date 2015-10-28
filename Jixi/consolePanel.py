from PyQt4 import QtGui, QtCore
from Jixi.jFieldset import jFieldset

class consolePanel(jFieldset):
    def __init__(self):
        super(consolePanel, self).__init__('Console')
        t = QtGui.QTableWidget(1,4)
        t.setHorizontalHeaderLabels(['Command','Sent','Done','Response'])
        self.grid.addWidget(t,0,0)
