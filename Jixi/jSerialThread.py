from PyQt4.QtCore import QThread, pyqtSignal
from serial import SerialException
import Jixi.jStatus
import time

class jRead(QThread):

    read_signal = pyqtSignal(str)
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
                self.read_signal.emit(c)
            if (c == '\n'):
                self.read_signal.emit(line)
                line = ''
            else:
                line += c

