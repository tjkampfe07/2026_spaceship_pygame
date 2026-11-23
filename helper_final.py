import pygame

class Title:
    def __init__ (self,x,y):
        '''get title screen'''
        # title font
        self.font_fn = "StarJedi-DGRW.ttf"
        self.title_font = pygame.font.Font(self.font_fn,100)
        self.title_surface = self.title_font.render('Project Void',1, (255,255,255))
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.center = (x,y-50)
        
        # make new text
        self.font_fn = "StarJedi-DGRW.ttf"
        self.subtitle_font = pygame.font.Font(self.font_fn,25)
        self.subtitle_surface = self.subtitle_font.render('Press Spacebar To Begin!',1,(255,255,255))
        self.subtitle_rect = self.subtitle_surface.get_rect()
        self.subtitle_rect.center = (x,y+75)
        
    def game_over(self, score):
        '''get game over screen'''
        self.font_fn = "StarJedi-DGRW.ttf"
        self.title_font = pygame.font.Font(self.font_fn,100)
        self.title_surface = self.title_font.render('Game over!', 1, (255,255,255))
        text_position = self.title_rect.center
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.center = text_position
        
        self.subtitle_font = pygame.font.Font(self.font_fn, 50)
        self.subtitle_surface = self.subtitle_font.render(f'Final Score: {score}', 1, (255,255,255))
        self.subtitle_rect = self.subtitle_surface.get_rect()
        self.subtitle_rect.center = (text_position[0], text_position[1] + 100)
        
    def draw (self, screen):
        screen.blit(self.title_surface, self.title_rect)
        screen.blit(self.subtitle_surface, self.subtitle_rect)


