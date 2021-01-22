# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-21 18:52:06
# @LastEditors: llseng
# @LastEditTime: 2021-01-21 18:52:07
#

import pygame
from random import randint
from enum import Enum, unique
from math import sqrt, pi

@unique
class Color( Enum ):
    """
    颜色枚举
    """
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 128, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    @staticmethod
    def random():
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        return ( r, g, b )

class Ball(object):
    """
    球
    """
    def __init__(self, name, x, y, radius, sx, sy, color=(255, 0, 0)):
        """
        构造函数
        """
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.area = (radius * pi) ** 2
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True
        self.steps = 0

    def move( self, screen ):
        self.x += self.sx
        self.y += self.sy
        self.steps += 1
        # 每一千步 增长一像素
        if not self.steps % 1000:
            self.steps = 0
            self.radius += 2
            self.area = (self.radius * pi) ** 2

        if self.x - self.radius < 0 or self.x + self.radius > screen.get_width():
            self.sx = -self.sx 
        if self.y - self.radius < 0 or self.y + self.radius > screen.get_height():
            self.sy = -self.sy 

    def eat( self, other ):
        self.area = self.area + other.area
        self.radius = sqrt( self.area ) // pi
        other.alive = False
    
    def draw( self, screen ):
        pygame.draw.circle( screen, self.color, (self.x, self.y), self.radius )
    
def main():
    balls = []

    pygame.init()
    
    screen = pygame.display.set_mode( (100, 100) )
    pygame.display.set_caption( "大球吃小球" )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = randint( 5, screen.get_width() - 5 ), randint( 5, screen.get_height() - 5 )
                sx, sy = randint( -5, 5 ), randint( -5, 5 )
                balls.append( Ball( 'name_%d' % randint(1, 1000), x, y, 2, sx, sy ) )

        screen.fill( (255, 255, 255) )

        for b in balls:
            if b.alive:
                if b.radius > min( screen.get_height(), screen.get_width() ) / 2:
                    running = False
                b.draw( screen )
            else:
                balls.remove( b )
        
        pygame.display.flip()
        pygame.time.delay(10)
        # 移动与碰撞
        for b in balls:
            if not b.alive: continue
            b.move( screen )
            for o in balls:
                if not o.alive: continue
                if b == o: continue
                total_radius = b.radius + o.radius
                if abs( b.x - o.x ) >= total_radius or abs( b.y - o.y ) >= total_radius: continue
                if b.radius >= o.radius:
                    b.eat( o )
                else:
                    o.eat( b )
                    break

    else:
        print( "游戏结束" )

if __name__ == "__main__":
    main()