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