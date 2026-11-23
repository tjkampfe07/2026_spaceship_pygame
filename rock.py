import pygame
from random import randint, uniform

class Rock(pygame.sprite.Sprite):
    def __init__(self, size, num_rocks, screen):
        pygame.sprite.Sprite.__init__(self)
        self.rock = r'C:\Users\m293330\Documents\EW200_AY27\Final_Project\kenney_space-shooter-extension\PNG\Sprites\Meteors\spaceMeteors_001.png'
        self.image = pygame.image.load(self.rock)
        self.image = pygame.transform.rotozoom(self.image, randint(0, 360), uniform(0.1, 0.5))
        self.x = randint(0, size[0])
        self.y = randint(0, size[1])
        while (size[0]/2 - 200 < self.x < size[0]/2 + 200) and (size[1]/2 - 200 < self.y < size[1]/2 + 200):
            self.x = randint(0, size[0])
            self.y = randint(0, size[1])
            
        self.vx = randint(-5, 5) / 10
        self.vy = randint(-5, 5) / 10
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.exploded = False
        self.exploded_time = 0
        self.width, self.height = size
        self.num_rocks = num_rocks
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
    def explode(self):
        self.explode_img = r'C:\Users\m293330\Documents\EW200_AY27\Final_Project\kenney_space-shooter-extension\PNG\Sprites\Effects\spaceEffects_015.png'
        self.image = pygame.image.load(self.explode_img)
        self.rect = self.image.get_rect(center = self.rect.center)
        
        # log explode time
        self.vx = 0
        self.vy = 0
        self.exploded = True
        self.exploded_time = pygame.time.get_ticks()
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        
        self.rect.center = (self.x, self.y)
             
        if self.exploded:
            if pygame.time.get_ticks() - self.exploded_time > 2000: 
                self.kill()
                
        # see if not inside screen, then kill
        if not self.screen_rect.contains(self.rect):
            # missle is outside screen kill it
            self.kill()
        
    def draw(self, screen):
        self.update()

        self.new_image = pygame.transform.rotate(self.image, self.theta)

        self.rect = self.new_image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, self.rect)
