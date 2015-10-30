#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

def msg(txt):
    w = QtCore.QCoreApplication.instance().topLevelWidgets()[0].statusBar()
    w.showMessage(txt)

def warning(txt):
    # I'm hoping to work out how to put different message types in different colours...
    msg(txt)

def error(txt):
    msg(txt)


