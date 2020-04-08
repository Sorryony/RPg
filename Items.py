import pygame


class Item(object):
    bone_i = [pygame.image.load("assets/Pics/Bone.png")]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = True

    def draw(self, win):
        win.blit(self.bone_i[0], (self.x, self.y))
