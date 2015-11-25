from PyQt4.QtCore import QThread, SIGNAL
from serial import SerialException
import Jixi.jStatus
import time

class jRead(QThread):

    data = ''

    def __init__(self, port):
        QThread.__init__(self)
        self.port = port

    def __del__(self):
        self.wait()

    def run(self):
        line = ''
        while (True):
            if (not self.port.isOpen()):
                time.sleep(1)
                continue

            c = ''
            try:
                c = self.port.read()
            except SerialException as e:
                Jixi.jStatus.error(e.message)
            except ValueError as e:
                Jixi.jStatus.error(e.message)

            if (c == '?'):
                self.emit(SIGNAL('read_data(QString)'), c)
            if (c == '\n'):
                self.emit(SIGNAL('read_data(QString)'), line)
                line = ''
            else:
                line += c

