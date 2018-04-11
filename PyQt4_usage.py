#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-4-10 上午10:56
# @Author  : Evan
# @File    : PyQt4_usage.py
# @Software: PyCharm Community Edition
import sys
from PyQt4 import QtGui

# def window():
#    app = QtGui.QApplication(sys.argv)
#    w = QtGui.QWidget()
#    b = QtGui.QLabel(w)
#    b.setText("Hello World!")
#    w.setGeometry(100,100,200,50)
#    b.move(50,20)
#    w.setWindowTitle('PyQt4-Test')
#    w.show()
#    sys.exit(app.exec_())
#
# if __name__ == '__main__':
#    window()

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('simple')
widget.show()

sys.exit(app.exec_())