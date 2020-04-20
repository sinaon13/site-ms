import pygame as pg
from threading import Thread
import os, sys
vec = pg.math.Vector2
class geometric_class(object): # Internal Class
    def __init__(self):
        self.geometric = True
class GUI:
    def __init__(self):
        self.screen = pg.display.set_mode((1800, 900), pg.RESIZABLE)
        pg.display.set_caption('GUI')
        icon = pg.image.load('./icons/webb.ico')
        icon.set_colorkey((0, 0, 0))
        i = pg.Surface(icon.get_size())
        i.blit(icon, (0, 0))
        i.set_colorkey((0, 0, 0))
        pg.display.set_icon(i)
        self.sprites = pg.sprite.Group()
        self.mouse = Mouse()
        self.screen.fill((255, 255, 255))
        pg.display.flip()
        self.clock = pg.time.Clock()
        self.a = Thread(target=(self.events))
        self.a.start()
    def events(self):
        distance = vec(0, 0)
        f = False
        chosen = None
        writing = None
        shifting = 0
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    del self
                    sys.exit()
                if event.type == pg.MOUSEMOTION:
                    self.mouse.rect.x , self.mouse.rect.y = event.pos

                if writing:
                    if event.type == pg.KEYDOWN:
                        text = writing.text
                        if 96 < event.key < 123:
                            text = text[:writing.pointer] + chr(event.key - shifting) + text[writing.pointer:]
                            writing.pointer += 1

                        if event.key == pg.K_BACKSPACE:
                            txt = ''
                            try:
                                writing.pointer -= 1
                                txt = text[:writing.pointer] + text[writing.pointer + 1:]
                            except :pass
                            text = txt
                        b = Box(text, (writing.rect.x, writing.rect.y))
                        chosen.boxes[writing.indexing[0]][writing.indexing[1]] = b
                        b.rect.x, b.rect.y = writing.rect.x, writing.rect.y
                        b.indexing = writing.indexing
                        b.pointer = writing.pointer
                        b.ind = writing.ind
                        writing = b

                        if event.key == pg.K_RSHIFT or event.key == pg.K_LSHIFT:
                            shifting = 32
                        if event.key == pg.K_RIGHT:
                            writing.pointer += 1
                        if event.key == pg.K_LEFT:
                            writing.pointer -= 1
                    if event.type == pg.KEYUP:
                        if event.key == pg.K_RSHIFT or event.key == pg.K_LSHIFT:
                            shifting = 0
            if writing:
                writing.update()
            mouse = pg.mouse.get_pressed()
            r, m, l = mouse
            if r and not f:
                writing = None
                hits = pg.sprite.spritecollide(self.mouse, self.sprites, False)
                if hits:
                    for hit in hits:
                        if "boxes" in dir(hit):
                            chosen = hits[0]
                            for i in chosen.boxes:
                                for j in i:
                                    j.set_text(j.text, j.f)
                                    j.rect.x, j.rect.y = j.rect.x + chosen.rect.x ,j.rect.y + chosen.rect.y
                                    j.pointer = len(j.text)
                                h = pg.sprite.spritecollide(self.mouse, i, False)
                                for j in i:
                                    j.rect.x, j.rect.y = j.rect.x - chosen.rect.x ,j.rect.y - chosen.rect.y
                                if h:
                                    writing = h[0]
                                continue
                            if writing:
                                continue
                if hits:
                    distance.x = self.mouse.rect.x - hits[0].rect.x
                    distance.y = self.mouse.rect.y - hits[0].rect.y
                    chosen = hits[0]
                    f = True
            if not r:
                f = False
            if f:
                if(chosen.geometric):
                    if (distance.x > 4 and distance.x < chosen.w - 4) and (distance.y > 4 and distance.y < chosen.h - 4):
                        chosen.rect.x = self.mouse.rect.x - distance.x
                        chosen.rect.y = self.mouse.rect.y - distance.y
                    else:
                        if(distance.x < 4):
                            chosen.w -= self.mouse.rect.x - (chosen.rect.x + distance.x)
                            chosen.rect.x = self.mouse.rect.x - distance.x
                            x, y = chosen.rect.x, chosen.rect.y
                            distance.x = self.mouse.rect.x - chosen.rect.x
                            distance.y = self.mouse.rect.y - chosen.rect.y
                            if chosen.type == 'button':
                                chosen.__init__(chosen.file, chosen.text, chosen.color, (chosen.rect.x, chosen.rect.y), (int(chosen.w), int(chosen.h)), 'arial', 14, chosen.border_radius)
                            elif chosen.type == 'input':
                                chosen.__init__(chosen.file, (chosen.rect.x, chosen.rect.y), (int(chosen.w), int(chosen.h)), chosen.color, chosen.border_radius)
                            else:
                                chosen.__init__(chosen.file, (chosen.rect.x, chosen.rect.y), (int(chosen.w), int(chosen.h)), chosen.border_radius)
                            chosen.rect = chosen.image.get_rect()
                            chosen.rect.x, chosen.rect.y = x, y
                        if(distance.x > chosen.w - 4):
                            chosen.w += self.mouse.rect.x - (chosen.rect.x + distance.x)
                            distance.x = self.mouse.rect.x - chosen.rect.x
                            distance.y = self.mouse.rect.y - chosen.rect.y
                            if chosen.type == 'button':
                                chosen.__init__(chosen.file, chosen.text, chosen.color, (chosen.rect.x, chosen.rect.y), (int(chosen.w), int(chosen.h)), 'arial', 14, chosen.border_radius)
                            elif chosen.type == 'input':
                                chosen.__init__(chosen.file, (chosen.rect.x, chosen.rect.y), (int(chosen.w), int(chosen.h)), chosen.color, chosen.border_radius)
                            else:
                                chosen.__init__(chosen.file, (chosen.rect.x, chosen.rect.y), (int(chosen.w), int(chosen.h)), chosen.border_radius)
                            x, y = chosen.rect.x, chosen.rect.y
                            chosen.rect = chosen.image.get_rect()
                            chosen.rect.x, chosen.rect.y = x, y
                        if(distance.y < 4):
                            chosen.h -= self.mouse.rect.y - (chosen.rect.y + distance.y)
                            chosen.rect.y = self.mouse.rect.y - distance.y
                            x, y = chosen.rect.x, chosen.rect.y
                            distance.x = self.mouse.rect.x - chosen.rect.x
                            distance.y = self.mouse.rect.y - chosen.rect.y
                            if chosen.type == 'button':
                                chosen.__init__(chosen.file, chosen.text, chosen.color, (chosen.rect.x, chosen.rect.y), (int(chosen.w), int(chosen.h)), 'arial', 14, chosen.border_radius)
                            elif chosen.type == 'input':
                                chosen.__init__(chosen.file, (chosen.rect.x, chosen.rect.y), (int(chosen.w), int(chosen.h)), chosen.color, chosen.border_radius)
                            else:
                                chosen.__init__(chosen.file, (chosen.rect.x, chosen.rect.y), (int(chosen.w), int(chosen.h)), chosen.border_radius)
                            chosen.rect = chosen.image.get_rect()
                            chosen.rect.x, chosen.rect.y = x, y
                        if(distance.y > chosen.h - 4):
                            chosen.h += self.mouse.rect.y - (chosen.rect.y + distance.y)
                            x, y = chosen.rect.x, chosen.rect.y
                            distance.x = self.mouse.rect.x - chosen.rect.x
                            distance.y = self.mouse.rect.y - chosen.rect.y
                            if chosen.type == 'button':
                                chosen.__init__(chosen.file, chosen.text, chosen.color, (chosen.rect.x, chosen.rect.y), (int(chosen.w), int(chosen.h)), 'arial', 14, chosen.border_radius)
                            elif chosen.type == 'input':
                                chosen.__init__(chosen.file, (chosen.rect.x, chosen.rect.y), (int(chosen.w), int(chosen.h)), chosen.color, chosen.border_radius)
                            else:
                                chosen.__init__(chosen.file, (chosen.rect.x, chosen.rect.y), (int(chosen.w), int(chosen.h)), chosen.border_radius)
                            chosen.rect = chosen.image.get_rect()
                            chosen.rect.x, chosen.rect.y = x, y
                else:
                    chosen.rect.x = self.mouse.rect.x - distance.x
                    chosen.rect.y = self.mouse.rect.y - distance.y

            self.sprites.update()
            self.update()

    def update(self):
        self.screen.fill((255, 255, 255))
        self.sprites.draw(self.screen)
        pg.display.flip()

    def add_item(self, item):
        self.sprites.add(item)


class Text(pg.sprite.Sprite):
    def __init__(self, text, pos, file, font='arial', size=20, color=(0, 0, 0)):
        pg.sprite.Sprite.__init__(self)
        self.geometric = False
        self.sheets = len(text)
        f = pg.font.Font(pg.font.match_font(font), size)
        letter = f.render('g', True, color).get_height()
        x = f.render('g', True, color).get_width()
        index = letter * len(text)
        m = 0
        for i in text:
            m = max(len(i), m)

        self.image = pg.Surface((m * x, index))
        self.image.fill((255, 255, 255))
        index = 0
        for i in text:
            txt = f.render(i, True, color)
            self.image.blit(txt, (0, txt.get_height() * index))
            index += 1;
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.file = file
        self.last = self.image.get_rect()

    def update(self):
        if self.last.x != self.rect.x or self.last.y != self.rect.y:
            try:
                with open(self.file, 'r') as f:
                    lines = f.readlines()
                    if len(lines) > 5:
                        lines = lines[:4 + self.sheets]
                    with open(self.file, 'w') as F:
                        for i in lines:
                            if i != lines[-1]:
                                x = i[:-1]

                            else:
                                x = i
                            F.write(x)
                            F.write('\n')
                        F.write(str(self.rect.x) + ' ' + str(self.rect.y))
                        F.close()
                    f.close()
            except:
                pass

            self.last.x = self.rect.x
            self.last.y = self.rect.y

class Image(pg.sprite.Sprite):

    def __init__(self, img, pos, file):
        pg.sprite.Sprite.__init__(self)
        self.geometric = False
        f = pg.image.load(img)
        self.image = pg.Surface(f.get_size())
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(f, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.file = file
        self.last = self.image.get_rect()
        self.last.x = self.rect.x
        self.last.y = self.rect.y

    def update(self):
        if self.last.x != self.rect.x or self.last.y != self.rect.y:
            try:
                with open(self.file, 'r') as (f):
                    lines = f.readlines()[0]
                    with open(self.file, 'w') as (F):
                        for i in lines:
                            F.write(i)

                        F.write(str(self.rect.x) + ' ' + str(self.rect.y))
                        F.close()
                    f.close()
            except:
                pass

            self.last.x = self.rect.x
            self.last.y = self.rect.y

class Mouse(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((1, 1))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class Button(pg.sprite.Sprite, geometric_class):
    def __init__(self, file, text, color, pos, size, font = 'arial', font_size = 14, border_radius = 0):
        self.type = 'button'
        font = pg.font.Font(pg.font.match_font(font), font_size)
        geometric_class.__init__(self)
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(size)
        self.w, self.h = size
        self.border_radius = border_radius
        self.text = text
        self.color = color

        if self.border_radius > 0:
            self.image.set_colorkey((0, 0, 0))
            pg.draw.circle(self.image, (1, 1, 1), (self.border_radius, self.border_radius), self.border_radius, 3)
            pg.draw.circle(self.image, (1, 1, 1), (self.w - self.border_radius, self.border_radius), self.border_radius, 3)
            pg.draw.circle(self.image, (1, 1, 1), (self.border_radius, self.h - self.border_radius), self.border_radius, 3)
            pg.draw.circle(self.image, (1, 1, 1), (self.w - self.border_radius, self.h - self.border_radius), self.border_radius, 3)
            pg.draw.circle(self.image, self.color, (self.border_radius, self.border_radius), self.border_radius - 3)
            pg.draw.circle(self.image, self.color, (self.w - self.border_radius, self.border_radius), self.border_radius - 3)
            pg.draw.circle(self.image, self.color, (self.border_radius, self.h - self.border_radius), self.border_radius - 3)
            pg.draw.circle(self.image, self.color, (self.w - self.border_radius, self.h - self.border_radius), self.border_radius - 3)
            pg.draw.rect(self.image, self.color, (self.border_radius, 0, self.w - (2 * self.border_radius), self.h))
            pg.draw.rect(self.image, self.color, (0, self.border_radius, self.w, self.h - (2 * self.border_radius)))
            pg.draw.line(self.image, (1, 1, 1), (self.border_radius, 1), (self.w - self.border_radius, 1), 3);
            pg.draw.line(self.image, (1, 1, 1), (self.border_radius, self.h - 2), (self.w - self.border_radius, self.h - 2), 3);
            pg.draw.line(self.image, (1, 1, 1), (1, self.border_radius), (1, self.h - self.border_radius), 3);
            pg.draw.line(self.image, (1, 1, 1), (self.w - 2, self.border_radius), (self.w - 2, self.h - self.border_radius), 3);
        else:
            self.image.fill(color)
            pg.draw.rect(self.image, (0, 0, 0), (0, 0, self.w, self.h), 5)
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = pos
        txt = font.render(text, True, (255, 255, 255))
        txt_rct = txt.get_rect()
        txt_rct.center = self.w // 2 , self.h // 2
        self.image.blit(txt, txt_rct)
        self.file = file
        self.last = self.image.get_rect()
        self.last.x = self.rect.x
        self.last.y = self.rect.y

    def update(self):
        if self.last.x != self.rect.x or self.last.y != self.rect.y:
            try:
                with open(self.file, 'r') as f:
                    lines = f.readlines()
                    if len(lines) > 5:
                        lines = lines[:5]
                    with open(self.file, 'w') as F:
                        for i in lines:
                            if i != lines[-1]:
                                x = i[:-1]
                            else:
                                x = i
                            F.write(x)
                            F.write('\n')
                        F.write(str(int(self.w)) + ' ' + str(int(self.h)) + '\n')
                        F.write(str(self.rect.x) + ' ' + str(self.rect.y))
                        F.close()
                    f.close()
            except:
                pass
            self.last.x = self.rect.x
            self.last.y = self.rect.y

class Input(pg.sprite.Sprite, geometric_class):
    def __init__(self, path, pos, size, color, border_radius = 0):
        self.type = 'input'
        pg.sprite.Sprite.__init__(self)
        self.w, self.h = size
        geometric_class.__init__(self)
        self.image = pg.Surface(size)
        self.color = color
        self.border_radius = border_radius
        if self.border_radius > 0:
            self.image.set_colorkey((0, 0, 0))
            pg.draw.circle(self.image, (1, 1, 1), (self.border_radius, self.border_radius), self.border_radius, 3)
            pg.draw.circle(self.image, self.color, (self.border_radius, self.border_radius), self.border_radius - 3)
            pg.draw.circle(self.image, (1, 1, 1), (self.w - self.border_radius, self.border_radius), self.border_radius, 3)
            pg.draw.circle(self.image, self.color, (self.w - self.border_radius, self.border_radius), self.border_radius - 3)
            pg.draw.circle(self.image, (1, 1, 1), (self.border_radius, self.h - self.border_radius), self.border_radius, 3)
            pg.draw.circle(self.image, self.color, (self.border_radius, self.h - self.border_radius), self.border_radius - 3)
            pg.draw.circle(self.image, (1, 1, 1), (self.w - self.border_radius, self.h - self.border_radius), self.border_radius, 3)
            pg.draw.circle(self.image, self.color, (self.w - self.border_radius, self.h - self.border_radius), self.border_radius - 3)
            pg.draw.rect(self.image, self.color, (self.border_radius, 0, self.w - (2 * self.border_radius), self.h))
            pg.draw.rect(self.image, self.color, (0, self.border_radius, self.w, self.h - (2 * self.border_radius)))
            pg.draw.line(self.image, (1, 1, 1), (self.border_radius, 2), (self.w - self.border_radius, 2), 5);
            pg.draw.line(self.image, (1, 1, 1), (self.border_radius, self.h - 2), (self.w - self.border_radius, self.h - 2), 5);
            pg.draw.line(self.image, (1, 1, 1), (2, self.border_radius), (2, self.h - self.border_radius), 5);
            pg.draw.line(self.image, (1, 1, 1), (self.w - 2, self.border_radius), (self.w - 2, self.h - self.border_radius), 5);
        else:
            self.image.fill((255, 255, 255))
            data = [0] * 4
            data[2], data[3] = size
            pg.draw.rect(self.image, self.color, data, 5)
        self.rect = self.image.get_rect()
        self.last = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.last = self.image.get_rect()
        self.last.x, self.last.y = pos
        self.file = path

    def update(self):
        if self.last.x != self.rect.x or self.last.y != self.rect.y:
            try:
                with open(self.file, 'r') as f:
                    lines = f.readlines()[:4]
                    lines[-1] += '\n'
                    with open(self.file, 'w') as F:
                        for i in lines:
                            F.write(i)
                        F.write(str(int(self.w)) + ' ' + str(int(self.h)) + '\n')
                        F.write(str(self.rect.x) + ' ' + str(self.rect.y))
                        F.close()
                    f.close()
            except:pass
            self.last.x = self.rect.x
            self.last.y = self.rect.y

class Movie(pg.sprite.Sprite, geometric_class):
    def __init__(self, m, pos, size, border_radius):
        self.type = 'movie'
        pg.sprite.Sprite.__init__(self)
        self.w, self.h = size
        geometric_class.__init__(self)
        self.image = pg.Surface((self.w, self.h))
        self.image.fill((255, 255, 255))
        self.color = (100, 100, 100)
        pg.draw.rect(self.image, self.color, (0, 0, self.w, self.h), 5)
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = pos
        self.last = self.image.get_rect()
        self.file = m

    def update(self):
        if self.last.x != self.rect.x or self.last.y != self.rect.y:
            try:
                with open(self.file, 'r') as f:
                    lines = f.readlines()[:1]
                    lines[-1] += '\n'
                    with open(self.file, 'w') as F:
                        for i in lines:
                            F.write(i)
                        F.write(str(int(self.w)) + ' ' + str(int(self.h)) + '\n')
                        F.write(str(self.rect.x) + ' ' + str(self.rect.y))
                        F.close()
                    f.close()
            except:pass
            self.last.x = self.rect.x
            self.last.y = self.rect.y

class Box(pg.sprite.Sprite):
    def __init__(self, text, pos):
        pg.sprite.Sprite.__init__(self)
        self.writable = True
        self.selection = False
        self.f = pg.font.Font(pg.font.match_font("arial"), 20, bold = True)
        self.text = text
        self.pointer = len(self.text)
        self.txt = self.f.render(text, True, (0, 0, 0))
        self.image = pg.Surface((self.txt.get_width()+10, self.txt.get_height()))
        self.image.fill((255, 255, 255))
        self.set_text(text, self.f)
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = pos
        self.rect.x += 10
        seff.rect.y += 10
        self.indexing = [0, 0]
        self.ind = 0
    def set_text(self, text, font):
        self.text = text
        self.txt = font.render(text, True, (0, 0, 0))
        self.image.blit(self.txt, (0, 0))
        self.image.set_colorkey((255, 255, 255))
    def update(self):
        self.image.fill((255, 255, 255))
        self.txt = self.f.render(self.text, True, (0, 0, 0))
        self.image.blit(self.txt, (0, 0))
        t = self.f.render(self.text[:self.pointer], True, (0, 0, 0))
        self.image.set_colorkey((255, 255, 255))
        pg.draw.line(self.image, (0, 0, 0), (t.get_width(), 0), (t.get_width(), self.image.get_height()),1)



class Table(pg.sprite.Sprite):
    def __init__(self, pos, size, heads, file):
        pg.sprite.Sprite.__init__(self)
        self.heads = heads
        self.geometric = False
        self.size = size
        self.boxes = self.init_table(len(self.heads), size)
        self.image = pg.Surface((self.max * (len(self.boxes[0])), self.high * (len(self.boxes) + 1)))
        self.image.fill((255, 255, 255))
        pg.draw.line(self.image, (0, 0, 0), (0, 0), (0, self.image.get_height()))
        for i in range(1, len(self.boxes[0]) + 1):
            pg.draw.line(self.image, (0, 0, 0), (self.image.get_width() // (len(self.boxes[0])) * i, 0), (self.image.get_width() // (len(self.boxes[0])) * i,self.image.get_height()), 3)
        pg.draw.line(self.image, (0, 0, 0), (0, 0), (self.image.get_width(), 0))
        for i in range(1,(len(self.boxes) + 2)):
            pg.draw.line(self.image, (0, 0, 0), (0, self.image.get_height() // (len(self.boxes) + 1) * i), (self.image.get_width(), self.image.get_height() // (len(self.boxes) + 1) * i), 3)
        position = [self.image.get_width() // (len(self.boxes[0])), self.image.get_height() // (len(self.boxes) + 1)]
        column = 0
        for text in self.heads:
            i = Box(text, (0, 0))
            i.rect.x, i.rect.y = position[0] * column + 5, 5
            self.image.blit(i.image, i.rect)
            column += 1
        column = 0
        for text in self.boxes:
            sheet = 0
            for i in text:
                i.rect.x, i.rect.y= position[0] * sheet, position[1] * column + 1
                self.image.blit(i.image, i.rect)
                sheet += 1
            column += 1
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.last = self.image.get_rect()

        self.file = file


    def init_table(self, x, y):
        l = []
        self.max = 0
        self.high = 0
        for i in self.heads:
            b = Box(i, (0, 0))
            self.max = max(self.max, b.txt.get_width() + 20)
        self.high = b.txt.get_width() + 10
        for i in range(y):
            a = []
            for j in range(x):
                b = Box('', (0, 0))
                b.indexing = [i, j]
                self.max = max(self.max, b.txt.get_width() + 20)
                a.append(b)
            l.append(a)
        return l;
    def get_geo(self, x, y):
        self.max = 0
        for i in self.heads:
            b = Box(i, (0, 0))
            self.max = max(self.max, b.txt.get_width() + 20)
        for i in range(y):
            for j in range(x):
                self.max = max(self.max, self.boxes[i][j].txt.get_width() + 20)
    def update(self):
        if self.last.x != self.rect.x or self.last.y != self.rect.y:
            try:
                with open(self.file, 'r') as f:
                    lines = f.readlines()[:4 + len(self.heads)]
                    lines.append('\n')
                    with open(self.file, 'w') as F:
                        for i in lines:
                            F.write(i)
                        print(self.rect)
                        F.write(str(self.rect.x) + ' ' + str(self.rect.y))
                        F.close()
                    f.close()
            except :pass
            self.last.x = self.rect.x
            self.last.y = self.rect.y
        try:
            with open(self.file[:-4] + '.tab.data', 'w') as f:
                for i in self.boxes:
                    for j in i[:-1]:
                        if j.text != '':
                            f.write(j.text + ' ')
                        else:
                            f.write('* ')
                    if i[-1].text != '':
                        f.write(i[-1].text + '\n')
                    else:
                        f.write('*\n')
                f.close()
        except:pass
        self.get_geo(len(self.boxes[0]), len(self.boxes))
        self.image = pg.Surface((self.max * (len(self.boxes[0])), self.high * (len(self.boxes) + 1)))
        self.image.fill((255, 255, 255))
        pg.draw.line(self.image, (0, 0, 0), (0, 0), (0, self.image.get_height()))
        for i in range(1, len(self.boxes[0]) + 1):
            pg.draw.line(self.image, (0, 0, 0), (self.image.get_width() // (len(self.boxes[0])) * i, 0), (self.image.get_width() // (len(self.boxes[0])) * i,self.image.get_height()), 3)
        pg.draw.line(self.image, (0, 0, 0), (0, 0), (self.image.get_width(), 0))
        for i in range(1,(len(self.boxes) + 2)):
            pg.draw.line(self.image, (0, 0, 0), (0, self.image.get_height() // (len(self.boxes) + 1) * i), (self.image.get_width(), self.image.get_height() // (len(self.boxes) + 1) * i), 3)
        position = [self.image.get_width() // (len(self.boxes[0])), self.image.get_height() // (len(self.boxes) + 1)]
        column = 0
        for text in self.heads:
            i = Box(text, (0, 0))
            i.rect.x, i.rect.y = position[0] * column + 5, 5
            self.image.blit(i.image, i.rect)
            column += 1
        column = 1
        for text in self.boxes:
            sheet = 0
            for i in text:
                i.rect.x, i.rect.y= position[0] * sheet, position[1] * column + 1
                self.image.blit(i.image, i.rect)
                sheet += 1
            column += 1
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.last.x, self.last.y
dictionary = {'red':(255, 0, 0),
 'green':(0, 255, 0),  'blue':(0, 0, 255),  'black':(1, 1, 1),  'white':(255, 255, 255),  'yellow':(255, 255, 0)}
