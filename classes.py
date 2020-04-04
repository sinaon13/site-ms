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
        self.a = Thread(target=(self.events))
        self.a.start()
    def events(self):
        distance = vec(0, 0)
        f = False
        chosen = None
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    del self
                    sys.exit()
                if event.type == pg.MOUSEMOTION:
                    self.mouse.rect.x , self.mouse.rect.y = event.pos
            mouse = pg.mouse.get_pressed()
            r, m, l = mouse
            if r and not f:
                hits = pg.sprite.spritecollide(self.mouse, self.sprites, False)
                if hits:
                    distance.x = self.mouse.rect.x - hits[0].rect.x
                    distance.y = self.mouse.rect.y - hits[0].rect.y
                    chosen = hits[0]
                    f = True
            if not r:
                f = False
            if f:
                if (distance.x > 4 and distance.x < chosen.w - 4) and (distance.y > 4 and distance.y < chosen.h - 4):
                    chosen.rect.x = self.mouse.rect.x - distance.x
                    chosen.rect.y = self.mouse.rect.y - distance.y
                else:
                    if(chosen.geometric):
                        if(distance.x < 4):
                            chosen.w -= self.mouse.rect.x - (chosen.rect.x + distance.x)
                            chosen.image = pg.Surface((chosen.w, chosen.h))
                            chosen.rect.x = self.mouse.rect.x - distance.x
                            x, y = chosen.rect.x, chosen.rect.y
                            chosen.image.fill((255, 255, 255))
                            distance.x = self.mouse.rect.x - chosen.rect.x
                            distance.y = self.mouse.rect.y - chosen.rect.y
                            pg.draw.rect(chosen.image, chosen.color, (0, 0, chosen.w, chosen.h), 5)
                            chosen.rect = chosen.image.get_rect()
                            chosen.rect.x, chosen.rect.y = x, y
                        if(distance.x > chosen.w - 4):
                            chosen.w += self.mouse.rect.x - (chosen.rect.x + distance.x)
                            chosen.image = pg.Surface((chosen.w, chosen.h))
                            chosen.image.fill((255, 255, 255))
                            pg.draw.rect(chosen.image, chosen.color, (0, 0, chosen.w, chosen.h), 5)
                            distance.x = self.mouse.rect.x - chosen.rect.x
                            distance.y = self.mouse.rect.y - chosen.rect.y
                            x, y = chosen.rect.x, chosen.rect.y
                            chosen.rect = chosen.image.get_rect()
                            chosen.rect.x, chosen.rect.y = x, y
                        if(distance.y < 4):
                            chosen.h -= self.mouse.rect.y - (chosen.rect.y + distance.y)
                            chosen.image = pg.Surface((chosen.w, chosen.h))
                            chosen.rect.y = self.mouse.rect.y - distance.y
                            x, y = chosen.rect.x, chosen.rect.y
                            chosen.image.fill((255, 255, 255))
                            distance.x = self.mouse.rect.x - chosen.rect.x
                            distance.y = self.mouse.rect.y - chosen.rect.y
                            pg.draw.rect(chosen.image, chosen.color, (0, 0, chosen.w, chosen.h), 5)
                            chosen.rect = chosen.image.get_rect()
                            chosen.rect.x, chosen.rect.y = x, y
                        if(distance.y > chosen.h - 4):
                            chosen.h += self.mouse.rect.y - (chosen.rect.y + distance.y)
                            chosen.image = pg.Surface((chosen.w, chosen.h))
                            chosen.image.fill((255, 255, 255))
                            pg.draw.rect(chosen.image, chosen.color, (0, 0, chosen.w, chosen.h), 5)
                            distance.x = self.mouse.rect.x - chosen.rect.x
                            distance.y = self.mouse.rect.y - chosen.rect.y
                            x, y = chosen.rect.x, chosen.rect.y
                            chosen.rect = chosen.image.get_rect()
                            chosen.rect.x, chosen.rect.y = x, y

            self.sprites.update()
            self.update()

    def update(self):
        self.screen.fill((255, 255, 255))
        self.sprites.draw(self.screen)
        pg.display.flip()

    def add_item(self, item):
        self.sprites.add(item)


class Text(pg.sprite.Sprite):

    def __init__(self, text, pos, file, font='arial', size=None, color=None):
        pg.sprite.Sprite.__init__(self)
        self.geometric = False
        if size:
            if color:
                f = pg.font.Font(pg.font.match_font(font), size)
                txt = f.render(text, True, color)
                self.image = pg.Surface((txt.get_width(), txt.get_height()))
                self.image.blit(txt, (0, 0))
                self.image.set_colorkey((0, 0, 0))
            else:
                f = pg.font.Font('arial', 20)
                txt = f.render(text, True, (0, 0, 0))
                self.image = pg.Surface((txt.get_width(), txt.get_height()))
                self.image.blit(txt, (0, 0))
                self.image.set_colorkey((0, 0, 0))
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
                        lines = lines[:5]
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
    def __init__(self, file, text, color, pos, size, font = 'arial', font_size = 14):
        font = pg.font.Font(pg.font.match_font(font), font_size)
        geometric_class.__init__(self)
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(size)
        self.w, self.h = size
        self.image.fill(color)
        self.color = color
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
                    if len(lines) > 4:
                        lines = lines[:4]
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
    def __init__(self, path, pos, size, color):
        pg.sprite.Sprite.__init__(self)
        self.w, self.h = size
        geometric_class.__init__(self)
        self.image = pg.Surface(size)
        self.image.fill((255, 255, 255))
        data = [0] * 4
        data[2], data[3] = size
        self.color = color
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
                    lines = f.readlines()[:3]
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
    def __init__(self, m, pos):
        pg.sprite.Sprite.__init__(self)
        self.w = 300
        self.h = 200
        geometric_class.__init__(self)
        self.image = pg.Surface((300, 200))
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



dictionary = {'red':(255, 0, 0),
 'green':(0, 255, 0),  'blue':(0, 0, 255),  'black':(1, 1, 1),  'white':(255, 255, 255),  'yellow':(255, 255, 0)}
