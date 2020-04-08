import pygame

import Main


class Enemy(object):
    walkRight = [pygame.image.load("assets/Pics/swr000.png"), pygame.image.load("assets/Pics/swr001.png"), pygame.image.load("assets/Pics/swr002.png"),
                 pygame.image.load("assets/Pics/swr003.png"), pygame.image.load("assets/Pics/swr004.png"), pygame.image.load("assets/Pics/swr005.png"),
                 pygame.image.load("assets/Pics/swr006.png"), pygame.image.load("assets/Pics/swr007.png"), pygame.image.load("assets/Pics/swr008.png"),
                 pygame.image.load("assets/Pics/swr009.png"), pygame.image.load("assets/Pics/swr010.png"), pygame.image.load("assets/Pics/swr011.png"),
                 pygame.image.load("assets/Pics/swr012.png")]
    walkLeft = [pygame.image.load("assets/Pics/swl000.png"), pygame.image.load("assets/Pics/swl001.png"), pygame.image.load("assets/Pics/swl002.png"),
                pygame.image.load("assets/Pics/swl003.png"), pygame.image.load("assets/Pics/swl004.png"), pygame.image.load("assets/Pics/swl005.png"),
                pygame.image.load("assets/Pics/swl006.png"), pygame.image.load("assets/Pics/swl007.png"), pygame.image.load("assets/Pics/swl008.png"),
                pygame.image.load("assets/Pics/swl009.png"), pygame.image.load("assets/Pics/swl010.png"), pygame.image.load("assets/Pics/swl011.png"),
                pygame.image.load("assets/Pics/swl012.png")]
    m_attackRight = [pygame.image.load("assets/Pics/smar007.png"), pygame.image.load("assets/Pics/smar008.png"),
                     pygame.image.load("assets/Pics/smar009.png"), pygame.image.load("assets/Pics/smar010.png"),
                     pygame.image.load("assets/Pics/smar011.png"), pygame.image.load("assets/Pics/smar012.png"),
                     pygame.image.load("assets/Pics/smar013.png"), pygame.image.load("assets/Pics/smar014.png"),
                     pygame.image.load("assets/Pics/smar015.png"), pygame.image.load("assets/Pics/smar016.png"),
                     pygame.image.load("assets/Pics/smar017.png")]
    m_attackLeft = [pygame.image.load("assets/Pics/smal007.png"), pygame.image.load("assets/Pics/smal008.png"),
                    pygame.image.load("assets/Pics/smal009.png"), pygame.image.load("assets/Pics/smal010.png"),
                    pygame.image.load("assets/Pics/smal011.png"), pygame.image.load("assets/Pics/smal012.png"),
                    pygame.image.load("assets/Pics/smal013.png"), pygame.image.load("assets/Pics/smal014.png"),
                    pygame.image.load("assets/Pics/smal015.png"), pygame.image.load("assets/Pics/smal016.png"),
                    pygame.image.load("assets/Pics/smal017.png")]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [Main.Chosen.x, self.x]
        self.walkCount = 0
        self.vel = 5
        self.attack = False
        self.right = False
        self.left = True
        self.isJump = False
        self.jumpCount = 10
        self.j_land = -10
        self.hitBox = (self.x, self.y + 9, 17, 27)
        self.health = 10
        self.max_health = 10
        self.visible = True
        self.drop = False
        self.damage = 10

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.right:
                if self.attack:
                    win.blit(self.m_attackRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            elif self.left:
                if self.attack:
                    win.blit(self.m_attackLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.left:
                    win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitBox[0] - 5, self.hitBox[1] - 10, self.max_health, 5))
            pygame.draw.rect(win, (0, 255, 0), (self.hitBox[0] - 5, self.hitBox[1] - 10, self.health, 5))
            self.hitBox = (self.x + 5, self.y + 5, 17, 30)
        # pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)

    def move(self):
        if self.vel >= 0:
            self.right = True
            self.left = False

            if self.x + self.vel <= self.path[1]:
                self.x += self.vel
                self.path[1] = Main.Chosen.x
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            self.left = True
            self.right = False

            if self.x - self.vel >= self.path[0]:
                self.x += self.vel
                self.path[0] = Main.Chosen.x
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        Main.hitSound.play()

        if Main.Skeleton.health <= 0:
            self.hitBox = (0, 0, 0, 0)
            self.visible = False
            self.drop = True

        if self.left:
            self.x += 20

        elif self.right:
            self.x -= 20

        if not self.isJump:
            self.isJump = True
            self.walkCount += 1
        else:
            if self.jumpCount >= self.j_land:
                if self.jumpCount < 0:
                    self.y -= (self.jumpCount ** 2) * 0.5
                    self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

        print("Hit!")
