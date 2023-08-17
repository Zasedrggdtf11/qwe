from pygame import *
import os
import time as tm
hieght = 1000
weight = 1000
window = display.set_mode((weight,hieght))
BLACK = (0,0,0)
display.set_caption('pyton')
a = 1
finish = 0
ani_start = tm.time()
ani_end = tm.time()
#back = transform.scale(image.load('back.jpg'),(weight,hieght))
def parser(dir,w,h):
    file_names = os.listdir(dir)
    spisoc = []
    for i in file_names:
        spisoc.append(transform.scale(image.load(dir+'\\'+i),(w,h)))
    return spisoc
class My_Sprite(sprite.Sprite):
    def __init__(self,name,w,h,x,y):
        self.image = transform.scale(image.load(name),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y= y
        super().__init__()
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Man(My_Sprite):
    def __init__(self,name,w,h,x,y,ani,speed):
        super().__init__(name,w,h,x,y)
        self.ani = ani
        self.rect = Rect((x,y),(w/6,h/6))
        self.shift_x = w/6
        self.shift_y = h/6
        self.speed = speed
        self.counter = 0
        self.animator()
    def draw(self):
        #draw.rect(window,(255,0,0),self.rect)
        #window.blit(self.image,(self.rect.x+self.shift_x,self.rect.y+self.shift_y))
        window.blit(self.image,(self.rect.x-25,self.rect.y-35))
    def animator(self):
        self.image = self.ani[self.counter]
        self.counter +=1
        if self.counter == len(self.ani):
            self.counter = 0
    def control(self):
        keys = key.get_pressed()
        if (keys[K_w]or keys[K_UP])and self.rect.y >0:
            self.rect.y -= self.speed
        if (keys[K_a]or keys[K_LEFT])and self.rect.x>0:
            self.rect.x -= self.speed
        if (keys[K_d]or keys[K_RIGHT])and self.rect.x < weight-self.rect.width:
            self.rect.x += self.speed
        if (keys[K_s]or keys[K_DOWN])and self.rect.y <hieght-self.rect.height:
            self.rect.y += self.speed
        #if keys[K_SPACE]:
        #    self.fire()
    def fire(self):
        bullets.add(Bullet('bullet1).png',10,10,self.rect.right,self.rect.centery,20))

class Bullet(My_Sprite):
    def __init__(self,name,w,h,x,y,speed):
        super().__init__(name,w,h,x,y)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > weight:
            self.kill()


class Enemy(My_Sprite):
    def __init__(self,name,w,h,x,y,speed):
        super().__init__(name,w,h,x,y)
        self.speed = speed
        self.direction_x =1
        self.direction_y =1
    def update(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y
        if self.rect.x > weight-self.rect.width or self.rect.x < -0 or \
            sprite.groupcollide(enemies,walls,False,True):
            self.direction_x *= -1
        if self.rect.y > weight-self.rect.height or self.rect.y < -0:
            self.direction_y *= -1
        col_list = sprite.spritecollide(self,enemies,False)
        for i in col_list:
            if not self is i:
                self.direction_y *= -1
                self.direction_x *= -1
        


bullets = sprite.Group()

enemies = sprite.Group()
enemies.add (Enemy('skull_skull.png',100,100,500,200,20))
enemies.add (Enemy('bones.png',100,100,300,200,40))




qwe = Man('hero\\run\\run0.png',300,300,30,400,parser('hero\\run',100,100),40)

final = My_Sprite('obelisk\\obelisk0.png',50,110,600,600)

walls = sprite.Group()
walls.add (My_Sprite('skull.png',120,200,150,200))
walls.add (My_Sprite('skull.png',300,100,150,300))
walls.add (My_Sprite('skull.png',120,200,250,370))
game_over= (My_Sprite('game_over.jpg',1000,1000,0,0))



while a:
    time.delay(60)
    for i in event.get():
        
        if i.type == QUIT:
            a = 0
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                qwe.fire()
    window.fill(BLACK)
    
    if not finish:
        last_pos = qwe.rect.x,qwe.rect.y
        qwe.control()
        enemies.update()
        bullets.update()
        if sprite.spritecollide(qwe,walls,False):
            qwe.rect.x,qwe.rect.y = last_pos
        if sprite.collide_rect(qwe,final) or sprite.spritecollide(qwe,enemies,False) :
            finish = True
        sprite.groupcollide(bullets,enemies,True,True)
        sprite.groupcollide(bullets,walls,True,False)
        #window.blit(back,(0,0))
        walls.draw(window)
        enemies.draw(window)
        bullets.draw(window)
        qwe.draw()
        final.draw()
        if ani_end - ani_start >= 0.001:
            qwe.animator()
            ani_start = tm.time()
        ani_end = tm.time()
    else:
        game_over.draw()
    display.update()

