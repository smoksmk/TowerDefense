#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Импортируем библиотеку pygame
import pygame, math

from pygame import *
from constant import *



class Projectiv(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.shootSptrite = Shoot()
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.yvel = 0
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.i = 0

        self.image = Surface((WIDTH, HEIGHT))
        self.image = self.shootSptrite.getshootTiles()
        self.maxRadius = 128
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.speed = 1
        self.oldtime = pygame.time.get_ticks()
        self.radius = 6
        self.angle = 0

    def getPos(self):
        self.rect = self.image.get_rect(center=self.rect.center)
        return self.rect.x, self.rect.y


    def update(self, screen, enemyPos):

        if pygame.time.get_ticks() > self.speed + self.oldtime:
            x = self.startX + self.radius * math.cos(math.radians(90-self.angle))
            y = self.startY + self.radius * math.sin(math.radians(90-self.angle))


            self.rect.x = x
            self.rect.y = y
            self.radius += 1
            self.oldtime = pygame.time.get_ticks()


        if self.radius == self.maxRadius or sprite.collide_rect(self, enemyPos[0]):
            self.kill()
        else:
            screen.blit(self.image, self.rect)



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

    def rotate(self, angle):
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, angle)


class Shoot(sprite.Sprite):
    def __init__(self):
        self.tiles = "data/tank.gif"
        self.tilesSize = [0, 32]
        self.tecsturiesSize = [5, 7]
        self.images = []
        self.counts = 0
        temp = pygame.image.load(self.tiles).convert_alpha()

        self.images.append(temp.subsurface(114, 13, self.tecsturiesSize[0], self.tecsturiesSize[1]))


    def getshootTiles(self):

        return self.images[0]

