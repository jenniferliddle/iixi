from PyQt4 import QtGui, QtCore

class commandTab(QtGui.QWidget):
    def __init__(self):
        super(commandTab, self).__init__()
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(QtGui.QLabel('Filename'),0,0)

        self.setLayout(self.grid)

