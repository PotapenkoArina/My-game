from ..abs_path import abspath
from .hero import Hero
import pygame 

pygame.init()

class Wizard(Hero):
    def __init__(self, **kwargs):
        Hero.__init__(
            self,
            hero_x= 550,
            all_name_image= ['/wizard/0.png', '/wizard/1.png', '/wizard/2.png', '/wizard/3.png'],
            **kwargs
        )
        
wizard = Wizard()
        