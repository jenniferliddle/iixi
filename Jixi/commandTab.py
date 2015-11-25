from PyQt4 import QtGui, QtCore

class commandTab(QtGui.QWidget):
    def __init__(self):
        super(commandTab, self).__init__()

        setHomeBtn = QtGui.QPushButton('Set Home Position')
        setHomeBtn.setStatusTip('Set the current positon to be the home position')
        setHomeBtn.clicked.connect(self.setHomePosition)

        goHomeBtn = QtGui.QPushButton('Return Home')
        goHomeBtn.setStatusTip('Return to the home position')
        goHomeBtn.clicked.connect(self.goHomePosition)

        stepw = QtGui.QDoubleSpinBox()
        stepw.setRange(0.1,10.0)
        stepw.setSingleStep(0.1)
        stepw.setSuffix('mm')

        xplus = QtGui.QPushButton('X+')
        xplus.setFixedSize(50,50)
        xminus = QtGui.QPushButton('X-')
        xminus.setFixedSize(50,50)
        yplus = QtGui.QPushButton('Y+')
        yplus.setFixedSize(50,50)
        yminus = QtGui.QPushButton('Y-')
        yminus.setFixedSize(50,50)
        zplus = QtGui.QPushButton('Z+')
        zplus.setFixedSize(50,50)
        zminus = QtGui.QPushButton('Z-')
        zminus.setFixedSize(50,50)

        self.grid = QtGui.QGridLayout()
        maxcol = 14

        self.grid.addWidget(setHomeBtn,0,0,1,3)
        self.grid.addWidget(goHomeBtn,1,0,1,3)

        self.grid.addWidget(yplus, 2, maxcol-5, 2, 2)
        self.grid.addWidget(xminus, 3, maxcol-7, 2, 2)
        self.grid.addWidget(xplus, 3, maxcol-3, 2, 2)
        self.grid.addWidget(yminus, 5, maxcol-5, 2, 2)
        self.grid.addWidget(zplus, 2, maxcol-1, 2, 2)
        self.grid.addWidget(zminus, 5, maxcol-1, 2, 2)

        self.grid.addWidget(QtGui.QLabel('Step size'),0,maxcol-3, 1, 2)
        self.grid.addWidget(stepw,0,maxcol-1, 1, 2)

        self.setLayout(self.grid)

    def setHomePosition(self):
        p = QtCore.QCoreApplication.instance().topLevelWidgets()[0].comport
        p.write('?')
        return True

    def goHomePosition(self):
        return True

