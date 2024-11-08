import pygame
from .abs_path import abspath

pygame.init()

screen_width = 1000
screen_height = 750



game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title= 'My Game')


fg_image = abspath(name_file= 'лес.jpg')
fg_image = pygame.image.load(fg_image)
fg_image = pygame.transform.scale(fg_image, (screen_width, screen_height))

