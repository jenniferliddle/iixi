from PyQt4 import QtGui, QtCore
from Jixi.jFieldset import jFieldset
from Jixi.fileTab import fileTab
from Jixi.commandTab import commandTab

class commandPanel(jFieldset):
    def __init__(self):
        super(commandPanel, self).__init__()
        t = QtGui.QTabWidget()
        t.addTab(fileTab(),'File')
        t.addTab(commandTab(),'Commands')
        self.grid.addWidget(t,0,0)

