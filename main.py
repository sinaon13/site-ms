import sys
import os
import pygame as pg
from threading import Thread
import glob
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
pg.font.init()
vec = pg.math.Vector2
class GUI:
    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("GUI")
        self.sprites = pg.sprite.Group()
        self.mouse = Mouse()
        self.screen.fill((255, 255, 255))
        pg.display.flip()
        Thread(target = self.events).start()

    def events(self):
        distance = vec(0, 0)
        while 1:
            mouse = pg.mouse.get_pressed()
            r, m, l = mouse
            if r:
                hits = pg.sprite.spritecollide(self.mouse, self.sprites, False)
                if hits:
                    if distance == vec(0, 0):
                        distance.x = self.mouse.rect.x - hits[0].rect.x
                        distance.y = self.mouse.rect.y - hits[0].rect.y
                    hits[0].rect.x = self.mouse.rect.x - distance.x
                    hits[0].rect.y = self.mouse.rect.y - distance.y
            else:
                distance = vec(0, 0)
            self.update()

    def update(self):
        self.screen.fill((255, 255, 255))
        self.sprites.draw(self.screen)
        pg.display.flip()

    def add_item(self, item):
        self.sprites.add(item)

class Text(pg.sprite.Sprite):
    def __init__(self, text, pos, file, font = None, size = None, color = None):
        pg.sprite.Sprite.__init__(self)
        if font and size and color:
            f = pg.font.Font(pg.font.match_font(font), size)
            txt = f.render(text, True, color)
            self.image = pg.Surface((txt.get_width(),txt.get_height()))
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(txt, (0, 0))

        else:
            f = pg.font.Font('arial', 20)
            txt = f.render(text, True, (0, 0, 0))
            self.image = pg.Surface((txt.get_width(),txt.get_height()))
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(txt, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.file = file + '.txt'
        Thread(target = self.auto_save).start()

    def auto_save(self):
        while 1:
            with open(self.file, 'r') as f:
                lines = f.readlines()
                l = []
                with open(self.file, 'w') as F:
                    for line in lines[:6]:
                        l.append(line)
                    try:
                        if len(l) < 6:
                            l[-1] += '\n'
                    except:pass
                    for line in l:
                        F.write(line)
                    F.write('\n' + str(self.rect.x) + ' ' + str(self.rect.y))
                    F.close()
                f.close()

class Image(pg.sprite.Sprite):
    def __init__(self, img, pos, file):
        pg.sprite.Sprite.__init__(self)
        f = pg.image.load(img)
        self.image = pg.Surface(f.get_size())
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(f, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.file = file +'.txt'
        Thread(target = self.update).start()

    def update(self):
        while 1:
            try:
                with open(self.file, 'r') as f:
                    lines = f.readlines()[0]
                    with open(self.file, 'w') as F:
                        for i in lines:
                            F.write(i)
                        F.write(str(self.rect.x)+' '+str(self.rect.y))
                        F.close()
                    f.close()
            except:pass

class Mouse(pg.sprite.Sprite, pg.Rect):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((1, 1))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        Thread(target = self.update).start()

    def update(self):
        while 1:
            for event in pg.event.get():
                if event.type == pg.MOUSEMOTION:
                    self.rect.center = event.pos
dictionary = {"red" : (255, 0, 0), "green" : (0, 255, 0), "blue" : (0, 0, 255), "black" : (1, 1, 1), "white" : (255, 255, 255), "yellow" : (255, 255, 0)}
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
            os.remove(lines[0] + ".txt")


    def done(self):
        doc = self.textedit.document()
        block = doc.begin()
        lines = [ block.text() ]
        for i in range( 1, doc.blockCount() ):
            block = block.next()
            lines.append( block.text() )
        self.w=open(lines[0]+'.txt','w')
        if self.d=='i':
            p=lines[0]+'\n'
        elif self.d=='t':
            p=lines[0]+'.txt'+'\n'
        for i in range(1,len(lines)):
            p+=lines[i]
            if i!=len(lines)-1:
                p+='\n'
        if self.d == 't':
            for i in lines[1:-3]:
                self.gui.add_item(Text(i, (0, 0), lines[0], lines[-3], int(lines[-2]), dictionary[lines[-1]]))

        else:
            self.gui.add_item(Image(lines[0], (0, 0), lines[0]))

        self.gui.update()
        self.w.write(p)
        self.w.close()
        print(p)
    
    def load(self):
        menu=self.menuBar()
        menubar=menu.addMenu("loaded")
        self.files=[]
        self.fl=[]
        for self.file in glob.glob("*.txt"):
            self.files.append(self.file)
            self.option=QAction( self.file , self)
            self.fl.append(self.option)
            self.option.triggered.connect(self.loading)
            menubar.addAction(self.option)
    def loading(self):
        print(self.file)
    def __init__(self):
        super().__init__( )
        self.gui = GUI()
        self.sele = None
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
        load=QAction(QIcon('load.png'), 'open', self)
        load.triggered.connect(self.load)
        load.setStatusTip('open previous files')
        self.statusBar()


        toolbar = self.addToolBar('site')
        toolbar.addAction(sina)
        toolbar.addAction(hasan)
        toolbar.addAction(save)
        toolbar.addAction(delete)
        toolbar.addAction(load)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Site Maker')
        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
