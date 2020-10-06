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
# کلاس راهنمای کاربر
class Hint(QWidget):
    def __init__(self, path):
        super().__init__()
        self.image = path
        self.initUI()
    # تابع مقدار دهی گرافیکی اولیه کلاس
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

#کلاس اصلی
class page(QMainWindow, QWidget):
    # تابع ایجاد کننده صفحه نوشتن برای ساختن متن
    def red(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 't'
        self.hint = Hint('.\\hints\\text.png')
    # تابع اضافه کننده عکس در صفحه
    def blue(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '.', "JPEG files (*.jpg *.jpeg);;PNG files (*.png)")
        imagePath = fname[0]
        imagePath.replace('/', '\\')
        self.d = 'i'
        self.done(imagePath)
    # تابع اضافه کننده فیلم در صفحه
    def vid(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '.', "MP4 files (*.mp4);;MKV files (*.mkv)")
        imagePath = fname[0]
        imagePath.replace('/', '\\')
        self.d = 'v'
        self.done(imagePath)
    # تابع ایجاد کننده صفحه نوشتن برای اضافه کردن جدول در صفحه
    def table(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 'ta'
        self.hint = Hint('.\\hints\\table.png')

    # تابع ایجاد کننده صفحه نوشتن برای اضافه کردن پیوند در صفحه
    def link(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 'l'

    # تابع ایجاد کننده صفحه نوشتن برای اضافه کردن دکمه در صفحه
    def button(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 'b'
        self.hint = Hint('.\\hints\\button.png')
    # تابع حذف کننده یک کلاس از صفحه
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
    # تابع کامپایل کردن همه ی کلاس ها به سایت
    def compile(self):
        os.system("py html."+ open("info.ini", 'r').readline() +" --file " + self.projection)
    # تابع اضافه کننده کلاس مورد نظر به صفحه و ذخیره اطلاعات کلاس
    def done(self, a = ""):
        if self.d != 'i' and self.d != 'v' and self.d != 'p':
            # گرفتن اطلاعات از صفحه نوشتن
            doc = self.textedit.document()
            block = doc.begin()
            lines = [block.text()]
            for i in range(1, doc.blockCount()):
                block = block.next()
                lines.append(block.text())
        if self.d != 'p':
            border_radius = 0
            if self.projection != '':
                # ساختن فایلی برای ذخیره اطلاعات
                if self.d != 'i' and self.d != 'v':
                    file = os.path.join(self.projection ,lines[0]) + '.txt'
                else:
                    file = os.path.join(self.projection ,a.split('/')[-1]) + '.txt'
                self.w = open(file, 'w')
            else:
                return
        # دادن شناسه به فایل ذخیره اطلاعات
        if self.d == 'i':
            p = a + '\n'
        elif self.d == 't':
            p = lines[0] + '.txt' + '\n'
        elif self.d == 'b':
            p = lines[0] + 'btn' + '\n'
        elif self.d == 'I':
            p = lines[0] + 'inp' + '\n'
        elif self.d == 'p':
            a += '.site'
        elif self.d == 'v':
            p = a.split('/')[-1] + '.vid' +'\n'
        elif self.d == 'ta':
            p = lines[0] + '.tab'+'\n'
        elif self.d== 'l':
            p = lines[0] +'.link' + '\n'
        else:pass
        # چک کردن حالت پیش فرض
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
        if self.d != 'i' and self.d != 'v' and self.d != 'p':
            # جمع آوری اطلاعات کلاس مورد نظر
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
            # مقدار دهی آدرس پروژه و چک کردن یکتایی آن در آدرس مورد نظر
            self.projection = a
            try:
                os.mkdir(a)
            except:
                reply = QMessageBox.question(self, 'Folder Found', 'This project is already exist. Do you want to replace it?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    for i in os.listdir(a):
                        os.remove(os.path.join(a,i))
                else:
                    self.projection = ''
                    return
            return
        # ایجاد کلاس های گرافیکی در صفحه
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
            self.gui.add_item(Movie(a, file, (randint(1, 100), randint(1, 100)), (600, 400)))
            self.gui.update()
        elif self.d == 'ta':
            self.gui.add_item(Table((randint(1, 100), randint(1, 100)) , int(lines[-1]), lines[2:-2], file))
            self.gui.update()
        elif self.d == 'l':
            self.gui.add_item(Link(txt[1:], (randint(1, 100), randint(1, 100)), font, int(size), dictionary[color], file))
            self.gui.update()
        if self.d != 'p':
            # نوشتن و ذخیره اطلاعات در فایل مورد نظر
            self.w.write(p)
            self.w.close()
    # تابع باز کننده پروژه های قبلی
    def load(self):
        # مقدار دهی دوباره به صفحه ی گرافیکی
        self.gui.sprites = pg.sprite.Group()
        # گرفتن ادرس پروژه موردنظر
        file = str(QFileDialog.getExistingDirectory(self, "Select project .site"))
        file = file.replace('/', '\\')
        # گرفتن تمام فایل های اطلاعاتی داخل پروژه و ساختن کلاس های گرافیکی با آن
        for i in os.listdir(file):
            if i[-4:] == '.txt':
                with open(os.path.join(file, i), 'r') as f:
                    lines = f.readlines()
                    f.close()
                if lines[0][-5:-1] == '.txt':
                    l = []
                    for j in lines[1:-5]:
                        l.append(j[:-1])
                    self.gui.add_item(Text(l, (int(lines[-1].split()[0]), int(lines[-1].split()[-1])), os.path.join(file, i), lines[-5], int(lines[-4]), dictionary[lines[-3][:-1]]))
                    self.gui.update()
                elif lines[0][-5:-1] == '.png':
                    self.gui.add_item(Image(lines[0][:-1], (int(lines[-1].split()[0]), int(lines[-1].split()[-1])), os.path.join(file, i)))
                    self.gui.update()
                elif lines[0][-4:-1] == 'btn':
                    border_radius = 0
                    for j in lines:
                        if 'border-radius' in j:
                            border_radius = int(j.split(':')[-1])
                            break
                    self.gui.add_item(Button(os.path.join(file, i), lines[0][:-4], dictionary[lines[1][:-1]], (int(lines[-1].split()[0]), int(lines[-1].split()[-1])), (int(lines[-2].split()[0]), int(lines[-2].split()[-1])), border_radius = border_radius))
                    self.gui.update()
                elif lines[0][-4:-1] == 'inp':
                    border_radius = 0
                    for j in lines:
                        if 'border-radius' in j:
                            border_radius = int(i.split(':')[-1])
                            break
                    self.gui.add_item(Input(os.path.join(file, i), (int(lines[-1].split()[0]), int(lines[-1].split()[-1])), (int(lines[-2].split()[0]), int(lines[-2].split()[-1])), dictionary[lines[1][:-1]], border_radius))
                    self.gui.update()
                elif lines[0][-4:-1] == 'vid':
                    self.gui.add_item(Movie(os.path.join(file, i), (int(lines[-1].split()[0]), int(lines[-1].split()[-1])), (int(lines[-2].split()[0]), int(lines[-2].split()[-1]))))
                    self.gui.update()
                elif lines[0][-5:-1] == '.tab':
                    heads = []
                    for j in lines[2:-4]:
                        heads.append(j[:-1])
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
                elif lines[0][-5:-1] == '.link':
                    l = []
                    for j in lines[1:-5]:
                        l.append(j[:-1])
                    self.gui.add_item(Link(l[1:], (int(lines[-1].split()[0]), int(lines[-1].split()[-1])), lines[-5], int(lines[-4]), dictionary[lines[-3][:-1]], os.path.join(file, i)))
                    self.gui.update()
        self.projection = file
    # تابع ایجاد کننده یک پروژه جدید
    def create(self):
        self.gui.sprites = pg.sprite.Group()
        fname, t = QFileDialog.getSaveFileName(self, 'New Project',"")
        fname = fname.replace('/', '\\')
        self.d = 'p'
        print(fname)
        self.done(fname)

    def __init__(self):
        super().__init__()
        self.gui = GUI()
        self.sele = None
        self.projection = ''
        self.initUI()
    # تابع مقدار دهی گرافیکی اولیه کلاس
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        # ساختن و مقدار دهی ماژول های برنامه
        # ساختن ماژول متن
        sina = QAction(QIcon('./icons/web.png'), 'text', self)
        sina.setStatusTip('Text Box')
        sina.triggered.connect(self.red)
        # ساختن ماژول عکس
        hasan = QAction(QIcon('./icons/img.png'), 'image', self)
        hasan.setStatusTip('Add Image')
        hasan.triggered.connect(self.blue)
        # ساختن ماژول فیلم
        vid=QAction(QIcon('./icons/vid.png'), 'video', self)
        vid.setStatusTip('Add Video')
        vid.triggered.connect(self.vid)
        # ساختن ماژول دکمه
        button = QAction(QIcon('./icons/button.png'), 'button', self)
        button.setStatusTip('Add Button')
        button.triggered.connect(self.button)
        # ساختن ماژول جدول
        table=QAction(QIcon('./icons/table.png'), 'table', self)
        table.setStatusTip('Add Table')
        table.triggered.connect(self.table)
        # ساختن ماژول پیوند
        link=QAction(QIcon('./icons/link.png'), 'link',self)
        link.setStatusTip('Make Link')
        link.triggered.connect(self.link)
        # ایجاد ماژول ذخیر اطلاعات
        save = QAction(QIcon('./icons/save.png'), 'save', self)
        save.setStatusTip('Save')
        save.triggered.connect(self.done)
        # دکمه پاک کننده اطلاعات خواسته شده
        delete = QAction(QIcon('./icons/delete.png'), 'delete', self)
        delete.triggered.connect(self.delete)
        delete.setStatusTip('Delete file')
        # دکمه باز کننده پروژه های قبلی
        load = QAction(QIcon('./icons/open.png'), 'open', self)
        load.triggered.connect(self.load)
        load.setStatusTip('open previous projects')
        # دکمه ایجاد کننده یک پروژه جئدید
        new = QAction(QIcon('./icons/new.png'), 'New Project', self)
        new.setStatusTip('create a project')
        new.triggered.connect(self.create)
        # ساختن ماژول ورودی
        inp = QAction(QIcon('./icons/input.png'), 'input box', self)
        inp.triggered.connect(self.inpt)
        inp.setStatusTip('add input box')
        # دکمه کامپایل پروژه به یک سایت
        cmple = QAction(QIcon("./icons/compile.png"), 'Build', self)
        cmple.triggered.connect(self.compile)
        cmple.setStatusTip('compile .site to .html')
        self.statusBar()
        toolbar = self.addToolBar('site')
        # اضافه کردن ماژول ها به صفحه اصلی
        toolbar.addAction(new)
        toolbar.addAction(load)
        toolbar.addAction(sina)
        toolbar.addAction(hasan)
        toolbar.addAction(button)
        toolbar.addAction(inp)
        toolbar.addAction(table)
        toolbar.addAction(vid)
        toolbar.addAction(link)
        toolbar.addAction(save)
        toolbar.addAction(delete)
        toolbar.addAction(cmple)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Site Maker')
        self.show()
    # تابع پردازشگر رویداد بستن
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Sure?', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            pg.quit()
            sys.exit()
        else:
            event.ignore()
    # تابع ایجاد کننده صفحه نوشتن برای اضافه کردن پیوند در صفحه
    def inpt(self):
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)
        self.d = 'I'
        self.hint = Hint(".\\hints\\input.png")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = page()
    sys.exit(app.exec_())
