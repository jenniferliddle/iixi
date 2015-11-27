from PyQt4 import QtGui, QtCore
from Jixi.jFieldset import jFieldset
from Jixi.fileTab import fileTab
from Jixi.commandTab import commandTab

class commandPanel(jFieldset):

    serial_send_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(commandPanel, self).__init__()
        t = QtGui.QTabWidget()

        ft = fileTab()
        ft.serial_send_signal.connect(self.serial_send_signal)
        t.addTab(ft,'File')

        ct = commandTab()
        ct.serial_send_signal.connect(self.serial_send_signal)
        t.addTab(ct,'Commands')
        self.grid.addWidget(t,0,0)

