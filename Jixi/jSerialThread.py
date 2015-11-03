from PyQt4.QtCore import QThread
import serial
import Jixi.jStatus


class jSerialThread(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.serial = serial.Serial('jport')
        Jixi.jStatus.msg(self.serial.name)
        self.serial.write('Serial port open!')

    def __del__(self):
        self.serial.close()
        self.wait()

    def run(self):
        pass
