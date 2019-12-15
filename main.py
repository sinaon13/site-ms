import sys
import os

from PyQt5.QtWidgets import (QMainWindow, QWidget, QToolTip, 
    QPushButton,QMessageBox ,QLineEdit, QApplication, QDesktopWidget, QLabel,QLineEdit, QTextEdit, QAction)
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
        
        self.statusBar().showMessage('Site Builder')
        
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
class page(QMainWindow,QWidget):

    def red(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d='t'
    def blue(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d='i'
    def delete(self):
        doc = self.textedit.document()
        block = doc.begin()
        lines = [ block.text() ]
        if lines!=['']:
            for i in range( 1, doc.blockCount() ):
                block = block.next()
                lines.append( block.text() )
            os.remove(lines[0])
    def done(self):
        self.rr=(open('t.txt','r')).readlines()
        self.e=int(self.rr[0])
        self.e+=1
        self.wr=open('t.txt','w')
        self.wr.write(str(self.e))
        print(self.e)
        self.wr.close()
        doc = self.textedit.document()
        block = doc.begin()
        lines = [ block.text() ]
        for i in range( 1, doc.blockCount() ):
            block = block.next()
            lines.append( block.text() )
        cors=lines[-1].split()
        self.cords=[int(cors[0]),int(cors[1])]
        print(self.cords)
        self.w=open(lines[0]+'.txt','w')
        if self.d=='i':
            p=lines[0]+'.img'+'\n'
        elif self.d=='t':
            p=lines[0]+'.txt'+'\n'
        for i in range(1,len(lines)):
            if lines[i]=='':
                p+='\n'
            elif lines[i]!='' and i!= len(lines)-1:
                p+=lines[i]+'\n'
            else:
                p+=lines[i]
        self.w.write(p)
        self.w.close()
        print(p)
        
    def __init__(self):
        super().__init__( )
        
        self.initUI()
        
    def initUI(self):               
        
        QToolTip.setFont(QFont('SansSerif', 10))
##        self.textbox = QLineEdit(self)
##        self.textbox.move(20, 20)
##        self.textbox.resize(280,40)
        sina = QAction(QIcon('text.png'), 'text', self)
        sina.setStatusTip('Text Box')
        sina.triggered.connect(self.red)
        hasan= QAction(QIcon('img.png'), 'image', self)
        hasan.setStatusTip('Add Image')
        hasan.triggered.connect(self.blue)
        save = QAction(QIcon('save.png'),'save', self)
        save.setStatusTip('Save text')
        save.triggered.connect(self.done)
        gg = QAction(QIcon('exit24.png'), 'undo', self)
        delete=QAction(QIcon('delete.png'),'delete',self)
        delete.triggered.connect(self.delete)
        delete.setStatusTip('Delete file')
        self.statusBar()
        

        menubar = self.menuBar()
        editmenu = menubar.addMenu('edit')
        editmenu.addAction(gg)
        toolbar = self.addToolBar('site')
        toolbar.addAction(sina)
        toolbar.addAction(hasan)
        toolbar.addAction(save)
        toolbar.addAction(delete)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Site Maker')    
        self.show()
        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

