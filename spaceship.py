import pygame
from missle import Missle
from math import atan2, pi

class Spaceship(pygame.sprite.Sprite):
    def __init__ (self,x,y,missles, screen):
        self.fp = r'C:\Users\m293330\Documents\EW200_AY27\Final_Project\kenney_space-shooter-extension\PNG\Sprites\Ships\spaceShips_001.png'
        self.image = pygame.image.load(self.fp)
        self.image = pygame.transform.rotate(self.image,90)
        self.og_image = self.image
        self.rect = self.image.get_rect()
        ship = pygame.image.load(self.fp)
        self.x = x
        self.y = y
        self.theta = 30
        self.speed = 15
        self.delta = 5
        self.missles = missles
        self.t_shot = 0 # the last time I shot a missle
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
    def draw(self,screen):
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.image = pygame.transform.rotate(self.og_image,self.theta)
        self.new_image = pygame.transform.rotate(self.image,self.theta)
        self.rect = self.image.get_rect(center=(self.x,self.y))
        screen.blit(self.image, (self.rect))
        
    def shoot(self, screen):
        t_now = pygame.time.get_ticks()
        if t_now - self.t_shot > 200:
            new_missle = Missle(self.x,self.y,self.theta, screen)
            self.missles.add(new_missle)
            self.t_shot = t_now
        else:
            print('Reloading')
            
            
    def update(self,screen):
        
        self.rect.center = (self.x, self.y)
        self.check_keys()
        
        if self.x <= 0:
            self.vx = 0
            self.x = 5
        
        if self.x >= 16*64 - 5:
            self.vx = 0
            self.x = 16*64 - 5
        
    def check_mouse(self,e):
        if e.type == pygame.MOUSEMOTION:
            print(e.pos)
            delta_x = e.pos[0] - self.x
            delta_y = e.pos[1] - self.y
            phi = atan2(-delta_y, delta_x)
            self.theta = int(phi*180/pi)
            
            
    def check_keys(self, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y = self.y - 2
            print('UP')
        if keys[pygame.K_s]:
            self.y = self.y + 2
            print('DOWN')
        if keys[pygame.K_d]:
            self.x = self.x + 2
            print('RIGHT')
        if keys[pygame.K_a]:
            self.x = self.x - 2
            print('LEFT')
        if keys[pygame.K_SPACE]:
            self.shoot()



    
