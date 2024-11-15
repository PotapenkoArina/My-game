from modules import *

import pygame
pygame.init()
#


if __name__ == "__main__":
    
    game = True
    #
    while game:
        
        # game_window.fill(color = (255, 0, 0))
        game_window.blit(fg_image, (0,0))
        
        game_window.blit(hero.image, (hero.hero_x, hero.hero_y))
        hero.animation()
        
        game_window.blit(hunter_1.image, (hunter_1.hero_x, hunter_1.hero_y))
        hunter_1.animation()
        
        game_window.blit(wizard.image, (wizard.hero_x, wizard.hero_y))
        wizard.animation()
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game = False
        
        pygame.display.flip()
