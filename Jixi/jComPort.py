from PyQt4 import QtCore
import serial
import Jixi.jStatus


class jComPort(serial.Serial):

    def __init__(self):
        serial.Serial.__init__(self)

    def __del__(self):
        if self.isOpen(): self.close()

    def open(self):
        self.port = 'jport'
        try:
            super(jComPort,self).open()
        except serial.SerialException as e:
            Jixi.jStatus.error(e.message)
        except ValueError as e:
            Jixi.jStatus.error(e.message)

    def read(self):
        if (not self.isOpen()): self.open()
        c = ''
        try:
            c = super(jComPort,self).read()
        except serial.SerialException as e:
            Jixi.jStatus.error(e.message)
        except ValueError as e:
            Jixi.jStatus.error(e.message)
        return c

    def write(self,txt):
        if (not self.isOpen()): self.open()
        super(jComPort,self).write(txt)

