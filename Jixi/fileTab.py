from PyQt4 import QtGui, QtCore
from Jixi.jFileThread import jFileThread

import os
import time
import Jixi.jStatus
import shlex, subprocess

class fileTab(QtGui.QWidget):

    serial_send_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(fileTab, self).__init__()
        btn = QtGui.QPushButton('Select File')
        btn.setStatusTip('Select g-code file')
        btn.clicked.connect(self.showDialog)

        self.sendBtn = QtGui.QPushButton('Send')
        self.sendBtn.setStatusTip('Send file to X-Carve')
        self.sendBtn.setEnabled(False)
        self.sendBtn.clicked.connect(self.sendFile)

        self.pauseBtn = QtGui.QPushButton('Pause')
        self.pauseBtn.setStatusTip('Pause carving')
        self.pauseBtn.setEnabled(False)
        self.pauseBtn.clicked.connect(self.pauseFile)

        self.cancelBtn = QtGui.QPushButton('Cancel')
        self.cancelBtn.setStatusTip('Cancel carving')
        self.cancelBtn.setEnabled(False)
        self.cancelBtn.clicked.connect(self.cancelFile)

        self.visualizeBtn = QtGui.QPushButton('Visualize')
        self.visualizeBtn.setStatusTip('Visualize file')
        self.visualizeBtn.setEnabled(False)
        self.visualizeBtn.clicked.connect(self.visualizeFile)

        self.fnamew = QtGui.QLabel()
        self.fstatw = QtGui.QLabel()
        self.durationw = QtGui.QLabel()
        self.estimationw = QtGui.QLabel()

        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(QtGui.QLabel('Filename:'),0,0)
        self.grid.addWidget(btn,0,4)

        self.grid.addWidget(self.fnamew,0,1,1,2)
        self.grid.addWidget(self.fstatw,1,0,1,3)
        self.grid.addWidget(self.visualizeBtn,1,4)

        self.grid.addWidget(self.sendBtn,2,0)
        self.grid.addWidget(self.pauseBtn,2,1)
        self.grid.addWidget(self.cancelBtn,2,2)

        self.grid.addWidget(QtGui.QLabel('Duration'),3,0)
        self.grid.addWidget(self.durationw,3,1)

        self.grid.addWidget(QtGui.QLabel('Remaining'),4,0)
        self.grid.addWidget(self.estimationw,4,1)

        self.setLayout(self.grid)

        self.filethread = jFileThread()
        self.filethread.serial_send_signal.connect(self.serial_send_signal)

    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Select file')
        if (fname):
            self.showFileDetails(fname)
            self.sendBtn.setEnabled(True)
            self.pauseBtn.setEnabled(True)
            self.cancelBtn.setEnabled(True)
            self.visualizeBtn.setEnabled(True)

    def sendFile(self):
        Jixi.jStatus.msg('sending')
        self.filethread.setFilename(self.fnamew.text())
        self.filethread.open()
        self.filethread.setStatus('send')
        self.filethread.start()

    def pauseFile(self):
        Jixi.jStatus.msg('pausing')
        self.filethread.setStatus('pause')

    def cancelFile(self):
        Jixi.jStatus.msg('cancelling')
        self.filethread.cancel()

    def visualizeFile(self):
        Jixi.jStatus.msg('visualizing')
        config = QtCore.QCoreApplication.instance().config
        program = config.get('Visualizer','program')
        args = shlex.split(program + ' ' + str(self.fnamew.text()))
        subprocess.Popen(args)        

    def showFileDetails(self, fname):
        self.fnamew.setText(fname)
        fs = os.stat(fname)
        txt = 'Size: '
        txt += '<b>' + str(fs.st_size/1024) + ' Kb</b>'
        txt += '  Date: '
        txt += '<b>' + time.ctime(fs.st_mtime) + '</b>'
        self.fstatw.setText(txt)

