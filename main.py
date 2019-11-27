import sys

from PyQt5.QtWidgets import (QMainWindow, QWidget, QToolTip, 
    QPushButton,QMessageBox , QApplication, QDesktopWidget, QLabel,QLineEdit, QTextEdit, QAction)
from PyQt5.QtGui import QIcon,QFont
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self. sina = khar()
        
    def initUI(self):
        
        lbl1 = QLabel('Site Maker', self)
        lbl1.move(200, 50)
        
        QToolTip.setFont(QFont('SansSerif', 50))

        self.resize(440,250)
        self.center()
        self.setWindowTitle('Site Maker')
        self.setWindowIcon(QIcon('webb.png'))        

        start=QPushButton('START',self)
        start.setToolTip('press it to make sites!')
        start.resize(start.sizeHint())
        start.move(190,160)
        start.clicked.connect(self.s)
        
        self.show() 
        
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Sure?',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  
    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def s(self):
        self.page = page()
        
class khar(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.statusBar().showMessage('Site Maker')
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')    
        self.show()
        
class khar(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        self.setWindowTitle('Site Maker')
        self.setWindowIcon(QIcon('webb.png'))

class page(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        QToolTip.setFont(QFont('SansSerif', 10))
        exitAct = QAction(QIcon('web.png'), 'text', self)
        exitAct.setStatusTip('Text Box')
        exitAct.triggered.connect(self.close)

        self.statusBar()



        toolbar = self.addToolBar('text')
        toolbar.addAction(exitAct)
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Site Maker')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

