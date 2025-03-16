import pygame
from sys import exit 

def scores():
    time = pygame.time.get_ticks() - active_score
    score = test_text3.render(f'score: {int(time/1000)}', False, 'white')
    score_rect = score.get_rect(center = (150, 100))
    screen.blit(score, score_rect)

pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption('Runner v667')
clock = pygame.time.Clock()

test_text = pygame.font.Font('font/Ninja Note.ttf', 50)
test_text2 = pygame.font.Font('font/Ninja Note.ttf', 250)
test_text3 = pygame.font.Font('font/Ninja Note.ttf', 35)

active_score = 0
teext = test_text.render('Aidan-chan', False, '#5c3c3c')
teext2 = test_text2.render('RETAKE', False, 'red')

backgr = pygame.image.load('images/photo_2025-03-16_16-39-13.jpg').convert_alpha()
ninja = pygame.image.load('images/sticker.webp').convert_alpha()
shuriken = pygame.image.load('images/shuriken.png').convert_alpha()
restart = pygame.image.load('images/reload.png').convert_alpha()

original_width, original_height = ninja.get_size() 
new_height = 300 
new_width = int((new_height / original_height) * original_width)

backgr = pygame.transform.scale(backgr, (1600, 900))
ninja = pygame.transform.scale(ninja, (new_width, new_height))
shuriken = pygame.transform.scale(shuriken, (100, 100))
restart = pygame.transform.scale(restart, (150, 150))

ninja_rect = ninja.get_rect(midbottom = (350, 300))
shuriken_rect = shuriken.get_rect(midtop = (1800, 650))
restart_rect = restart.get_rect(midtop = (800, 600))

AA = True
gravity = 0
active = True

def reset():
    global AA, gravity, ninja_rect, shuriken_rect, active, active_score
    AA = True
    gravity = 0
    active = True
    ninja_rect.midbottom = (350, 300)  
    shuriken_rect.midtop = (1800, 650)
    active_score = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        """if event.type == pygame.MOUSEMOTION:
            print(pygame.mouse.get_pos())"""
        if active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and ninja_rect.bottom >= 815:
                    gravity = -25
        else: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    reset()

    if active:
        if ninja_rect.bottom >= 815:
            ninja_rect.bottom = 815

        screen.blit(backgr, (0, 0))
        screen.blit(ninja, ninja_rect)
        screen.blit(teext, (600, 80))

        pygame.draw.line(screen, '#100c1c', (0, 815), (1600, 815), 10)
        
        screen.blit(shuriken, shuriken_rect)

        if AA == True: shuriken_rect.x -= 15 
        if shuriken_rect.right <= 0:
            shuriken_rect.left = 1600
        
        if shuriken_rect.colliderect(ninja_rect):
            active = False
            
        if ninja_rect.bottom >= 815:
            ninja_rect.bottom = 815

        gravity += 1
        ninja_rect.y += gravity
        scores()
    else:
        AA = False
        screen.blit(teext2, (200, 280))
        screen.blit(restart, restart_rect)
        
    pygame.display.update()
    clock.tick(60)
