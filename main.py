import sys
import os
import pygame as pg

from PyQt5.QtWidgets import (QMainWindow, QWidget, QToolTip, 
    QPushButton,QMessageBox ,QLineEdit, QApplication, QDesktopWidget, QLabel,QLineEdit, QTextEdit, QAction)
from PyQt5.QtGui import QIcon,QFont
class GUI:
    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Sina f**k kesh")
        self.sprites = pg.sprite.Group()
        self.screen.fill((255, 255, 255))
        pg.display.flip()

    def update(self):
        self.screen.fill((255, 255, 255))
        self.sprites.draw(self.screen)
        pg.display.flip()

    def add_item(self, item):
        self.sprites.add(item)

class Text(pg.sprite.Sprite):
    def __init__(self, text, pos, font = None, size = None, color = None):
        pg.sprite.Sprite.__init__(self)
        if font and size and color:
            f = pg.font.Font(pg.font.match_font(font), size)
            txt = f.render(text, True, color)
            self.image = pg.Surface((txt.get_width(),txt.get_height()))
            self.image.blit(txt, (0, 0))

        else:
            f = pg.font.Font('arial', 20)
            txt = f.render(text, True, (0, 0, 0))
            self.image = pg.Surface((txt.get_width(),txt.get_height()))
            self.image.blit(txt, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

class Image(pg.sprite.Sprite):
    def __init__(self, img, pos):
        pg.sprite.Sprite.__init__(self)
        f = pg.image.load(img)
        self.image = pg.Surface(f.get_size())
        self.image.blit(f, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
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
        t = ''
        for i in lines:
            if i == lines[-4]:
                break
            t+= i
            
    def done(self):
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
            p=lines[0]+'\n'
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
        self.gui = GUI()
        self.initUI()
        
    def initUI(self):               
        
        QToolTip.setFont(QFont('SansSerif', 10))
##        self.textbox = QLineEdit(self)
##        self.textbox.move(20, 20)
##        self.textbox.resize(280,40)
        sina = QAction(QIcon('web.png'), 'text', self)
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

