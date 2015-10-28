from PyQt4 import QtGui, QtCore
import os

class fileTab(QtGui.QWidget):
    def __init__(self):
        super(fileTab, self).__init__()
        btn = QtGui.QPushButton('Open')
        btn.setStatusTip('Select g-code file')
        btn.clicked.connect(self.showDialog)

        self.fnamew = QtGui.QLabel()
        self.fstatw = QtGui.QLabel()

        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(QtGui.QLabel('Filename'),0,0)
        self.grid.addWidget(btn,0,1)
        self.grid.addWidget(self.fnamew,1,0,1,2)
        self.grid.addWidget(self.fstatw,2,0,1,2)

        self.setLayout(self.grid)

    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        self.fnamew.setText(fname)
        fs = os.stat(fname)
        self.fstatw.setText('File is ' + str(fs.st_size/1024) + ' Kb')

