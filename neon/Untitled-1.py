import pygame
import random
from os import path
import pygame.gfxdraw


#размер графического окна
WIDTH=800
HEIGHT=600
#кардовая частота
FPS=120
#базовые цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
Colour = [WHITE, BLACK, RED, BLUE, GREEN]
speedx = 0
speedy = 0
k = 0
SP=[0,0,0,0,0]
img_dir="img"
snd_dir ="sound"

run = True
damage = False
damage_b = False
delay = 0
delay_b = 0




class Player(pygame.sprite.Sprite):
    global delay
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.image=pygame.transform.scale(pl_fon[0],(50,70))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.frame = 0
        self.frame_rate = 120
        self.timer_old=pygame.time.get_ticks()

    def update(self):
        timer_new=pygame.time.get_ticks()
        if timer_new - self.timer_old > self.frame_rate:
            self.timer_old=timer_new
            self.frame+=1
            self.image=pygame.transform.scale(pl_fon[(self.frame)%2],(50,70))
            self.image.set_colorkey(BLACK)
            '''
            if delay < 10 and delay > 0:
                self.image=pygame.transform.scale(pl_fon[(self.frame)%6 + 6],(50,50))
                self.image.set_colorkey(BLACK)
            else:
                self.image=pygame.transform.scale(pl_fon[(self.frame)%6],(50,50))
                self.image.set_colorkey(BLACK)
            '''           
            
        self.rect.x+=speedx
        self.rect.y+=speedy

        if self.rect.x > WIDTH-50:
            self.rect.x = WIDTH-50
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > HEIGHT-50:
            self.rect.y = HEIGHT-50
        if self.rect.y < 0:
            self.rect.y = 0
            
    
    def shot(self):
        p = Rocket(self.rect.x, self.rect.y)
        all_sprites.add(p)
        rc.add(p)
        shoot_snd.play()
        


class Rocket(pygame.sprite.Sprite):
    def _init_(self, x, y):
        pygame.sprite.Sprite._init_(self)
        self.image=pygame.transform.scale(rc_fon[0],(50,50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x+25, y)
        self.frame = 0
        self.frame_rate = 120
        self.timer_old=pygame.time.get_ticks()

    def update(self):
        timer_new=pygame.time.get_ticks()
        if timer_new - self.timer_old > self.frame_rate:
            self.timer_old=timer_new
            self.frame+=1
            self.image=pygame.transform.scale(rc_fon[(self.frame)%3],(50,50))
            self.image.set_colorkey(BLACK)
            
        self.rect.y+=-2
        if self.rect.y < -50:
            self.kill()
        

class Rocket_boss (pygame.sprite.Sprite):
    def _init_(self, x, y):
        pygame.sprite.Sprite._init_(self)
        self.image=pygame.transform.scale(rc_fon1,(10,20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x+25, y)

    def update(self):
        self.rect.y+=2
        if self.rect.y > 650:
            self.kill()
            
    


class Enemy(pygame.sprite.Sprite):
    def _init_(self, sx):
        pygame.sprite.Sprite._init_(self)
        self.image=pygame.transform.scale(en_fon[random.randint(0, 1)],(70,70))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 750), random.randint(0, 50))
        self.speedx = sx
        self.speedy = random.randint(1, 3)
        
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx


        if self.rect.x > WIDTH-50:
            self.speedx=self.speedx*(-1)
        if self.rect.x < 0:
            self.speedx=self.speedx*(-1)
        if self.rect.y > HEIGHT-50:
            self.rect.y = 0
            self.rect.x = random.randint(0, 750)

    def bou(self):
        self.speedx=self.speedx*(-1)

    def death(self):
        self.kill()

class Boss(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.image=pygame.transform.scale(boss_fon[0],(100,100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 750), random.randint(50, 60))
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(-3, 3)
        self.frame = 0
        self.frame_rate = 120
        self.timer_old=pygame.time.get_ticks()
        
    def update(self):
        timer_new=pygame.time.get_ticks()
        if timer_new - self.timer_old > self.frame_rate:
            self.timer_old=timer_new
            self.frame+=1
            self.image=pygame.transform.scale(boss_fon[(self.frame)%5],(100,100))
            self.image.set_colorkey(BLACK)

        
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx


        if self.rect.x > WIDTH-50:
            self.speedx=self.speedx*(-1)
        if self.rect.x < 0:
            self.speedx=self.speedx*(-1)
        if self.rect.y > HEIGHT//3:
            self.speedy = self.speedy*(-1)
        if self.rect.y <= 0:
            self.speedy = self.speedy*(-1)

    def death(self):
        self.kill()

    def shot(self):
        p = Rocket_boss(self.rect.x, self.rect.y)
        all_sprites.add(p)
        rc_b.add(p)
        shoot_b_snd.play()



class Boom(pygame.sprite.Sprite):
    def _init_(self, center, size):
        pygame.sprite.Sprite._init_(self)
        self.size = size
        if self.size == 1:
            self.image=pygame.transform.scale(boom[0],(70,70))
        if self.size == 2:
            self.image=pygame.transform.scale(boom[0],(300,300))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(boom):
                self.kill()
            else:
                center = self.rect.center
                if self.size == 1:
                    self.image = pygame.transform.scale(boom[self.frame],(70,70))
                if self.size == 2:
                    self.image = pygame.transform.scale(boom[self.frame],(300,300))
                self.image.set_colorkey(BLACK)
                self.rect = self.image.get_rect()
                self.rect.center = center



font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def screentobegin():
    global run
    pygame.mixer.music.play(loops=-1)
    screen.blit(fon,fon_rect)
    draw_text(screen, "КОСМИЧЕСКАЯ", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "СТРЕЛЯЛКА!", 64, WIDTH / 2, HEIGHT / 3 + 30)
    draw_text(screen, "Клавиши со стрелками для перемещения, пробел для стрельбы", 22, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Нажмите клавишу Enter, чтобы начать", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_RETURN:
                    waiting = False
            if event.type == pygame.QUIT:
                run = False
                waiting = False
    
def screentolevel(level):
    global run
    screen.blit(fon,fon_rect)
    draw_text(screen, "УРОВЕНЬ "+str(level)+"!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Нажмите клавишу Enter, чтобы начать", 18, WIDTH / 2, HEIGHT / 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_RETURN:
                    waiting = False
            if event.type == pygame.QUIT:
                run = False
                waiting = False

def screentowin():
    global run
    screen.blit(fon,fon_rect)
    draw_text(screen, "ПОБЕДА!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Нажмите клавишу Escape, чтобы выйти", 18, WIDTH / 2, HEIGHT / 2 + 100)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_ESCAPE:
                    run = False
                    waiting = False
            if event.type == pygame.QUIT:
                run = False
                waiting = False

def gameover():
    global run
    global bs_life
    global pl_life
    global score
    global level
    screen.blit(fon,fon_rect)
    draw_text(screen, "Вы проиграли!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Ваш счёт:"+str(score), 64, WIDTH / 2, HEIGHT / 3 + 30)
    draw_text(screen, "Нажмите клавишу Enter, чтобы начать сначала", 18, WIDTH / 2, HEIGHT / 2 + 100)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_RETURN:
                    bs_life = 5
                    pl_life = 5
                    score = 0
                    waiting = False
            if event.type == pygame.QUIT:
                run = False
                waiting = False
                   
            
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

fon=pygame.image.load(path.join(img_dir,"fon3_1.png")).convert()
fon_rect=fon.get_rect()
pl_fon1=pygame.image.load(path.join(img_dir,"Player1_1.png")).convert()
pl_fon2=pygame.image.load(path.join(img_dir,"Player1_2.png")).convert()
pl_fon=[pl_fon1, pl_fon2]

burst_snd = pygame.mixer.Sound(path.join(snd_dir, 'burst.mp3'))
shoot_snd = pygame.mixer.Sound(path.join(snd_dir, 'shoot.mp3'))
shoot_b_snd = pygame.mixer.Sound(path.join(snd_dir, 'shoot_b.mp3'))

pygame.mixer.music.load(path.join(snd_dir, 'fon.mp3'))
pygame.mixer.music.set_volume(0.4)


en_fon1=pygame.image.load(path.join(img_dir,"Enemy1.png")).convert()
en_fon2=pygame.image.load(path.join(img_dir,"Enemy2.png")).convert()
en_fon=[en_fon1, en_fon2]



boom1=pygame.image.load(path.join(img_dir,"Boom1.png")).convert()
boom2=pygame.image.load(path.join(img_dir,"Boom2.png")).convert()
boom3=pygame.image.load(path.join(img_dir,"Boom3.png")).convert()
boom4=pygame.image.load(path.join(img_dir,"Boom4.png")).convert()
boom5=pygame.image.load(path.join(img_dir,"Boom5.png")).convert()
boom6=pygame.image.load(path.join(img_dir,"Boom6.png")).convert()
boom=[boom1, boom2, boom3, boom4, boom5, boom6]




boss_fon1=pygame.image.load(path.join(img_dir,"Boss1.png")).convert()
boss_fon2=pygame.image.load(path.join(img_dir,"Boss2.png")).convert()
boss_fon3=pygame.image.load(path.join(img_dir,"Boss3.png")).convert()
boss_fon4=pygame.image.load(path.join(img_dir,"Boss4.png")).convert()
boss_fon5=pygame.image.load(path.join(img_dir,"Boss5.png")).convert()
boss_fon=[boss_fon1, boss_fon2, boss_fon3, boss_fon4, boss_fon5]



rc_fon1=pygame.image.load(path.join(img_dir,"rc1.png")).convert()
rc_fon2=pygame.image.load(path.join(img_dir,"rc2.png")).convert()
rc_fon3=pygame.image.load(path.join(img_dir,"rc3.png")).convert()
rc_fon=[rc_fon1, rc_fon2, rc_fon3]




rc_fon1=pygame.image.load(path.join(img_dir,"rc_b.png")).convert()


all_sprites = pygame.sprite.Group()
pl = Player()
pl1 = pygame.sprite.Group()
pl.add(pl1)
all_sprites.add(pl)

en = pygame.sprite.Group()
for i in range(5):
    SP[i]=random.randint(-1, 1)
    m = Enemy(SP[i])
    all_sprites.add(m)
    en.add(m)
rc = pygame.sprite.Group()

count_b = 0
bs_life = 5
pl_life = 5
score = 0
level = 1

while run:
    if score > 500 and level == 2:
        level = 3

    if score > 1000 and level == 4:
        level = 5
    
    if level == 1:
        screentobegin()
        screentolevel(level)
        level = 2

    if level == 3:
        screentolevel(level-1)
        bs = pygame.sprite.Group()
        m1=Boss()
        all_sprites.add(m1)
        bs.add(m1)
        rc_b = pygame.sprite.Group()
        level = 4

    if level == 5:
        screentowin()
        for i in en:
            i.kill()
        for i in rc:
            i.kill()
        pl.kill()
        
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                pl.shot()
            if event.key==pygame.K_UP:
                speedy=-1
            if event.key==pygame.K_DOWN:
                speedy=1
            if event.key==pygame.K_LEFT:
                speedx=-1
            if event.key==pygame.K_RIGHT:
                speedx=1

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                speedy=0
            if event.key==pygame.K_DOWN:
                speedy=0
            if event.key==pygame.K_LEFT:
                speedx=0
            if event.key==pygame.K_RIGHT:
                speedx=0

    
    if score > 500 and level == 4:
        count_b +=1
        if count_b%(random.randint(20, 60))==0 and bs_life > 0:
            m1.shot()
        col2=pygame.sprite.groupcollide(rc, bs, True, False)
        for i in col2:
            bs_life -= 1
            delay_b = 10
            burst_snd.play()
            if bs_life > 0:
                bm = Boom(i.rect.center, 1)
            if bs_life == 0:
                bm = Boom(i.rect.center, 2)
            all_sprites.add(bm)
        #коллизии босс - пули игрока
        col3=pygame.sprite.groupcollide(rc_b, pl1, True, False)
        for i in col3:
            pl_life -= 1
            burst_snd.play()
            delay = 10
            bm = Boom(i.rect.center, 1)
            all_sprites.add(bm)
        #коллизии игрок - пули босса
        col4=pygame.sprite.groupcollide(rc, rc_b, True, True)
        for i in col4:
            burst_snd.play()
            bm = Boom(i.rect.center, 1)
            all_sprites.add(bm)
        #коллизии пули игрока - пули босса

    for i in en:
        col = pygame.sprite.collide_rect_ratio( 0.5 )(pl,i)
        #коллизии игрок - враги
        if col:
            i.kill()
            pl_life -= 1
            burst_snd.play()
            delay = 10
            m = Enemy(random.randint(-1, 1))
            all_sprites.add(m)
            en.add(m)
            bm = Boom(i.rect.center, 1)
            all_sprites.add(bm)
            
        
    col1 =  pygame.sprite.groupcollide(en, rc, True, True)
    #коллизии пули игрока - враги
    for i in col1:
        m = Enemy(random.randint(-1, 1))
        all_sprites.add(m)
        en.add(m)
        score = score + 10
        burst_snd.play()
        bm = Boom(i.rect.center, 1)
        all_sprites.add(bm)
        

    if bs_life == 0:
        m1.death()
        score = score + 100
        bs_life -= 1
        
    clock.tick(FPS)
    all_sprites.update()
    

    if pl_life > 0:
        screen.fill(BLACK)
        screen.blit(fon,fon_rect)
        all_sprites.draw(screen)
        draw_text(screen, 'Мои жизни:'+str(pl_life), 18, 700, 10)
        draw_text(screen, 'Счёт:'+str(score), 18, 700, 35)
        if delay < 10 and delay > 0:
            pygame.gfxdraw.box(screen, pygame.Rect(0, 0, WIDTH, HEIGHT), (255, 0, 0, 100))

        if delay_b < 10 and delay_b > 0:
            pygame.gfxdraw.box(screen, pygame.Rect(0, 0, WIDTH, HEIGHT), (0, 255, 0, 100))
    else:
        gameover()
        for i in rc:
            i.kill()
        if level == 4:
            m1.death()
        level = 1

    delay-=1
    delay_b-=1

        

    pygame.display.flip()
    
pygame.quit()