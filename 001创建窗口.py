#!/usr/bin/env python3
import pygame,time

def main():
    # 创建一个窗口
    screen = pygame.display.set_mode((640,480),0,32)

    # 创建一个背景图片
    background = pygame.image.load("./未标题-1.JPG")

    while True:
        screen.blit(background,(0,0))
        pygame.display.update()
        time.sleep(0.02)

if __name__ == "__main__":
    main()    
