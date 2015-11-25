from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL

import serial
import Jixi.jStatus


class jComPort(QtCore.QObject):

    connected = QtCore.pyqtSignal(bool)

    def __init__(self):
        self.serial = serial.Serial()
        #serial.Serial.__init__(self)
        QtCore.QObject.__init__(self)

    def __del__(self):
        if self.isOpen(): self.serial.close()

    def open(self):
        print "Trying toopen port"
        self.serial.port = 'jport'
        try:
            #super(jComPort,self).open()
            self.serial.open()
        except serial.SerialException as e:
            Jixi.jStatus.error(e.message)
        except ValueError as e:
            Jixi.jStatus.error(e.message)

        print "sending signal"
        self.connected.emit(self.isOpen())

    def read(self):
        if (not self.isOpen()): self.open()
        c = ''
        try:
            #c = super(jComPort,self).read()
            c = self.serial.read()
        except serial.SerialException as e:
            Jixi.jStatus.error(e.message)
        except ValueError as e:
            Jixi.jStatus.error(e.message)
        return c

    def write(self,txt):
        if (not self.isOpen()): self.open()
        #super(jComPort,self).write(txt)
        self.serial.write(txt)

    def isOpen(self):
        return self.serial.isOpen()

