import pygame

import Main
import Menu

win = pygame.display.set_mode((1536, 288))


class MainPlayer(object):


    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
        self.jumpCount = 7
        self.j_land = -7
        self.walkCount = 0
        self.standing = True
        self.a_bow = False
        self.a_attack = False
        self.isJump = False
        self.left = False
        self.right = True
        self.hitBox = (self.x + 15, self.y + 7, 20, 30)
        self.health = 100

    def draw(self, win):

        if self.walkCount + 1 >= 18:
            self.walkCount = 0

        if self.standing:
            if self.right:
                if self.a_bow:
                    win.blit(ani_bow[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.a_attack:
                    win.blit(s_attack[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(char[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1

            elif self.left:
                if self.a_bow:
                    win.blit(ani_bow_2[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.a_attack:
                    win.blit(s_attack2[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.left:
                    win.blit(char_2[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1

        elif not self.standing:
            if self.right:
                if self.a_bow:
                    win.blit(ani_bow[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.a_attack:
                    win.blit(s_attack[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            elif self.left:
                if self.a_bow:
                    win.blit(ani_bow_2[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.a_attack:
                    win.blit(s_attack2[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.left:
                    win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
        pygame.draw.rect(win, (255, 0, 0), (55, 25, 100, 10))
        pygame.draw.rect(win, (0, 255, 0), (55, 25, self.health, 10))
        self.hitBox = (self.x + 15, self.y + 7, 20, 30)
        # pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)

    def hit(self):
        if self.health > 0:
            self.health -= Main.Skeleton.damage
        else:
            Main.Skeleton.attack = False
            death_txt = pygame.font.SysFont('Sans', 100)
            text = death_txt.render('YOU DIED!', 1, (255, 0, 0))
            Main.win.blit(text, (768, 144))
            # deathSound.play()
            pygame.display.update()
            i = 0
            while i < 300:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()
            Main.Chosen.health = 100
            Menu.game_intro()

        if Main.Skeleton.left:
            self.x -= 50

        elif Main.Skeleton.right:
            self.x += 50

        if not self.isJump:
            self.isJump = True
            self.walkCount += 1

        '''else:
            if self.jumpCount_hit >= self.j_land_hit:
                neg = 1
                if self.jumpCount_hit < 0:
                    neg = -1
                self.y -= (self.jumpCount_hit ** 2) * 0.5 * neg
                self.jumpCount_hit -= 1
            else:
                self.isJump = False
                self.jumpCount_hit = 2'''


class Projectile(object):
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 9 * facing
        self.damage = 2

    def draw(self, win):
        win.blit(pro_tile_r, (self.x, self.y))


class Swing(object):
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.right = False
        self.left = False
        self.walkCount = 0
        self.facing = facing
        self.vel = 8 * facing
        self.damage = 5

    def draw(self, win):
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if Main.Chosen.right and self.x >= Main.Chosen.x:
            win.blit(pro_swing[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        if Main.Chosen.left and self.x - 30 <= Main.Chosen.x:
            win.blit(pro_swing_L[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1


walkRight = [pygame.image.load('assets/Pics/adventurer-run3-00.png'), pygame.image.load('assets/Pics/adventurer-run3-01.png'),
             pygame.image.load('assets/Pics/adventurer-run3-02.png'), pygame.image.load('assets/Pics/adventurer-run3-03.png'),
             pygame.image.load('assets/Pics/adventurer-run3-04.png'), pygame.image.load('assets/Pics/adventurer-run3-05.png')]
walkLeft = [pygame.image.load('assets/Pics/adventurer-run3-00-L.png'), pygame.image.load('assets/Pics/adventurer-run3-01-L.png'),
            pygame.image.load('assets/Pics/adventurer-run3-02-L.png'), pygame.image.load('assets/Pics/adventurer-run3-03-L.png'),
            pygame.image.load('assets/Pics/adventurer-run3-04-L.png'), pygame.image.load('assets/Pics/adventurer-run3-05-L.png')]
char = [pygame.image.load('assets/Pics/adventurer-idle-2-00.png'), pygame.image.load('assets/Pics/adventurer-idle-2-01.png'),
        pygame.image.load('assets/Pics/adventurer-idle-2-02.png'), pygame.image.load('assets/Pics/adventurer-idle-2-00.png'),
        pygame.image.load('assets/Pics/adventurer-idle-2-01.png'), pygame.image.load('assets/Pics/adventurer-idle-2-02.png')]
char_2 = [pygame.image.load('assets/Pics/adventurer-idle-2-00-L.png'), pygame.image.load('assets/Pics/adventurer-idle-2-01-L.png'),
          pygame.image.load('assets/Pics/adventurer-idle-2-00-L.png'), pygame.image.load('assets/Pics/adventurer-idle-2-01-L.png'),
          pygame.image.load('assets/Pics/adventurer-idle-2-00-L.png'), pygame.image.load('assets/Pics/adventurer-idle-2-01-L.png')]
s_attack = [pygame.image.load('assets/Pics/adventurer-attack3-02.png'), pygame.image.load('assets/Pics/adventurer-attack3-02.png'),
            pygame.image.load('assets/Pics/adventurer-attack3-02.png'), pygame.image.load('assets/Pics/adventurer-attack3-02.png'),
            pygame.image.load('assets/Pics/adventurer-attack3-02.png'), pygame.image.load('assets/Pics/adventurer-attack3-02.png')]
s_attack2 = [pygame.image.load('assets/Pics/adventurer-attack3-02-L.png'), pygame.image.load('assets/Pics/adventurer-attack3-02-L.png'),
             pygame.image.load('assets/Pics/adventurer-attack3-02-L.png'), pygame.image.load('assets/Pics/adventurer-attack3-02-L.png'),
             pygame.image.load('assets/Pics/adventurer-attack3-02-L.png'), pygame.image.load('assets/Pics/adventurer-attack3-02-L.png')]
ani_bow = [pygame.image.load('assets/Pics/adventurer-bow-07.png'), pygame.image.load('assets/Pics/adventurer-bow-07.png'),
           pygame.image.load('assets/Pics/adventurer-bow-07.png'), pygame.image.load('assets/Pics/adventurer-bow-07.png'),
           pygame.image.load('assets/Pics/adventurer-bow-07.png'), pygame.image.load('assets/Pics/adventurer-bow-07.png')]
ani_bow_2 = [pygame.image.load('assets/Pics/adventurer-bow-07-L.png'), pygame.image.load('assets/Pics/adventurer-bow-07-L.png'),
             pygame.image.load('assets/Pics/adventurer-bow-07-L.png'), pygame.image.load('assets/Pics/adventurer-bow-07-L.png'),
             pygame.image.load('assets/Pics/adventurer-bow-07-L.png'), pygame.image.load('assets/Pics/adventurer-bow-07-L.png')]
pro_swing = [pygame.image.load('assets/Pics/effect_attack.png'), pygame.image.load('assets/Pics/effect_attack.png'),
             pygame.image.load('assets/Pics/effect_attack.png'), pygame.image.load('assets/Pics/effect_attack.png'),
             pygame.image.load('assets/Pics/effect_attack.png'), pygame.image.load('assets/Pics/effect_attack.png')]
pro_swing_L = [pygame.image.load('assets/Pics/effect_attack_2.png'), pygame.image.load('assets/Pics/effect_attack_2.png'),
               pygame.image.load('assets/Pics/effect_attack_2.png'), pygame.image.load('assets/Pics/effect_attack_2.png'),
               pygame.image.load('assets/Pics/effect_attack_2.png'), pygame.image.load('assets/Pics/effect_attack_2.png')]
pro_tile = pygame.image.load('assets/Pics/trail_00.png').convert()
pro_tile_r = pygame.transform.scale(pro_tile, (10, 5))
