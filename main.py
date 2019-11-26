import sys

from PyQt5.QtWidgets import (QMainWindow, QWidget, QToolTip, 
    QPushButton,QMessageBox , QApplication, QDesktopWidget, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        lbl1 = QLabel('Site Maker', self)
        lbl1.move(200, 50)
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.resize(440,250)
        self.center()
        self.setWindowTitle('Site Maker')
        self.setWindowIcon(QIcon('webb.png'))        
        
        start=QPushButton('START',self)
        start.setToolTip('press it to make sites!')
        start.resize(start.sizeHint())
        start.move(190,160)
        
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
##class Example(QMainWindow):
##    
##    def __init__(self):
##        super().__init__()
##        
##        self.initUI()
##        
##        
##    def initUI(self):               
##        
##        self.statusBar().showMessage('Site Maker')
##        
##        self.setGeometry(300, 300, 250, 150)
##        self.setWindowTitle('Statusbar')    
##        self.show()
##        
##        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

