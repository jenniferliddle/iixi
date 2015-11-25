from PyQt4 import QtGui, QtCore
from Jixi.jFieldset import jFieldset

class connectionPanel(jFieldset):
    def __init__(self):
        super(connectionPanel, self).__init__('Connection')

        self.config = QtCore.QCoreApplication.instance().config

        self.grid.addWidget(QtGui.QLabel('Port'),0,0)
        self.portw = QtGui.QLineEdit()
        self.portw.setText(self.config.get('Comms','port'))
        self.portw.textChanged[str].connect(self.portChanged)
        self.grid.addWidget(self.portw,0,1,1,2)

        self.grid.addWidget(QtGui.QLabel('Baud'),1,0)
        self.baudw = QtGui.QComboBox()
        self.baudw.addItem('115200')
        self.baudw.addItem('9600')
        self.baudw.addItem('4800')
        self.baudw.addItem('1200')
        i = self.baudw.findText(self.config.get('Comms','baud'))
        if (i >= 0): self.baudw.setCurrentIndex(i)

        self.baudw.activated[str].connect(self.baudChanged)
        self.grid.addWidget(self.baudw,1,1)

        self.connectw = QtGui.QPushButton('Connect')
        self.grid.addWidget(self.connectw,1,2)

    def portChanged(self, text):
        if (str(text) != self.config.get('Comms','port')):
            print "Was " + self.config.get('Comms','port') + ' is now ' + str(text)
            self.config.set('Comms','port',str(text))
            self.config.save()

    def baudChanged(self, text):
        if (text != self.config.get('Comms','baud')):
            self.config.set('Comms','baud',str(text))
            self.config.save()

    def show_connected(self, isconnected):
        if (isconnected):
            self.connectw.setStyleSheet("background-color: green")
        else:
            self.connectw.setStyleSheet("background-color: red")
