#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Импортируем библиотеку pygame
import pygame

from pygame import *
from constant import *
from mob import *
from walls import *


def main():

    pygame.init()                                       #Инициализация PyGame
    hero = Player(100, 100)  # создаем героя по (x,y) координатам
    left = right = up = down = False  # по умолчанию — стоим

    timer = pygame.time.Clock()
    screen = pygame.display.set_mode(DISPLAY)           #Создаем окошко
    pygame.display.set_caption("Tower Defense")         #Пищем щапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))               #Создание видимокй поверхности
    bgFlor = pygame.sprite.Group()
    entities = pygame.sprite.Group()
    entities.add(hero)  # Все объекты
    x = y = 0       # Начинаем отрисовку с 0 координат

    for row in flor:
        for col in row:
            if col != 0:
                pf = Walls(x, y, int(col))
                bgFlor.add(pf)
                # Создаем блок разкрашиваем его цветом

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    platforms = []                                      # то, во что мы будем врезаться или опираться
                                                        #Будем ее как фон
    # bg.fill(Color(BACKGROUND_COLOR))                    #Заливаем ее одним цветом

    x = y = 0
    for row in Wall:
        for col in row:


            if col != 0:
                pf = Walls(x, y, int(col))
                entities.add(pf)
                # Создаем блок разкрашиваем его цветом
                platforms.append(pf)

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0


    while 1:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit, "QUIT"

            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False

        # screen.blit(bg, (0, 0))
        hero.update(left, right, up, down, platforms)  # передвижение
        bgFlor.draw(screen)
        entities.draw(screen)  # отображение всего

        # screen.blit(bg, (0,0)) #Каждую интерацию надо все перересовывать
        pygame.display.update() #Обновление и вывод всех изменений на экран



if __name__ == "__main__":
    main()
