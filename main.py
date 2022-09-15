import pygame
from time import sleep,time

from Game import Game
from Player import Player





def main():
    FPS=1/60
    size=(1080,720)
    screen = pygame.display.set_mode(size)
    game=Game()
    game.addPlayer(Player())
    
    
    
    while True:
        t0=time()
        events=pygame.event.get()
        keys=pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT: 
                end=True
                pygame.quit()
                quit()
        screen.fill((0,0,0))
        
        
        
        
        
        
        
        game
        t1=time()
        if t1-t0<FPS:
            sleep(FPS-(t1-t0))
     
     
main()   
