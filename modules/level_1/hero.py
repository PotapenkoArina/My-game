from ..abs_path import abspath
import pygame 

pygame.init()

class Hero:
    def __init__(
            self,
            hero_width: int= 320,
            hero_height: int= 230, 
            hero_x: int= 5, 
            hero_y: int= 520, 
            count_animation:int= 0,
            all_name_image: list= ['/main_character/0.png', '/main_character/1.png', '/main_character/2.png'],
            count: int= 0
            ):
                self.hero_width= hero_width
                self.hero_height= hero_height
                self.hero_x= hero_x
                self.hero_y= hero_y
                self.count_animation= count_animation
                self.all_name_image = all_name_image
                self.list_image = []
                self.count = count
                
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

        
        