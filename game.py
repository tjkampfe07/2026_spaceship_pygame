import pygame
from spaceship import Spaceship
from missle import Missle
from rock import Rock
from helper_final import Title


pygame.init()
clock = pygame.time.Clock()

TS = 64
WIDTH = 16*TS
HEIGHT = 12*TS
SIZE = (WIDTH, HEIGHT)

title = Title(WIDTH/2, HEIGHT/2-50)


screen = pygame.display.set_mode(SIZE)

# get bg
bg = pygame.Surface(SIZE,pygame.SRCALPHA)
bg.fill((0,150,200))

missles = pygame.sprite.Group()

USS_Enterprise = Spaceship(WIDTH/2,HEIGHT/2, missles, screen)
running = 1

# make space bg
space_fp = r'C:\Users\m293330\Documents\EW200_AY27\Final_Project\skybox-space-galaxy.png'
space_surf = pygame.image.load(space_fp)
space_surf = pygame.transform.rotozoom(space_surf,0,0.5)

rocks = pygame.sprite.Group()
num_rocks = [10]
for i in range(num_rocks[0]):
    rocks.add(Rock(SIZE,num_rocks, screen))
    
    
score = 0
pygame.font.init()
f = pygame.font.Font(size=50)

# intro screen loop

# intro screen loop
running = 1
while running:
    screen.blit(bg,(0,0))
    title.draw(screen)
    pygame.display.flip()
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            running = 0
        if e.type == pygame.KEYDOWN:
            running = 0


running = 1
# main game loop
while running:
    clock.tick(60)
    # blit bg
    screen.blit(bg,(0,0))
    screen.blit(space_surf,(-500,-100))
    #draw Enterprise
    USS_Enterprise.draw(screen)
    for m in missles:
        m.update()
        m.draw(screen)
    
    
    
    rocks.update()
    if len(rocks) < 10:
        rocks.add(Rock(SIZE, num_rocks, screen))
        
    rocks.draw(screen)
    
    score_surface = f.render(f'Score: {score}', 1, (255,255,255))
    screen.blit(score_surface, (25, 50))
    
    pygame.display.flip()
    
    collided_rocks = pygame.sprite.groupcollide(missles,rocks,1,1)
    
    for k, v in collided_rocks.items():
        for r in v:
            if score < 100: 
                if not r.exploded:  
                    r.explode()
                    score += 1
            elif score < 1000:
                if not r.exploded:
                    r.explode()
                    score += 10
    
    # update ship 
    USS_Enterprise.update()
    
    events = pygame.event.get()        

    for e in events:
        #leave while loop
        if e.type == pygame.QUIT:
            running = 0
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_q:
                running = 0
        USS_Enterprise.check_mouse(e)
        
    if pygame.sprite.spritecollide(USS_Enterprise, rocks, 1):
            running = 0

        
# game over loop
title.game_over(score)

# End game loop
bg.fill((255,0,0))
running = 1
while running:
    # blit bg
    screen.blit(bg,(0,0))
    title.draw(screen)
    pygame.display.flip()
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            running = 0
        if e.type == pygame.KEYDOWN:
            running=0



pygame.quit()
