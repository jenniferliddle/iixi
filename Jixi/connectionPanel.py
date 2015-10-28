from PyQt4 import QtGui, QtCore
from Jixi.jFieldset import jFieldset

class connectionPanel(jFieldset):
    def __init__(self):
        super(connectionPanel, self).__init__('Connection')
        self.grid.addWidget(QtGui.QLabel('Port'),0,0)
        self.portw = QtGui.QLineEdit()
        self.grid.addWidget(self.portw,0,1,1,2)
        self.grid.addWidget(QtGui.QLabel('Baud'),1,0)
        self.baudw = QtGui.QComboBox()
        self.baudw.addItem('1200')
        self.baudw.addItem('4800')
        self.baudw.addItem('9600')
        self.baudw.addItem('19200')
        self.grid.addWidget(self.baudw,1,1)
        self.grid.addWidget(QtGui.QPushButton('Connect'),1,2)
