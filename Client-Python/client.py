#!/usr/bin/python2
from PyQt4 import QtGui
import PyQt4
import PyQt4.QtNetwork
import PyQt4.QtWebKit
from os import path, chdir

import error
import gui
import sys
import sip

sys.excepthook = error.excepthook

if __name__ == "__main__":
    #chdir(path.dirname(path.abspath(__file__)))
    # if "-t" in sys.argv: chat.bash()
    # else:
    app = QtGui.QApplication(sys.argv)
    mainWindow = gui.Main()
    mainWindow.show()
    app.exec_()
