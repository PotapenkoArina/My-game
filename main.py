from modules import *
import pygame
from modules.level_1.wizard import *
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
        game_window.blit(wizard.image, (wizard.wizard_x, wizard.wizard_y))
        wizard.animation()
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game = False
        
        pygame.display.flip()
