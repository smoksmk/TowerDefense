#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Импортируем библиотеку pygame
import pygame

from pygame import *
from constant import *


class Walls(sprite.Sprite):
    def __init__(self, x, y, col):

        sprite.Sprite.__init__(self)
        self.tiles = RenderMap().getTiles()
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = self.tiles[col]
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class RenderMap(sprite.Sprite):
    def __init__(self):
        self.tiles = "data/tiles.png"
        self.tilesSize = [640, 704]
        self.tecsturiesSize = [64, 64]
        self.images = []
        temp = pygame.image.load(self.tiles).convert_alpha()
        for y in range(0, self.tilesSize[1], self.tecsturiesSize[1]):  # Нужно брать большую сторону для правельного отсчета

            for x in range(0, self.tilesSize[0], self.tecsturiesSize[0]):

                self.images.append(temp.subsurface(x, y,  self.tecsturiesSize[0],  self.tecsturiesSize[1]))

    def getTiles(self):
        return self.images

