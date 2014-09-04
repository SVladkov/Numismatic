from PyQt4 import QtCore, QtGui

class MainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setGeometry(300, 150, 700, 500)
		self.central_widget = QtGui.QStackedWidget()
		self.setCentralWidget(self.central_widget)
		
		self.login_widget = LoginWidget(self)
		self.login_widget.button.clicked.connect(self.open_example)
		self.central_widget.addWidget(self.login_widget)
	
	def login(self):
		logged_in_widget = LoggedWidget(self)
		self.central_widget.addWidget(logged_in_widget)
		self.central_widget.setCurrentWidget(logged_in_widget)
	
	def open_example(self):
		example = Example(self)
		self.central_widget.addWidget(example)
		self.central_widget.setCurrentWidget(example)
	
	def return_back(self):
		self.central_widget.setCurrentWidget(self.login_widget)
		
class LoginWidget(QtGui.QWidget):
	def __init__(self, parent=None):
		super(LoginWidget, self).__init__(parent)
		layout = QtGui.QHBoxLayout()
		self.button = QtGui.QPushButton('Login')
		layout.addWidget(self.button)
		self.setLayout(layout)
		# you might want to do self.button.click.connect(self.parent().login) here


class LoggedWidget(QtGui.QWidget):
	def __init__(self, parent=None):
		super(LoggedWidget, self).__init__(parent)
		layout = QtGui.QHBoxLayout()
		self.label = QtGui.QLabel('logged in!')
		layout.addWidget(self.label)
		self.setLayout(layout)

class Example(QtGui.QWidget):
    
	def __init__(self, parent=None):
		super(Example, self).__init__()
		self.parent = parent
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
		
		cancelButton.clicked.connect(self.return_back)		
		
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
		
	def return_back(self):
		self.close()
		print(self.parent)
		self.parent.return_back()
		
	def hide(self):
		self.hide()
		
		
app = QtGui.QApplication([])
window = MainWindow()
window.show()
app.exec_()