#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Импортируем библиотеку pygame
import pygame, math

from pygame import *
from constant import *
from projective import *


class Tower(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.timer = pygame.time.Clock()
        self.mobSptrite = renderTower()
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.angle = 90
        self.size = 32
        self.colour = (255, 255, 255)
        self.thickness = 1
        self.distanse = 128
        self.oldAngle = self.angle
        self.image = Surface((WIDTH, HEIGHT))
        self.shoots = []
        self.projectiv = Projectiv(self.startX, self.startY)

        self.image = self.mobSptrite.getMobPosisn(self.angle)
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект



    def update(self, screen, enemyPos):

        if abs(self.startX - enemyPos[0]) < self.distanse and abs(self.startY - enemyPos[1]) < self.distanse:
            self.angle = self.getangleToEnemy(enemyPos)
            if len(self.shoots)<1:
                print "shoot"
                self.projectiv.rotate(self.angle+90)
                self.shoots.append(self.projectiv)
                print self.shoots
            # print self.projectiv.getPos()
            if self.projectiv.getPos() > (self.startX+200, self.startY+200):
                print "remove"
                self.shoots.remove(0)

            self.projectiv.update()
            self.projectiv.draw(screen)
            self.angle = self.getangleToEnemy(enemyPos)
            self.image = self.mobSptrite.getMobPosisn(self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            screen.blit(self.image, self.rect)



    def getangleToEnemy(self, player ):
        # Позиция башни
        YTowerPos = self.startY
        XTowerPos = self.startX
        # Позиция врага
        YEnemyPos = player[1]
        XEnemePos = player[0]
        # Вычесляем где находится враг
        result = math.atan2(YTowerPos - YEnemyPos, XEnemePos - XTowerPos) * (180 / math.pi)

        return result




class renderTower(sprite.Sprite):
    def __init__(self):
        self.tiles = "data/tank.gif"
        self.tilesSize = [594, 265]
        self.tecsturiesSize = [32, 32]
        self.images = []
        self.counts = 0
        temp = pygame.image.load(self.tiles).convert_alpha()

        self.images.append(temp.subsurface(331, 265, self.tecsturiesSize[0], self.tecsturiesSize[1]))

    def getMobPosisn(self, angle=0):
        return pygame.transform.rotate(self.images[0], angle)


