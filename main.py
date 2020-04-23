import sys, os, pygame as pg
from random import randint
from threading import Thread
import glob
from classes import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
pg.font.init()
vec = pg.math.Vector2

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.sina = khar()

    def initUI(self):
        lbl1 = QLabel('Site Maker', self)
        lbl1.move(200, 50)
        QToolTip.setFont(QFont('SansSerif', 50))
        self.resize(440, 250)
        self.center()
        self.setWindowTitle('Site Maker')
        self.setWindowIcon(QIcon('./icons/webb.png'))
        start = QPushButton('START', self)
        start.setToolTip('press it to make sites!')
        start.resize(start.sizeHint())
        start.move(190, 160)
        start.clicked.connect(self.s)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Sure?', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            pg.quit()
            sys.exit()
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
        self.setWindowIcon(QIcon('./icons/webb.png'))

class Hint(QWidget):
    def __init__(self, path):
        super().__init__()
        self.image = path
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hint')
        self.setWindowIcon(QIcon('.\\icons\\help.png'))
        self.label = QLabel('Hint', self)
        self.setGeometry(300, 300, 704, 436)
        pixmap = QPixmap(self.image)
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.label.setGeometry(0,0,pixmap.width(),pixmap.height())
        self.show()


class page(QMainWindow, QWidget):

    def red(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 't'
        self.hint = Hint('.\\hints\\text.png')

    def blue(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '.', "JPEG files (*.jpg *.jpeg);;PNG files (*.png)")
        imagePath = fname[0]
        self.d = 'i'
        self.done(imagePath)

    def vid(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '.', "MP4 files (*.mp4);;MKV files (*.mkv)")
        imagePath = fname[0]
        self.d = 'v'
        self.done(imagePath)


    def table(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 'ta'
        self.hint = Hint('.\\hints\\table.png')


    def button(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 'b'
        self.hint = Hint('.\\hints\\button.png')

    def delete(self):
        doc = self.textedit.document()
        block = doc.begin()
        lines = [block.text()]
        if lines != ['']:
            for i in range(1, doc.blockCount()):
                block = block.next()
                lines.append(block.text())
            path = os.path.join(self.projection ,lines[0] + '.txt')
            os.remove(path)
            for sprite in self.gui.sprites:
                if path == sprite.file:
                    sprite.kill()
                    self.gui.sprites.remove(sprite)
                    break

    def compile(self):
        os.system("py html."+ open("info.ini", 'r').readline() +" --file " + self.projection)

    def done(self, a = ""):
        if self.d != 'i' and self.d != 'v':
            doc = self.textedit.document()
            block = doc.begin()
            lines = [block.text()]
            for i in range(1, doc.blockCount()):
                block = block.next()
                lines.append(block.text())
        if self.d != 'p':
            border_radius = 0
            if self.projection != '':
                if self.d != 'i' and self.d != 'v':
                    file = os.path.join(self.projection ,lines[0]) + '.txt'
                else:
                    file = os.path.join(self.projection ,a.split('/')[-1]) + '.txt'
                    print(a.split('/')[-1])
                self.w = open(file, 'w')
            else:
                return
        if self.d == 'i':
            p = a + '\n'
        elif self.d == 't':
            p = lines[0] + '.txt' + '\n'
        elif self.d == 'b':
            p = lines[0] + 'btn' + '\n'
        elif self.d == 'I':
            p = lines[0] + 'inp' + '\n'
        elif self.d == 'p':
            lines[0] += '.site'
        elif self.d == 'v':
            p = a.split('\\')[-1] + '.vid' +'\n'
        elif self.d == 'ta':
            p = lines[0] + '.tab'+'\n'
        else:pass
        try:
            color = lines[-1]
            size = lines[-2]
            font = lines[-3]
            txt = lines[1:-3]
            if lines[-1] == "default":
                color = 'black'
                font = 'arial'
                size = '20'
                txt = lines[1:-1]
        except:pass
        if self.d != 'i' and self.d != 'v':
            for i in range(1, len(lines)):
                if lines[i] == '':
                    continue
                if self.d == 'b':
                    if 'script:' in lines[i] and lines[i][-3:] == '.js':
                        p += lines[i].split(':')[-1]
                        if i != len(lines) - 1:
                            p += '\n'
                        continue
                if 'border_radius' in lines[i]:
                    border_radius = int(lines[i].split(':')[-1])
                    p += 'border-radius:'+str(border_radius) + '\n'
                    continue
                if lines[i] == 'default':
                    p += font + '\n'
                    p += size + '\n'
                    p += color
                else:
                    p += lines[i]
                if i != len(lines) - 1:
                    p += '\n'
        if self.d == 'p':
            self.projection = lines[0]
            try:
                os.mkdir(lines[0])
            except:
                reply = QMessageBox.question(self, 'Folder Found', 'This project is already exist. Do you want to replace it?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    for i in os.listdir(lines[0]):
                        os.remove(i)
                else:
                    self.projection = ''
                    return
            return
        elif self.d == 't':
            self.gui.add_item(Text(txt, (randint(1, 100), randint(1, 100)), file, font, int(size), dictionary[color]))
            self.gui.update()
        elif self.d == 'i':
            self.gui.add_item(Image(a, (randint(1, 100), randint(1, 100)), file))
            self.gui.update()
        elif self.d == 'b':
            self.gui.add_item(Button(file, lines[0], dictionary[lines[1]], (randint(1, 100), randint(1, 100)), (70, 40), border_radius = border_radius))
            self.gui.update()
        elif self.d == 'I':
            self.gui.add_item(Input(file, (randint(1, 100), randint(1, 100)), (300, 40), dictionary[lines[1]], border_radius))
            self.gui.update()
        elif self.d == 'v':
            self.gui.add_item(Movie(file, (randint(1, 100), randint(1, 100)), (300, 200)))
            self.gui.update()
        elif self.d == 'ta':
            self.gui.add_item(Table((randint(1, 100), randint(1, 100)) , int(lines[-1]), lines[2:-2], file))
            self.gui.update()
        if self.d != 'p':
            self.w.write(p)
            self.w.close()

    def load(self):
        self.gui.sprites = pg.sprite.Group()
        file = str(QFileDialog.getExistingDirectory(self, "Select project .site"))
        for i in os.listdir(file):
            if i[-4:] == '.txt':
                with open(os.path.join(file, i), 'r') as f:
                    lines = f.readlines()
                    f.close()
                if lines[0][-5:-1] == '.txt':
                    l = []
                    for i in lines[1:-5]:
                        l.append(i[:-1])
                    self.gui.add_item(Text(l, (int(lines[-1].split()[0]), int(lines[-1].split()[-1])), os.path.join(file, i), lines[-5], int(lines[-4]), dictionary[lines[-3][:-1]]))
                    self.gui.update()
                elif lines[0][-5:-1] == '.png':
                    self.gui.add_item(Image(lines[0][:-1], (int(lines[-1].split()[0]), int(lines[-1].split()[-1][:-1])), os.path.join(file, i)))
                    self.gui.update()
                elif lines[0][-4:-1] == 'btn':
                    border_radius = 0
                    for i in lines:
                        if 'border-radius' in i:
                            border_radius = int(i.split(':')[-1])
                            break
                    self.gui.add_item(Button(os.path.join(file, i), lines[0][:-4], dictionary[lines[1][:-1]], (int(lines[-1].split()[0]), int(lines[-1].split()[-1][:-1])), (int(lines[-2].split()[0]), int(lines[-2].split()[-1])), border_radius = border_radius))
                    self.gui.update()
                elif lines[0][-4:-1] == 'inp':
                    border_radius = 0
                    for i in lines:
                        if 'border-radius' in i:
                            border_radius = int(i.split(':')[-1])
                            break
                    self.gui.add_item(Input(os.path.join(file, i), (int(lines[-1].split()[0]), int(lines[-1].split()[-1])), (int(lines[-2].split()[0]), int(lines[-2].split()[-1])), dictionary[lines[1][:-1]], border_radius))
                    self.gui.update()
                elif lines[0][-4:-1] == 'vid':
                    self.gui.add_item(Movie(os.path.join(file, i), (int(lines[-1].split()[0]), int(lines[-1].split()[-1])), (int(lines[-2].split()[0]), int(lines[-2].split()[-1]))))
                    self.gui.update()
                elif lines[0][-5:-1] == '.tab':
                    heads = []
                    for i in lines[2:-4]:
                        heads.append(i[:-1])
                    t = Table((int(lines[-1].split()[0]), int(lines[-1].split()[-1][:-1])) , int(lines[-3][:-1]), heads, os.path.join(file, i))
                    with open(os.path.join(file, lines[0][:-1] + '.data'), 'r') as f:
                        data = f.readlines()
                        for i in range(len(data)):
                            data[i] = data[i].split('\n')[0].split()
                        f.close()
                    t.boxes = []
                    for i in data:
                        a = []
                        for j in i:
                            w = ''
                            if j != '*':
                                w = j
                            a.append(Box(w, (0, 0)))
                        t.boxes.append(a)
                    t.get_geo(len(t.boxes[0]), len(t.boxes))
                    t.image = pg.Surface((t.max * (len(t.boxes[0])), t.high * (len(t.boxes) + 1)))
                    t.image.fill((255, 255, 255))
                    pg.draw.line(t.image, (0, 0, 0), (0, 0), (0, t.image.get_height()))
                    for i in range(1, len(t.boxes[0]) + 1):
                        pg.draw.line(t.image, (0, 0, 0), (t.image.get_width() // (len(t.boxes[0])) * i, 0), (t.image.get_width() // (len(t.boxes[0])) * i,t.image.get_height()), 3)
                    pg.draw.line(t.image, (0, 0, 0), (0, 0), (t.image.get_width(), 0))
                    for i in range(1,(len(t.boxes) + 2)):
                        pg.draw.line(t.image, (0, 0, 0), (0, t.image.get_height() // (len(t.boxes) + 1) * i), (t.image.get_width(), t.image.get_height() // (len(t.boxes) + 1) * i), 3)
                    position = [t.image.get_width() // (len(t.boxes[0])), t.image.get_height() // (len(t.boxes) + 1)]
                    column = 0
                    for text in t.heads:
                        i = Box(text[:-1], (0, 0))
                        i.rect.x, i.rect.y = position[0] * column + 5, 5
                        t.image.blit(i.image, i.rect)
                        column += 1
                    column = 1
                    for text in t.boxes:
                        sheet = 0
                        for i in text:
                            i.rect.x, i.rect.y= position[0] * sheet, position[1] * column
                            i.indexing = [column- 1, sheet]
                            t.image.blit(i.image, i.rect)
                            sheet += 1
                        column += 1
                    t.rect = t.image.get_rect()
                    t.rect.x, t.rect.y = int(lines[-1].split()[0]), int(lines[-1].split()[-1][:-1])
                    self.gui.add_item(t)
                    self.gui.update()
        self.projection = file

    def create(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 'p'

    def __init__(self):
        super().__init__()
        self.gui = GUI()
        self.sele = None
        self.projection = ''
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        sina = QAction(QIcon('./icons/web.png'), 'text', self)
        sina.setStatusTip('Text Box')
        sina.triggered.connect(self.red)
        hasan = QAction(QIcon('./icons/img.png'), 'image', self)
        hasan.setStatusTip('Add Image')
        hasan.triggered.connect(self.blue)
        vid=QAction(QIcon('./icons/vid.png'), 'video', self)
        vid.setStatusTip('Add Video')
        vid.triggered.connect(self.vid)
        button = QAction(QIcon('./icons/button.png'), 'button', self)
        button.setStatusTip('Add Button')
        button.triggered.connect(self.button)
        table=QAction(QIcon('./icons/table.png'), 'table', self)
        table.setStatusTip('Add Table')
        table.triggered.connect(self.table)
        save = QAction(QIcon('./icons/save.png'), 'save', self)
        save.setStatusTip('Save')
        save.triggered.connect(self.done)
        gg = QAction(QIcon('./icons/exit24.png'), 'undo', self)
        delete = QAction(QIcon('./icons/delete.png'), 'delete', self)
        delete.triggered.connect(self.delete)
        delete.setStatusTip('Delete file')
        load = QAction(QIcon('./icons/open.png'), 'open', self)
        load.triggered.connect(self.load)
        load.setStatusTip('open previous projects')
        new = QAction(QIcon('./icons/new.png'), 'New Project', self)
        new.triggered.connect(self.create)
        inp = QAction(QIcon('./icons/input.png'), 'input box', self)
        inp.triggered.connect(self.inpt)
        cmple = QAction(QIcon("./icons/compile.png"), 'Build', self)
        cmple.triggered.connect(self.compile)
        self.statusBar()
        toolbar = self.addToolBar('site')
        toolbar.addAction(new)
        toolbar.addAction(load)
        toolbar.addAction(sina)
        toolbar.addAction(hasan)
        toolbar.addAction(button)
        toolbar.addAction(inp)
        toolbar.addAction(table)
        toolbar.addAction(vid)
        toolbar.addAction(save)
        toolbar.addAction(delete)
        toolbar.addAction(cmple)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Site Maker')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Sure?', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            pg.quit()
            sys.exit()
        else:
            event.ignore()

    def inpt(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 'I'
        self.hint = Hint(".\\hints\\input.png")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
