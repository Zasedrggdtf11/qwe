import pygame

import os
from PIL import Image

def extractFrames(inGif, outFolder):
    frame = Image.open(inGif)
    nframes = 0
    while frame:
        frame.save(f'{outFolder}\{os.path.basename(inGif)}-{nframes}.png', 'PNG')
        nframes += 1
        try:
            frame.seek(nframes)
        except EOFError:
            break
    return True

class Tileset:
    def __init__(self, file,output,v,name, size=(200, 400), margin=0, spacing=0):
        self.file = file
        self.size = size
        self.v =v
        self.name = name
        self.output = output
        self.margin = margin
        self.spacing = spacing
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()
    def save_set(self):
        a = 0
        os.mkdir(self.output)
        for i in self.tiles:
            pygame.image.save(i,f'{self.output}\{self.name}{a}.png')
            a +=1


    def load(self):
        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing

        for y in range(y0, h, dy):
            for x in range(x0, w, dx):

                tile = pygame.Surface(self.size,pygame.SRCALPHA)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)
                self.v -=1
                if self.v == 0:
                    break

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'
#tileset = Tileset('Новая папка\FlyingObelisk_no_lightnings_no_letter.png')
#tileset.load()
#tileset.save_set()
#
#
#extractFrames('Новая папка\\NightBorne_attack.gif','NightBorne_attack')

#tileset2 = Tileset('Новая папка\\25.png','bones',(1000,153))
#tileset2.load()
#tileset2.save_set()

tileset3 = Tileset('NightBorne.png','hero',5,'hero',(1840,80))
tileset3.load()
tileset3.save_set()
tileset3 = Tileset('hero\\hero0.png','hero\\stoyka',9,'stoyka',(80,80))
tileset3.load()
tileset3.save_set()
tileset3 = Tileset('hero\\hero1.png','hero\\run',6,'run',(80,80))
tileset3.load()
tileset3.save_set()
tileset3 = Tileset('hero\\hero2.png','hero\\atack',12,'atack',(80,80))
tileset3.load()
tileset3.save_set()
tileset3 = Tileset('hero\\hero3.png','hero\\harm',5,'harm',(80,80))
tileset3.load()
tileset3.save_set()
tileset3 = Tileset('hero\\hero4.png','hero\\dead',21,'dead',(80,80))
tileset3.load()
tileset3.save_set()
