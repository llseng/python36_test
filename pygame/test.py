# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-21 17:20:34
# @LastEditors: llseng
# @LastEditTime: 2021-01-21 17:20:35
#

import pygame, os, random

def main():
    pygame.init()
    
    screen = pygame.display.set_mode( (800, 600) )
    pygame.display.set_caption('小球吃大球')

    screen.fill((255, 255, 255))

    # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    pygame.draw.circle(screen, (255, 0, 0,), (100, 100), 30, 0)
    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    pygame.display.flip()
    
    ball_image = pygame.image.load( os.path.dirname( __file__ ) + "/../source/bt.jpg" )
    screen.blit( ball_image, (100, 150) )
    pygame.display.flip()

    x, y = 50, 50

    runing = True
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
        
        screen.fill( ( 255, 255, 255 ) )
        # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
        pygame.draw.circle(screen, (255, 0, 50,), (x, y), 30, 0)
        # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
        pygame.display.flip()

        pygame.time.delay(10)
        if x > 500:
            x, y = 50, 50
        else:
            x, y = x + 1, y + 1

if __name__ == "__main__":
    main()