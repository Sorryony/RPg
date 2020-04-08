import pygame

import Main


class Start(object,):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.hitbox = (self.x + 15, self.y + 7, 100, 50)


    def draw(self, win):

        if self.visible:
            start = pygame.image.load("assets/Pics/Start.jpg").convert()
            start2 = pygame.transform.scale(start, (100, 50))
            win.blit(start2, (450, 75))
            self.hitbox = (self.x + 15, self.y + 7, 100, 50)


class Exit(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True

    def draw(self, win):

        if pygame.MOUSEBUTTONUP:
            pass

        if self.visible:
            exit = pygame.image.load("assets/Pics/Exit.jpg").convert()
            exit2 = pygame.transform.scale(exit, (100, 50))
            win.blit(exit2, (450, 200))
            self.hitbox = (self.x + 15, self.y + 7, 100, 50)


class Character_image_intro(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.walkCount = 0
        self.images = [pygame.image.load('assets/Pics/adventurer-run3-00.png'), pygame.image.load('assets/Pics/adventurer-run3-01.png'),
                       pygame.image.load('assets/Pics/adventurer-run3-02.png'), pygame.image.load('assets/Pics/adventurer-run3-03.png'),
                       pygame.image.load('assets/Pics/adventurer-run3-04.png'), pygame.image.load('assets/Pics/adventurer-run3-05.png')]

    def draw(self, win_intro):

        if self.walkCount + 1 >= 18:
            self.walkCount = 0

        if self.visible:
            win_intro.blit(self.images[self.walkCount // 3], (300, 217))
            self.walkCount += 1


def game_intro():

    win_intro = pygame.display.set_mode((700, 288))
    intro_x1 = 0
    intro_x2 = Main.bg.get_width()


    intro = True
    while intro:

        intro_x1 -= 2
        intro_x2 -= 2

        if intro_x1 < Main.bg.get_width() * -1:
            intro_x1 = Main.bg.get_width()
        if intro_x2 < Main.bg.get_width() * -1:
            intro_x2 = Main.bg.get_width()
        win_intro.blit(Main.bg, (intro_x1, 0))
        win_intro.blit(Main.bg, (intro_x2, 0))

        start_press = pygame.image.load("assets/Pics/Start_press.jpg").convert()
        start_press2 = pygame.transform.scale(start_press, (100, 50))
        exit_press = pygame.image.load("assets/Pics/Exit_press.jpg").convert()
        exit_press2 = pygame.transform.scale(exit_press, (100, 50))

        # Character and Monsters
        Main.start_intro.draw(win_intro)
        Main.exit_intro.draw(win_intro)
        Main.Cii_intro.draw(win_intro)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if Main.start_intro.hitbox[0] + Main.start_intro.hitbox[2] > pos[0] > Main.start_intro.hitbox[0] and Main.start_intro.hitbox[1] + Main.start_intro.hitbox[3] > pos[1] > \
                        Main.start_intro.hitbox[1]:
                    Main.win.blit(start_press2, (450, 75))
                    Main.Chosen.health = 100
                    Main.game_loop()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if Main.exit_intro.hitbox[0] + Main.exit_intro.hitbox[2] > pos[0] > Main.exit_intro.hitbox[0] and Main.exit_intro.hitbox[1] + Main.exit_intro.hitbox[3] > pos[1] > \
                        Main.exit_intro.hitbox[1]:
                    Main.win.blit(exit_press2, (450, 200))
                    quit()

            if Main.start_intro.hitbox[0] + Main.start_intro.hitbox[2] > pos[0] > Main.start_intro.hitbox[0] and Main.start_intro.hitbox[
                1] + Main.start_intro.hitbox[3] > pos[1] > \
                    Main.start_intro.hitbox[1]:
                Main.win.blit(start_press2, (450, 75))

            if Main.exit_intro.hitbox[0] + Main.exit_intro.hitbox[2] > pos[0] > Main.exit_intro.hitbox[0] and Main.exit_intro.hitbox[1] + \
                    Main.exit_intro.hitbox[3] > pos[1] > \
                    Main.exit_intro.hitbox[1]:
                Main.win.blit(exit_press2, (450, 200))

        Main.clock.tick(27)
        pygame.display.update()
