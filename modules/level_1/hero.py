from ..abs_path import abspath
import pygame 

pygame.init()

class Hero:
    def __init__(self):
        self.hero_width= 320
        self.hero_height= 230
        self.hero_x= 5
        self.hero_y= 520
        self.count_animation= 0
        self.all_name_image = ['/main_character/0.png', '/main_character/1.png', '/main_character/2.png']
        self.list_image = []
        self.count = 0
        self.all_image()
        self.image = self.load_image(name_image= self.all_name_image[0])
        
    def load_image(self, name_image: str):
        path = abspath(name_file= name_image)
        image = pygame.image.load(path)
        return pygame.transform.scale(image, (self.hero_width, self.hero_height))
    
    def all_image(self):
        for el in self.all_name_image:
            self.list_image.append(self.load_image(name_image= el))
    
    def animation(self):
        if self.count_animation == 20:
            self.image = self.list_image[self.count]
            self.count += 1
            if self.count > len(self.all_name_image) - 1:
                self.count = 0
        if self.count_animation > 80:
            self.count_animation = 0
        self.count_animation += 1

hero = Hero()
print(hero.image)
        
        