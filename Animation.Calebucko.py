# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:13:37 2024

@author: Caleben Jahn
"""
import pygame

def main():
    pygame.init()
    
    screen= pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Oh boy oh boy!")
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,255,0))
    
    saxman = pygame.image.load("C:/Users/clbja/OneDrive/Pictures/Saved Pictures/Saxguy.png")
    saxman.convert_alpha()
    saxman =pygame.transform.scale(saxman, (150,100))
    saxman_x = 0
    saxman_y = 150
    
    clock = pygame.time.Clock()
    keepgoing= True
    while(keepgoing):
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepgoing= False
        saxman_x += 3 
        if saxman_x > screen.get_width():
            saxman_x =0
        saxman_y +=5
        if saxman_y > screen.get_width():
            saxman_y =0
        screen.blit(background, (0,0))
        screen.blit(saxman, (saxman_x, saxman_y))
        pygame.display.flip()
    
    pygame.quit()
    
if __name__=="__main__":
    main()
        
    
    