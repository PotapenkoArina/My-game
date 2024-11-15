# from ..abs_path import abspath
import pygame 
from .hero import Hero

pygame.init()

class Hunter(Hero):
    def __init__(self,  **kwargs):
        Hero.__init__(
           self,
           hero_x= 300,
           all_name_image= ['/hunter/0.png','/hunter/1.png','/hunter/2.png','/hunter/3.png'],
           **kwargs
        )
        
hunter_1 = Hunter()
