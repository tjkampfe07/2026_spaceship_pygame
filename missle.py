import pygame
from math import cos, sin, pi

class Missle(pygame.sprite.Sprite):
    def __init__ (self,x,y,theta, screen):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.theta=theta
        self.speed= 10
        
        self.dx = self.speed*cos(self.theta*pi/180)
        self.dy = -self.speed*sin(self.theta*pi/180)
        
        self.fp = r'C:\Users\m293330\Documents\EW200_AY27\Final_Project\kenney_space-shooter-extension\PNG\Sprites\Missiles\spaceMissiles_006.png'
        self.image = pygame.image.load(self.fp)
        
        # put missle in line with ships theta
        self.image = pygame.transform.rotate(self.image,0)
        self.og_image = pygame.transform.rotate(self.image,self.theta)
        self.rect = self.image.get_rect(center=(self.x,self.y))
        
        self.og_image = pygame.transform.rotate(self.image,-90)
        self.image = pygame.transform.rotozoom(self.og_image, self.theta, 0.5)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
    def update(self):
        self.rect.center = (self.x, self.y)
        self.x += self.dx
        self.y += self.dy
        
        # see if not inside screen, then kill
        if not self.screen_rect.contains(self.rect):
            # missle is outside screen kill it
            self.kill()
                                        
        
    def draw(self, screen):
        self.update()
        self.new_image = pygame.transform.rotate(self.image, self.theta)
        self.rect = self.new_image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, self.rect)