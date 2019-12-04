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
        
        lbl1 = QLabel('Welcome to << Site Builder >>!!!', self)
        lbl1.move(512 - 70, 50)
        
        QToolTip.setFont(QFont('SansSerif', 10))

        self.resize(1024, 768)
        self.center()
        self.setWindowTitle('Site Builder')
        self.setWindowIcon(QIcon('webb.png'))        

        start=QPushButton('START',self)
        start.setToolTip('press it to make sites!')
        start.resize(start.sizeHint())
        start.move(512 - 30,384 - 10)
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
        
        self.statusBar().showMessage('Site Builder')
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')    
        self.show()
        
class khar(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        self.setWindowTitle('Site Builder')
        self.setWindowIcon(QIcon('webb.png'))

class page(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def edit(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
    
    def initUI(self):               
        menubar = self.menuBar()
        editmenu = menubar.addMenu('edit')
        QToolTip.setFont(QFont('SansSerif', 10))
        save = QAction(QIcon('save.png'), 'save', self)
        save.setStatusTip("Save Edition")
        remove = QAction(QIcon('remove.png'), 'remove', self)
        remove.setStatusTip("Remove")
        sina = QAction(QIcon('web.png'), 'text', self)
        sina.triggered.connect(self.edit)
        sina.setStatusTip("add Textbox")
        hasan= QAction(QIcon('img.png'), 'image', self)
        hasan.setStatusTip("add Image")
        hasan.triggered.connect(self.getImage)
        self.statusBar()
        


        toolbar = self.addToolBar('Text')
        toolbar.addAction(sina)
        toolbar.addAction(hasan)
        toolbar.addAction(remove)
        toolbar.addAction(save)
##        tool = self.addToolBar('img')
##        tool = self.addToolBar(hasan)
        self.setGeometry(0, 0, 1024, 768)
        self.setWindowTitle('Site Builder') 
        self.show()

    def getImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Image Files (*.png, *.jpg, *.gif)", options=options)
        self.im = QPixmap(filename)
        self.label = QLabel()
        self.label.setPixmap(self.im)
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

