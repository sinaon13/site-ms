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


class page(QMainWindow, QWidget):

    def red(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 't'

    def blue(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 'i'

    def vid(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 'v'

    def button(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 'b'

    def delete(self):
        doc = self.textedit.document()
        block = doc.begin()
        lines = [block.text()]
        if lines != ['']:
            for i in range(1, doc.blockCount()):
                block = block.next()
                lines.append(block.text())

            os.remove(lines[0] + '.txt')

    def compile(self):
        os.system("py html."+ open("info.ini", 'r').readline() +" --file " + self.projection)

    def done(self):
        doc = self.textedit.document()
        block = doc.begin()
        lines = [block.text()]
        for i in range(1, doc.blockCount()):
            block = block.next()
            lines.append(block.text())
        if self.d != 'p':
            border_radius = 0
            if self.projection != '':
                file = os.path.join(self.projection ,lines[0]) + '.txt'
                self.w = open(file, 'w')
            else:
                return
        if self.d == 'i':
            p = lines[0] + '\n'
        elif self.d == 't':
            p = lines[0] + '.txt' + '\n'
        elif self.d == 'b':
            p = lines[0] + 'btn' + '\n'
        elif self.d == 'I':
            p = lines[0] + 'inp' + '\n'
        elif self.d == 'p':
            lines[0] += '.site'
        elif self.d == 'v':
            p =lines[0] + '.vid' +'\n'
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
            os.mkdir(lines[0])
            return
        elif self.d == 't':
            self.gui.add_item(Text(txt, (randint(1, 100), randint(1, 100)), file, font, int(size), dictionary[color]))
            self.gui.update()
        elif self.d == 'i':
            self.gui.add_item(Image(file, (randint(1, 100), randint(1, 100)), lines[0]))
            self.gui.update()
        elif self.d == 'b':
            self.gui.add_item(Button(file, lines[0], dictionary[lines[1]], (randint(1, 100), randint(1, 100)), (70, 40), border_radius = border_radius))
            self.gui.update()
            p += 'border-radius:'+str(border_radius) + '\n'
        elif self.d == 'I':
            self.gui.add_item(Input(file, (randint(1, 100), randint(1, 100)), (300, 40), dictionary[lines[1]], border_radius))
            self.gui.update()
            p += 'border-radius:'+str(border_radius)+ '\n'
        elif self.d == 'v':
            self.gui.add_item(Movie(file, (randint(1, 100), randint(1, 100)), border_radius))
            self.gui.update()
        if self.d != 'p':
            self.w.write(p)
            self.w.close()

    def load(self):
        menu = self.menuBar()
        menubar = menu.addMenu('loaded')
        self.files = []
        self.fl = []
        for self.file in glob.glob('*.txt'):
            self.files.append(self.file)
            self.option = QAction(self.file, self)
            self.fl.append(self.option)
            self.option.triggered.connect(self.loading)
            menubar.addAction(self.option)

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
        save = QAction(QIcon('./icons/save.png'), 'save', self)
        save.setStatusTip('Save')
        save.triggered.connect(self.done)
        gg = QAction(QIcon('./icons/exit24.png'), 'undo', self)
        delete = QAction(QIcon('./icons/delete.png'), 'delete', self)
        delete.triggered.connect(self.delete)
        delete.setStatusTip('Delete file')
        load = QAction(QIcon('./icons/load.png'), 'open', self)
        load.triggered.connect(self.load)
        load.setStatusTip('open previous files')
        new = QAction(QIcon('./icons/new.png'), 'New Project', self)
        new.triggered.connect(self.create)
        inp = QAction(QIcon('./icons/input.png'), 'input box', self)
        inp.triggered.connect(self.inpt)
        cmple = QAction(QIcon("./icons/compile.png"), 'Build', self)
        cmple.triggered.connect(self.compile)
        self.statusBar()
        toolbar = self.addToolBar('site')
        toolbar.addAction(new)
        toolbar.addAction(sina)
        toolbar.addAction(hasan)
        toolbar.addAction(vid)
        toolbar.addAction(button)
        toolbar.addAction(inp)
        toolbar.addAction(save)
        toolbar.addAction(delete)
        toolbar.addAction(load)
        toolbar.addAction(cmple)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Site Maker')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Sure?', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            pg.quit()
            sys.exit()
        else:
            event.ignore()

    def inpt(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 'I'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
