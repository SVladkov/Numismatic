#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
	def __init__(self):
		super(Example, self).__init__()
        
		self.initUI()
        
	def initUI(self):
        
		lbl1 = QtGui.QLabel('Zetcode', self)
		lbl1.move(15, 10)

		lbl2 = QtGui.QLabel('tutorials', self)
		lbl2.move(35, 40)
        
		lbl3 = QtGui.QLabel('for programmers', self)
		lbl3.move(55, 70)        
		
		cancelButton = QtGui.QPushButton("Cancel")
		okButton = QtGui.QPushButton("OK")
		
		hbox = QtGui.QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(okButton)
		hbox.addWidget(cancelButton)

		vbox = QtGui.QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)
        
		self.setLayout(vbox)
       
		self.setGeometry(300, 150, 700, 500)
		self.setWindowTitle('Absolute')    
        
		self.show()
		
	def hide(self):
		self.hide()
		
def main():
	
	app = QtGui.QApplication(sys.argv)
	ex = Example()	
	sys.exit(app.exec_())
	
main()