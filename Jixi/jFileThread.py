from PyQt4.QtCore import QThread, pyqtSignal
from PyQt4 import QtCore
from serial import SerialException
import Jixi.jStatus
import time

class jFileThread(QThread):

    serial_send_signal = pyqtSignal(str)

    def __init__(self, filename=''):
        QThread.__init__(self)
        self.filename = filename
        if (filename): self.open()

    def __del__(self):
        self.wait()

    def setFilename(self,filename):
        self.filename = filename

    def setStatus(self,status):
        self.status = status

    def open(self):
        self.fd = open(self.filename,'r')

    def cancel(self):
        self.setStatus('cancel')
        self.fd.close()
        self.terminate()

    def run(self):
        while (True):
            if (self.status == 'send'):
                if (self.fd and not self.fd.closed):
                    line = self.fd.readline()
                    if (line == ''):
                        self.fd.close()
                        self.terminate()
                    self.serial_send_signal.emit(line)
                    

