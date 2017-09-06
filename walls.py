#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Импортируем библиотеку pygame
import pygame

from pygame import *
from constant import *
from map import *

class Walls(sprite.Sprite):
    def __init__(self, x, y, col, plas=0):

        sprite.Sprite.__init__(self)
        self.tiles = RenderMap().getTiles()
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = self.tiles[col]
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

