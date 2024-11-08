from ..abs_path import abspath
import pygame 

pygame.init()

class Wizard:
    def __init__(self):
        self.wizard_width= 325
        self.wizard_height= 240
        self.wizard_x= 550
        self.wizard_y= 520
        self.count_animation_wizard= 0
        self.all_name_image_wizard = ['/wizard/0.png', '/wizard/1.png', '/wizard/2.png', '/wizard/3.png']
        self.list_image_wizard = []
        self.count1 = 0
        self.all_image()
        self.image = self.load_image(name_image= self.all_name_image_wizard[0])
        
    def load_image(self, name_image: str):
        path = abspath(name_file= name_image)
        image = pygame.image.load(path)
        return pygame.transform.scale(image, (self.wizard_width, self.wizard_height))
    
    def all_image(self):
        for el in self.all_name_image_wizard:
            self.list_image_wizard.append(self.load_image(name_image= el))
    
    def animation(self):
        if self.count_animation_wizard == 20:
            self.image = self.list_image_wizard[self.count1]
            self.count1 += 1
            if self.count1 > len(self.all_name_image_wizard) - 1:
                self.count1 = 0
        if self.count_animation_wizard > 80:
            self.count_animation_wizard = 0
        self.count_animation_wizard += 1

wizard = Wizard()
print(wizard.image)