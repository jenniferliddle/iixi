from PyQt4.QtCore import QThread, SIGNAL
import serial
import Jixi.jStatus


class jRead(QThread):

    data = ''

    def __init__(self, port):
        QThread.__init__(self)
        Jixi.jStatus.msg(port.name)
        self.port = port

    def __del__(self):
        self.port.close()
        self.wait()

    def run(self):
        line = ''
        while (True):
            c = self.port.read()
            if (c == '?'):
                self.emit(SIGNAL('read_data(QString)'), c)
            if (c == '\n'):
                self.emit(SIGNAL('read_data(QString)'), line)
                line = ''
            else:
                line += c

