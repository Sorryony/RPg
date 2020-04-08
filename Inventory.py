import pygame


class Inventory(object):

    def __init__(self, objects, slots, gold):
        self.gold = 0
        self.objects = []
        self.slots = 20

    def draw(self, win):
        font = pygame.font.SysFont("Sans", 30, True, True)
        txt = font.render('Items:{}'.format(len(self.objects)), 1, (0, 0, 255))
        win.blit(txt, (1200, 10))
