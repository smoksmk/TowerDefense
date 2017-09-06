#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Импортируем библиотеку pygame
import pygame

from pygame import *
from constant import *



class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.mobSptrite = renderMob()
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y


        self.image = Surface((WIDTH, HEIGHT))
        self.image = self.mobSptrite.getMobTiles(2)

        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

    def update(self, left, right, up, down, platforms):
        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image = self.mobSptrite.getMobTiles(7)

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image = self.mobSptrite.getMobTiles(6)

        if up:
            self.yvel = -MOVE_SPEED  # Вверх = x- n
            self.image = self.mobSptrite.getMobTiles(4)
        if down:
            self.yvel = MOVE_SPEED  # Вниз = x + n
            self.image = self.mobSptrite.getMobTiles(5)

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        if not (up or down):
            self.yvel = 0


        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)


    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает



class renderMob(sprite.Sprite):
    def __init__(self):
        self.tiles = "data/tank.gif"
        self.tilesSize = [594, 265]
        self.tecsturiesSize = [32, 32]
        self.images = []
        self.counts = 0
        temp = pygame.image.load(self.tiles).convert_alpha()
        for y in range(1, 264, 33):
            imagesTails = []
            for x in range(330,559,33):
                imagesTails.append(temp.subsurface(x+1, y, self.tecsturiesSize[0], self.tecsturiesSize[1]))
            self.images.append(imagesTails)

    def getMobTiles(self, vektor):
        self.counts +=1
        if self.counts == 7: self.counts = 0
        return self.images[vektor][self.counts]
